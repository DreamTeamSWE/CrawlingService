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

    #getters
    def get_username(self) -> str:
        return self.__username
    
    def get_post_id(self) -> str:
        return self.__post_id
    
    def get_date(self) -> str:
        return self.__date

    def get_img_url(self) -> list[str]:
        return self.__img_url

    def get_caption_text(self) -> str:
        return self.__caption_text

    def get_location(self) -> Location:
        return self.__location

    
