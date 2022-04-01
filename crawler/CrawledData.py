from instagrapi.types import Media
from crawler.Location import Location

class CrawledData:

    def __init__(self, username, post_id, date, img_url: list[str], caption_text: str, location: Location = None) -> None:
        self.__username = username
        self.__post_id = post_id
        self.__date = date
        self.__img_url = img_url
        self.__caption_text = caption_text
        self.__location = location
