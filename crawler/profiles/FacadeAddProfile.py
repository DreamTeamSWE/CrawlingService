from repository.ProfilesRepository import ProfilesRepository
from crawler.Crawler import Crawler
import logging
from enum import Enum


# enums for returns
class AddProfileReturn(Enum):
    SUCCESS = 0
    ALREADY_IN_DB = 1
    DOES_NOT_EXIST = 2
    PRIVATE_PROFILE = 3


class FacadeAddProfile:
    def __init__(self, profile: str):
        self.__profile = profile
        self.__repository = ProfilesRepository()

    def add_profile(self) -> AddProfileReturn:
        """
        Try to add the profile to the database.
        There are four possible returns:

        - SUCCESS: The profile was added to the database.
        - ALREADY_IN_DB: The profile is already in the database.
        - DOES_NOT_EXIST: The profile does not exist.
        - PRIVATE_PROFILE: The profile is private.

        :return: An object of AddProfileReturn enum corresponding to the result of the operation.
        """
        # check if the profile is already in the database
        if len(self.__repository.select_profile(self.__profile)) != 0:
            logging.info("Profile already in database")
            return AddProfileReturn.ALREADY_IN_DB

        # check if exists
        crawler = Crawler()
        crawler.login_from_cookies()
        if crawler.does_profile_exists(self.__profile) is False:
            logging.info("Profile does not exist")
            return AddProfileReturn.DOES_NOT_EXIST

        # check if private
        if crawler.is_profile_private(self.__profile):
            logging.info("Profile is private")
            return AddProfileReturn.PRIVATE_PROFILE

        # add the profile to the database
        self.__repository.insert_profile(self.__profile)
        logging.info(f'Profile {self.__profile} added to the database')

        # add all the followings of the profile
        # followings = crawler.get_public_following_list(self.__profile)
        # self.__repository.insert_profiles_list(followings)
        # logging.info(f'Followings of {self.__profile} added to the database')

        return AddProfileReturn.SUCCESS
