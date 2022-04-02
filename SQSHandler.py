import uuid
import json

import boto3

from crawler import CrawledData


class SQSHandler:

    def __init__(self, queue_name: str) -> None:
        self.__sqs_client = boto3.client('sqs')
        self.__queue_url = self.__sqs_client.get_queue_url(QueueName=queue_name)
        self.__group_id = uuid.uuid4()

    def enqueue_message(self, crawled_data_obj: CrawledData) -> dict:
        response = self.__sqs_client.send_message(QueueUrl=self.__queue_url,
                                                  MessageBody=json.dumps(crawled_data_obj.to_json()),
                                                  MessageGroupId=str(self.__group_id))
        return response
