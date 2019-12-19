from test.adbc.const import ERR_CODE_DEV_TASK_ERROR, ERR_CODE_DEV_TASK_CANCEL
ERR_CODE_PIPELINE_NOT_FOUND = 'dev.pipeline.notfound'
class PipelineException(Exception):
    def __init__(self,message,error_code = ERR_CODE_DEV_TASK_ERROR):
        Exception.__init__(self,message)
        self.error_code = error_code
        self.error_msg = message

class NotFoundException(PipelineException):
    def __init__(self,message):
        super(NotFoundException, self).__init__(message,ERR_CODE_PIPELINE_NOT_FOUND)

class NoMasterPengine(PipelineException):
    def __init__(self,message):
        PipelineException.__init__(self,message)

class PipelineCanceException(Exception):
    def __init__(self, message, error_code=ERR_CODE_DEV_TASK_CANCEL):
        Exception.__init__(self,message)
        self.error_code = error_code
        self.error_msg = message

class StepException(Exception):
    def __init__(self,step,function,*args):
        Exception.__init__(self,*args)
        self.step = step
        self.function = function

    def __str__(self):
        return 'StepException: step=%s; function=%s; message=%s'%(
            self.step, self.function, self.message
        )

class WorkFinished(Exception):
    def __init__(self, is_ok, message):
        self._is_ok = is_ok
        Exception.__init__(self,message)


raise PipelineCanceException("stepmsg",error_code="4567890")