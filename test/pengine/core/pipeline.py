class PipelineFactory(object):
    _pipelines = {}
    _factory = {}
    TASK_TYPE = 'class attribute TASK_TYPE must defined in sub-class'

    def on_create_before(self, task):
        pass

    def get_pipeline_do(self, pipeline_id, task_id = None):
        raise NotImplementedError()

    def get_task_do(self, task_id):
        raise NotImplementedError()
    @staticmethod
    def create_pipeline(cls_name, task_type=None):
        task_types = (task_type,) if task_type else \
            PipelineFactory._pipelines.keys()
        for task_type in task_types:
            pipelines = PipelineFactory._pipelines[task_type]
            if cls_name in pipelines:
                return pipelines[cls_name]()
        raise Exception








pipeline_factory = PipelineFactory()):