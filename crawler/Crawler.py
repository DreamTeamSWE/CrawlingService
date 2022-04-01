from http import client
from instagrapi import Client
from instagrapi.exceptions import (ClientError)
import json
import boto3

class Crawler:

    def __init__(self) -> None:
        self.__cl = Client()

    def login_from_account (self, username: str, password: str):
        try:
            print("login in progress...")
            self.__cl.login(username, password)
            print("login crawler successful!!")
        except (ClientError):
            print('an error occoured during log in')

    def save_cookies (self):
        json.dump(self.__cl.get_settings(), open('cookie.json', 'w'))

    def login_from_cookies (self):
        print('login from cookies...')
        s3 = boto3.client(service_name = 's3')
        content_object = s3.get_object(Bucket = 'sweeat-crawler-cookies', Key = 'DreamTeamUnipd.txt')
        file_content = content_object['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        self.__cl = Client(json_content)
        print ('login successful!')

    def get_id_from_username (self, username: str):
        return self.__cl.user_id_from_username(username)

    def get_public_following_list(self, username: str) -> list[str]:
        id = self.get_id_from_username(username)
        following = self.__cl.user_following_v1(id)
        return [users.username for users in following if not (users.is_private)]

    def get_media(self, username: str, amount: int = 0):
        id = self.get_id_from_username(username)
        return self.__cl.user_medias_v1(id, amount)

    def get_detailed_location(self, loc_name, lat, lng):
        place = self.__cl.fbsearch_places(loc_name, lat, lng)[0]
        return self.__cl.location_info_v1(place.pk)
