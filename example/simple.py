from aws_lambda_utils.utils import LambdaFunction


class MyLambda(LambdaFunction):
    def execute(self):
        pass


def lambda_handler(event, context):
    MyLambda(__file__, event, context).execute()


if __name__ == '__main__':
    MyLambda(__file__, {}).execute()
