from http import client
from instagrapi import Client
from instagrapi.exceptions import (ClientError)
import json

class Crawler:

    def __init__(self) -> None:
        self.__cl = Client()

    def login_from_account (self, username: str, password: str):
        try:
            print("Login in progress...")
            self.__cl.login(username, password)
            print("Login crawler Successful!!")
        except (ClientError):
            print('an error occoured during log in')

    def save_cookies (self):
        json.dump(self.__cl.get_settings(), open('cookie.json', 'w'))

    def login_from_cookies (self):
        self.__cl = Client(json.load(open('cookie.json')))

    def get_id_from_username (self, username: str):
        return self.__cl.user_id_from_username(username)

    def get_public_following_list (self, username: str) -> list[str]:
        id = self.get_id_from_username(username)
        following = self.__cl.user_following_v1(id)
        following_list = []
        for users in following:
            if not (users.is_private):
                following_list.append(users.username)
        return following_list

    def get_media (self, username: str, amount: int = 0):
        id = self.get_id_from_username(username)
        medias = self.__cl.user_medias_v1(id, amount)
        return medias
