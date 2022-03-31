from instagrapi.types import Media
from Location import Location

class CrawledData:

    def __init__(self, user_id, img_url: list[str], caption_text: str, location: Location = None) -> None:
        self.__user_id = user_id
        self.__img_url = img_url
        self.__caption_text = caption_text
        self.__location = location