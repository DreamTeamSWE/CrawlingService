import unittest
from crawler.crawled_data.CrawledDataFactory import CrawledDataFactory
from crawler.location.Location import Location
from instagrapi.types import Media
from instagrapi.types import Location as LocationType


class TestCrawledDataFactory(unittest.TestCase):
    def test_build_from_media(self):
        media = Media(id="123", caption_text="test", media_type=1, thumbnail_url="http://test_url.jpg",
                      pk="123", code="test_code", user={"pk":"123", "username":"test_username"},
                      like_count=123, usertags=[], taken_at = "2022-02-02T12:12:12.000Z")
        crawled_data = CrawledDataFactory.build_from_media(media)
        self.assertEqual(crawled_data.get_post_id(), media.id)
        self.assertEqual(crawled_data.get_caption_text(), media.caption_text)

    def test_build_from_media_and_location(self):
        media = Media(id="123", caption_text="test", media_type=1, thumbnail_url="http://test_url.jpg",
                      pk="123", code="test_code", user={"pk":"123", "username":"test_username"},
                      like_count=123, usertags=[], taken_at = "2022-02-02T12:12:12.000Z")
        location = LocationType(name='name', id='id', latitude='latitude', pk=1234)
        crawled_data = CrawledDataFactory.build_from_media_and_location(media, location)
        self.assertEqual(crawled_data.get_post_id(), media.id)
        self.assertEqual(crawled_data.get_caption_text(), media.caption_text)





if __name__ == '__main__':
    unittest.main()
