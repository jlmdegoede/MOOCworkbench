import base64
import logging

from allauth.socialaccount.models import SocialToken
from django.conf import settings
from django.shortcuts import reverse
from github import Github
from github.GithubException import GithubException, UnknownObjectException

from user_manager.models import WorkbenchUser


logger = logging.getLogger(__name__)


class GitHubHelper(object):
    def __init__(self, user, repo_name, create=False):
        """GitHubHelper helps with common functions for GitHub for experiments in the workbench
        :param user: Either a workbench or user instance
        :param repo_name: Repository name for which to initialize the GitHub helper.
        :param create: Boolean to indicate if a repository has to be created, if True new repo is created.
        False by default"""
        self.user = self._get_user(user)

        self.socialtoken = self._get_social_token()
        self.github_object = self._get_github_object()
        self.github_user = self.github_object.get_user()
        self.github_repository = None
        self.repo_name = repo_name

        if create:
            self._create_github_repository()
        elif repo_name is not None:
            self._init_github_repository()

    def _create_github_repository(self):
        self.github_repository = self.github_user.create_repo(self.repo_name)
        self.repo_name = self.github_repository.name
        self._create_webhook()

    def _init_github_repository(self):
        self.github_repository = self.github_user.get_repo(self.repo_name)

    @property
    def owner(self):
        """Gets the GitHub username of the user"""
        return self.github_repository.owner.login

    def get_clone_url(self):
        clone_url = self.github_repository.clone_url
        remaining_clone_url = clone_url.split('https://')[1]
        return 'https://{0}@{1}'.format(self.socialtoken, remaining_clone_url)

    def list_files_in_folder(self, folder='', func=None, *args):
        try:
            folder = self._fix_folder_slashes(folder)
            if func:
                return func(self.github_repository.get_contents(folder), *args)
            return self.github_repository.get_contents(folder)
        except GithubException as e:
            return [e.data['message']]

    def view_file(self, file_name):
        try:
            encoded = self.github_repository.get_file_contents(file_name)
            decoded = base64.b64decode(encoded.content).decode("utf-8")
            return decoded
        except GithubException as e:
            print([e.data['message']])

    def get_commits_in_repository(self, since):
        return self.github_repository.get_commits(since=since)

    def add_file_to_repository(self, file_name, commit_message, folder='', contents=''):
        try:
            repo_file_name = self._get_repo_file_name(file_name, folder)
            self.github_repository.create_file(repo_file_name, commit_message, contents)
        except GithubException as e:
            print(e)

    def update_file(self, file_name, commit_message, contents, folder=''):
        repo_file_name = self._get_repo_file_name(file_name, folder)
        current_file = self.github_repository.get_file_contents(repo_file_name)
        self.github_repository.update_file(repo_file_name, commit_message, contents, current_file.sha)

    def create_release(self, tag_name, name, body, pre_release):
        return self.github_repository.create_git_release(tag_name, name, body, prerelease=pre_release)

    def get_commit(self, sha1_hash):
        return self.github_repository.get_commit(sha1_hash)

    def get_issues(self):
        return self.github_repository.get_issues()

    def create_branch(self, branch_name):
        branches = self.get_branches()
        for branch in branches:
            if branch.name == branch_name:
                return
        latest_commit = self.github_repository.get_commits()[:1]
        for commit in latest_commit:
            latest_commit = commit
        branch = 'refs/heads/{0}'.format(branch_name)
        self.github_repository.create_git_ref(branch, latest_commit.sha)

    def get_branches(self):
        branches = self.github_repository.get_branches()
        return branches

    def get_single_issue(self, issue_nr):
        return self.github_repository.get_issue(issue_nr)

    def _fix_folder_slashes(self, folder):
        if not folder.startswith('/'):
            folder = '/{0}'.format(folder)
        if folder != '/' and folder.endswith('/'):
            folder = folder[:-1]
        return folder

    def _create_webhook(self):
        from helpers.helper import get_absolute_url
        webhook_url = get_absolute_url(to=reverse('webhook_receive'))
        config_dict = {'url': webhook_url,
                       'content_type': 'json',
                       'secret': settings.GITHUB_WEBHOOK_KEY}
        self.github_repository.create_hook('web', config_dict)

    def _get_repo_file_name(self, file_name, folder=''):
        return '/{0}/{1}'.format(folder, file_name) if folder else '/{0}'.format(file_name)

    def _get_github_object(self):
        return Github(login_or_token=self.socialtoken)

    def _get_user(self, user):
        if isinstance(user, WorkbenchUser):
            return user.user
        return user

    def _get_social_token(self):
        socialtoken = SocialToken.objects.filter(account__user=self.user, account__provider='github')
        if socialtoken.count() != 0:
            return socialtoken[0].token
        raise ValueError('SocialToken is missing')

    def _delete_repository(self):
        self.github_repository.delete()


def get_github_helper(request, exp_or_package):
    """Returns GitHubHelper more easily
    :param request: The request, containing the currently signed in user
    :param exp_or_package: DB object to Experiment or InternalPackage"""
    try:
        return GitHubHelper(request.user, exp_or_package.git_repo.name)
    except UnknownObjectException as e:
            logger.error('GitHubHelper could not be initialized for %s (%s) with error: %s', request.user,
                         exp_or_package, e)
