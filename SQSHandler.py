import uuid
import json

import boto3


class SQSHandler:
    AWS_KEY = 'AKIARZPP2F6H24B5GXVA'
    AWS_PSW = 'P61Tdsg5C4mg72PjhPULTFa9dqz0pt5hWRt+K815'
    AWS_REGION = 'eu-central-1'

    def __init__(self, queue_name: str) -> None:
        self.__sqs_client = boto3.client('sqs',
                                         region_name=self.AWS_REGION,
                                         aws_access_key_id=self.AWS_KEY,
                                         aws_secret_access_key=self.AWS_PSW)
        self.__queue_url = self.__sqs_client.get_queue_url(QueueName=queue_name)
        self.__group_id = uuid.uuid4()

    def enqueue_message(self, message_body: str) -> dict:
        response = self.__sqs_client.send_message(QueueUrl=self.__queue_url,
                                                  MessageBody=json.dumps(message_body),
                                                  MessageGroupId=str(self.__group_id))
        return response
