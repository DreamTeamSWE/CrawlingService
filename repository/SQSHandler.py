import uuid

import boto3

from crawler.crawled_data.CrawledData import CrawledData


class SQSHandler:

    def __init__(self, queue_name: str) -> None:
        self.__sqs_client = boto3.client('sqs')
        response = self.__sqs_client.get_queue_url(QueueName=queue_name)
        self.__queue_url = response['QueueUrl']
        self.__group_id = uuid.uuid4()

    def enqueue_message(self, crawled_data_obj: CrawledData) -> dict:
        """
        Enqueues a message to the SQS queue.

        :param crawled_data_obj: CrawledData object to be enqueued.
        :return: SQS response.
        """
        response = self.__sqs_client.send_message(QueueUrl=self.__queue_url,
                                                  MessageBody=crawled_data_obj.to_json(),
                                                  MessageGroupId=str(self.__group_id))
        return response
