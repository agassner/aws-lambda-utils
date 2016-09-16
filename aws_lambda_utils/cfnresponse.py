from botocore.vendored import requests
import json

SUCCESS = "SUCCESS"
FAILED = "FAILED"


def send(event, context, responseStatus, responseData={},
         physicalResourceId=None, logger=None):

    responseUrl = event.get('ResponseURL')

    if responseUrl is None:
        log(logger, 'Response URL not defined, unable to send signal to Cloudformation')
        return

    log(logger, responseUrl)

    responseBody = {}
    responseBody['Status'] = responseStatus
    responseBody['Reason'] = 'See the details in CloudWatch Log Stream: ' + \
        context.log_stream_name
    responseBody['PhysicalResourceId'] = physicalResourceId or \
        context.log_stream_name
    responseBody['StackId'] = event['StackId']
    responseBody['RequestId'] = event['RequestId']
    responseBody['LogicalResourceId'] = event['LogicalResourceId']
    responseBody['Data'] = responseData

    json_responseBody = json.dumps(responseBody)

    log(logger, "Response body:\n" + json_responseBody)

    headers = {
        'content-type': '',
        'content-length': str(len(json_responseBody))
    }

    try:
        response = requests.put(responseUrl,
                                data=json_responseBody,
                                headers=headers)
        log(logger, "Status code: " + response.reason)
    except Exception as e:
        log(logger, "send(..) failed executing requests.put(..): " + str(e))


def log(logger, message):
    if logger is None:
        print(message)
    else:
        logger.info(message)
