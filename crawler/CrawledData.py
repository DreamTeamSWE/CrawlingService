import json

from instagrapi.types import Media
from typing import List

from crawler.Location import Location


class CrawledData:

    def __init__(self, username, post_id, date, img_url: List[str], caption_text: str,
                 location: Location = None) -> None:
        self.__username = username
        self.__post_id = post_id
        self.__date = date
        self.__img_url = img_url
        self.__caption_text = caption_text
        self.__location = location
        self.__s3_id = []

    # getters
    def get_username(self) -> str:
        return self.__username

    def get_post_id(self) -> str:
        return self.__post_id

    def get_date(self) -> str:
        return str(self.__date)

    def get_img_url(self) -> List[str]:
        return self.__img_url

    def get_caption_text(self) -> str:
        return self.__caption_text

    def get_location(self) -> Location:
        return self.__location

    def get_s3_id(self) -> List[str]:
        return self.__s3_id

    def get_id_location(self) -> int:
        return self.__location.get_db_id()

    def add_s3_id(self, s3_id: str) -> None:
        self.__s3_id.append(s3_id)

    def to_json(self) -> str:
        json_obj = {
            "username": self.__username,
            "post_id": self.__post_id,
            "date": str(self.__date),
            "img_url": self.__s3_id,
            "caption_text": self.__caption_text,
            "location": self.__location.to_dict() if self.__location is not None else None
        }
        return json.dumps(json_obj)


