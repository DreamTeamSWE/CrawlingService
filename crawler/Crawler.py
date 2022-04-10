
from instagrapi import Client
import instagrapi.exceptions
import json
import boto3
import random
import time
import logging


from typing import List


class Crawler:

    def __init__(self) -> None:
        self.__cl = Client()

    @staticmethod
    def __emulate_human_behaviour():
        x = random.uniform(5, 15)
        logging.info(f'emulating human behaviour: waiting {round(x,1)} seconds...')
        time.sleep(x)

    def login_from_account(self, username: str, password: str):
        try:
            logging.info("login in progress...")
            self.__cl.login(username, password)
            logging.info("login crawler successful!!")
        except instagrapi.exceptions.ClientError:
            logging.info('an error occoured during log in')

    def save_cookies(self):
        json.dump(self.__cl.get_settings(), open('cookie.json', 'w'))

    def login_from_cookies(self):
        logging.info('login from cookies...')
        s3 = boto3.client(service_name='s3')
        content_object = s3.get_object(Bucket='sweeat-crawler-cookies', Key='instaswe2021.txt')
        file_content = content_object['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        self.__cl = Client(json_content)
        logging.info('login successful!')

    def get_id_from_username(self, username: str):
        return self.__cl.user_id_from_username(username)

    def get_media(self, username: str, amount: int = 0):
        logging.info(f'scraping {amount} medias from {username}...')
        user_instagrapi_id = self.get_id_from_username(username)
        media = self.__cl.user_medias_v1(int(user_instagrapi_id), amount)
        logging.info('medias scraped successfully!')
        return media

    def get_detailed_location(self, loc_name, lat, lng):
        response = self.__cl.fbsearch_places(loc_name, lat, lng)
        if len(response) > 0:
            place = response[0]
            info = self.__cl.location_info_v1(place.pk)
            info.name = loc_name
            info.lat = lat
            info.lng = lng
            self.__emulate_human_behaviour()
            return info
        else:
            self.__emulate_human_behaviour()
            return None

    def does_profile_exists(self, username: str) -> bool:
        try:
            self.get_id_from_username(username)
            return True
        except instagrapi.exceptions.UserNotFound:
            return False

    def is_profile_private(self, username: str) -> bool:
        user_instagrapi = self.__cl.user_info_by_username(username)
        return user_instagrapi.is_private

    def get_public_following_list(self, username: str) -> List[str]:
        user_instagrapi_id = self.get_id_from_username(username)
        following = self.__cl.user_following_v1(user_instagrapi_id)
        return [users.username for users in following if not users.is_private]
