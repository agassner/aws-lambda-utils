import logging


class LambdaFunction:
    def __init__(self, name, event=None, context=None):
        self.event = event
        self.context = context
        self.name = name
        self.config_logger()

    def config_logger(self):
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(format=format)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)

        self.logger = logger

    def _execute(self):
        self.logger.debug('Event: %s' % self.event)
        self.logger.debug('Context: %s' % self.context)

        try:
            self.execute()
            cfnresponse.send(self.event, self.context, cfnresponse.SUCCESS)
        except Exception as e:
            self.logger.error('Error: %s' % e)
            cfnresponse.send(self.event, self.context, cfnresponse.FAILED)

    def execute(self):
        pass
