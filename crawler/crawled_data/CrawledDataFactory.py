from instagrapi.types import Media

from crawler.crawled_data.CrawledData import CrawledData
from crawler.location.Location import Location


class CrawledDataFactory:
    @staticmethod
    def build_from_media(media: Media) -> CrawledData:
        """
        Builds a CrawledData object from an instagrapi media object.

        :param media: instagrapi media object
        :return: CrawledData object corresponding to the media object
        """
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
    def build_from_media_and_location(media: Media, location: Location) -> CrawledData:
        """
        Builds a CrawledData object from an instagrapi media object and a location object, the location attribute of the
        returned object is set to the location object.

        :param media: instagrapi media object
        :param location: location object
        :return: CrawledData object corresponding to the media object with location set to the location object
        """
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

    def build_from_media_location_and_username(self, media: Media, location: Location, username: str) -> CrawledData:
        """
        Builds a CrawledData object from an instagrapi media object, a location object and a username, the location
        attribute of the returned object is set to the location object, the username attribute of the returned object is
        set to the username string.

        :param media: instagrapi media object
        :param location: location object
        :param username: username string of the user who posted the media
        :return: CrawledData object corresponding to the media object with location set to the location object and the
        username set to the username string
        """
        crawled_data = self.build_from_media_and_location(media, location)
        crawled_data.set_username(username)
        return crawled_data

    # def build_from_story(self, story: Story):
    #     pass
    #
    # def build_from_db(self, db_data: dict):
    #     pass
