import cfnresponse
import logging


class LambdaFunction:
    def __init__(self, name, event=None, context=None, logging_level=logging.INFO):
        self.name = name
        self.event = event
        self.context = context
        self.config_logger(logging_level)

    def config_logger(self, logging_level):
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(format=format)
        logger = logging.getLogger(self.name)
        logger.setLevel(logging_level)

        self.logger = logger

    def call(self):
        self.logger.debug('Event: %s' % self.event)
        self.logger.debug('Context: %s' % self.context)

        try:
            self.execute()
            cfnresponse.send(self.event, self.context, cfnresponse.SUCCESS, logger=self.logger)
        except Exception as e:
            self.logger.error('Error: %s' % e)
            cfnresponse.send(self.event, self.context, cfnresponse.FAILED, logger=self.logger)

    def execute(self):
        pass
