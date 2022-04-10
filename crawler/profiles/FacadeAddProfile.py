from repository.ProfilesRepository import ProfilesRepository
from crawler.Crawler import Crawler
import logging


class FacadeAddProfile:

    def __init__(self, profile: str):
        self.__profile = profile
        self.__repository = ProfilesRepository()

    def add_profile(self) -> int:

        """
              add profile to the database

              Returns
              -------
              int
                    0 if the profile was added successfully
                    1 if the profile is already in the database
                    2 if the profile does not exist
                    3 if the profile is private
        """

        # check if the profile is already in the database
        if len(self.__repository.select_profile(self.__profile)) != 0:
            logging.info("Profile already in database")
            return 1

        # check if exists
        crawler = Crawler()
        crawler.login_from_cookies()
        if crawler.does_profile_exists(self.__profile) is False:
            logging.info("Profile does not exist")
            return 2

        # check if private
        if crawler.is_profile_private(self.__profile):
            logging.info("Profile is private")
            return 3

        # add the profile to the database
        self.__repository.insert_profile(self.__profile)
        logging.info(f'Profile {self.__profile} added to the database')

        # add all the followings of the profile
        followings = crawler.get_public_following_list(self.__profile)
        self.__repository.insert_profiles_list(followings)
        logging.info(f'Followings of {self.__profile} added to the database')

        return 0
