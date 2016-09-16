from aws_lambda_utils import LambdaFunction


class MyLambda(LambdaFunction):
    def execute(self):
        self.logger.info('I am a Lambda Function')


def lambda_handler(event, context):
    MyLambda(__file__, event=event, context=context).call()


if __name__ == '__main__':
    import logging
    MyLambda(__file__, event={'key': 'value'}, context={}, logging_level=logging.DEBUG).call()
