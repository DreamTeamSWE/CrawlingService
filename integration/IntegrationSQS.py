import unittest
from repository.SQSHandler import SQSHandler
from crawler.crawled_data.CrawledData import CrawledData


class TestCrawledData(unittest.TestCase):
    def setUp(self) -> None:
        self.SQS_handler = SQSHandler('integration-test-queue.fifo')

    def test_enqueue_message(self):
        crawled_data_obj = CrawledData('lorenzolinguini',
                                       '2806725869999084478_241913061',
                                       '2022-04-01',
                                       ['https://www.instagram.com', 'https://www.google.com'],
                                       'tutto molto buono!',
                                       None)
        response = self.SQS_handler.enqueue_message(crawled_data_obj)
        self.assertEqual(response['ResponseMetadata']['HTTPStatusCode'], 200)


if __name__ == '__main__':
    unittest.main()
