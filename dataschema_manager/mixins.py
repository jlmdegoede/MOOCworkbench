from experiments_manager.helper import verify_and_get_experiment


class DataSchemaFieldListMixin(object):
    def get_context_data(self, **kwargs):
        context = super(DataSchemaFieldListMixin, self).get_context_data(**kwargs)
        experiment = verify_and_get_experiment(self.request, self.kwargs['experiment_id'])
        data_schema = experiment.schema.first()
        context['data_schema_list'] = data_schema.fields.all()
        context['experiment_id'] = experiment.id
        return context
