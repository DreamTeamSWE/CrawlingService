import unittest
from crawler.location.Location import Location
from crawler.crawled_data.CrawledData import CrawledData


class TestCrawledData(unittest.TestCase):
    def setUp(self) -> None:
        self.crawled_data = CrawledData('lorenzolinguini',
                                        '2806725869999084478_241913061',
                                        '2022-04-01',
                                        ['https://www.instagram.com', 'https://www.google.com'],
                                        'tutto molto buono!',
                                        Location('location_name',
                                                 43.3,
                                                 12.2134,
                                                 'fast food',
                                                 '1234567890',
                                                 'http://www.google.com',
                                                 1))

    def test_get_username(self):
        self.assertEqual(self.crawled_data.get_username(), 'lorenzolinguini')

    def test_get_post_id(self):
        self.assertEqual(self.crawled_data.get_post_id(), '2806725869999084478_241913061')

    def test_get_date(self):
        self.assertEqual(self.crawled_data.get_date(), '2022-04-01')

    def test_get_img_urls(self):
        self.assertEqual(self.crawled_data.get_img_urls(), ['https://www.instagram.com', 'https://www.google.com'])

    def test_get_caption(self):
        self.assertEqual(self.crawled_data.get_caption_text(), 'tutto molto buono!')

    def test_get_s3_id (self):
        self.assertEqual(self.crawled_data.get_s3_id(), [])

    def test_get_id_location(self):
        self.assertEqual(self.crawled_data.get_id_location(), 1)

    def test_set_username(self):
        self.crawled_data.set_username('new_username')
        self.assertEqual(self.crawled_data.get_username(), 'new_username')

    def test_add_s3_id(self):
        self.crawled_data.add_s3_id('123456789')
        self.crawled_data.add_s3_id('987654321')
        self.assertEqual(self.crawled_data.get_s3_id(), ['123456789', '987654321'])


if __name__ == '__main__':
    unittest.main()
