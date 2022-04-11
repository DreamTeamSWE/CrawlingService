from instagrapi import Client
from instagrapi.types import Media
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
    def __emulate_human_behaviour() -> None:
        """
        Emulate human behaviour by sleeping for random time between 5 and 15 seconds.
        """
        x = random.uniform(5, 15)
        logging.info(f'emulating human behaviour: waiting {round(x, 1)} seconds...')
        time.sleep(x)

    def login_from_account(self, username: str, password: str) -> None:
        """
        Login the client to instagram using username and password.

        :param username: username of the account
        :param password: password of the account

        :raise: instagrapi.exceptions.ClientError if something went wrong during login
        """
        try:
            logging.info("login in progress...")
            self.__cl.login(username, password)
            logging.info("login crawler successful!!")
        except instagrapi.exceptions.ClientError:
            logging.info('an error occoured during log in')

    def save_cookies(self) -> None:
        """
        Save the cookies of the client in a local json file called cookies.json.
        """
        json.dump(self.__cl.get_settings(), open('cookie.json', 'w'))

    def login_from_cookies(self) -> None:
        """
        Login the client to instagram using the cookies saved in a file stored in s3.
        """
        logging.info('login from cookies...')
        s3 = boto3.client(service_name='s3')
        content_object = s3.get_object(Bucket='sweeat-crawler-cookies', Key='instaswe2021.txt')
        file_content = content_object['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        self.__cl = Client(json_content)
        logging.info('login successful!')

    def get_id_from_username(self, username: str) -> str:
        """
        Get the instagram id of a user by username.

        :return: the instagram id of the user with the given username
        """
        return self.__cl.user_id_from_username(username)

    def get_media(self, username: str, amount: int = 0) -> List[Media]:
        """
        Get a user's media by Private Mobile API.

        :param username: username of the user to get the media from
        :param amount: amount of media to get, 0 means all
        :return: a list of objects of Media
        """
        logging.info(f'scraping {amount} medias from {username}...')
        user_instagrapi_id = self.get_id_from_username(username)
        media = self.__cl.user_medias_v1(int(user_instagrapi_id), amount)
        logging.info('medias scraped successfully!')
        return media

    def get_detailed_location(self, loc_name, lat, lng):
        """
        Get more information like website, phone number, etc. of a location. Can return None if the location is not
        found.

        :param loc_name: name of the location
        :param lat: latitude of the location
        :param lng: longitude of the location
        :return: an instagrapi.types.Location object if the location is found, None otherwise
        """
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
            # TODO: evitare di ritornare None e lanciare un'eccezione, aggiorna documentazione di conseguenza
            return None

    def does_profile_exists(self, username: str) -> bool:
        """
        Check if a profile corresponding to the given username exists.

        :param username: username of the profile to check
        :return: True if the profile exists, False otherwise
        """
        try:
            self.get_id_from_username(username)
            return True
        except instagrapi.exceptions.UserNotFound:
            return False

    def is_profile_private(self, username: str) -> bool:
        """
        Check if a profile corresponding to the given username is private.

        :param username: username of the profile to check
        :return: True if the profile is private, False otherwise
        """
        user_instagrapi = self.__cl.user_info_by_username(username)
        return user_instagrapi.is_private

    def get_public_following_list(self, username: str) -> List[str]:
        """
        Get the list of public following of a profile.

        :param username: username of the profile to get the public following list from
        :return: a list of usernames of the public following of the profile
        """
        user_instagrapi_id = self.get_id_from_username(username)
        following = self.__cl.user_following_v1(user_instagrapi_id)
        return [users.username for users in following if not users.is_private]
