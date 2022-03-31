from instagrapi.types import Media, Story
from CrawledData import CrawledData
from instagrapi import Client

class CrawledDataFactory:
    def build_from_media(self, media: Media) -> CrawledData:
        username = media.user.username
        caption_text = media.caption_text
        img_urls = []
        if media.media_type == 1: #il media è una foto
            img_urls.append(media.thumbnail_url)
        elif media.media_type == 8: #il media è un album
            for resource in media.resources:
                img_urls.append(resource.thumbnail_url)
        
        return CrawledData(username, img_urls, caption_text, )

    def build_from_story(self, story: Story):
        pass

    def build_from_db(self, db_data: dict):
        pass