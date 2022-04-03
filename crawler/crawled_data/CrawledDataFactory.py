from instagrapi.types import Media, Story

from crawler.crawled_data.CrawledData import CrawledData
from crawler.location.Location import Location


class CrawledDataFactory:
    @staticmethod
    def build_from_media(media: Media) -> CrawledData:
        username = media.user.username
        post_id = media.id
        date = media.taken_at
        caption_text = media.caption_text
        img_urls = []
        location = media.location
        if media.media_type == 1:  # il media è una foto
            img_urls.append(media.thumbnail_url)
        elif media.media_type == 8:  # il media è un album
            img_urls.extend(resource.thumbnail_url for resource in media.resources)
        return CrawledData(username, post_id, date, img_urls, caption_text, location)

    @staticmethod
    def build_from_media_and_location(media: Media, location: Location):
        username = media.user.username
        post_id = media.id
        date = media.taken_at.strftime("%Y-%m-%d %H:%M:%S")
        caption_text = media.caption_text
        img_urls = []
        if media.media_type == 1:  # il media è una foto
            img_urls.append(media.thumbnail_url)
        elif media.media_type == 8:  # il media è un album
            img_urls.extend(resource.thumbnail_url for resource in media.resources)
        return CrawledData(username, post_id, date, img_urls, caption_text, location)

    def build_from_story(self, story: Story):
        pass

    def build_from_db(self, db_data: dict):
        pass
