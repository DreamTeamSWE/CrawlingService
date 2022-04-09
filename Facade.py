from instagrapi.types import Media
from crawler.crawled_data.CrawledDataFactory import CrawledDataFactory
from crawler.Crawler import Crawler
from crawler.location.LocationFactory import LocationFactory
from repository.InternalRepository import InternalRepository
from repository.ProfilesRepository import ProfilesRepository
from repository.SQSHandler import SQSHandler
from crawler.profiles.ProfileFactory import ProfileFactory
from crawler.profiles.ProfileForCrawling import ProfileForCrawling
from datetime import datetime


class Facade:
    def __init__(self) -> None:
        self.__crawler = Crawler()
        self.__repository = InternalRepository()
        self.__profile_repository = ProfilesRepository()
        self.__log_counter = 0

    @staticmethod
    def __get_amount_to_crawl(profile: ProfileForCrawling):
        if profile.get_last_time_checked() is None:
            return 48
        last_check = profile.get_last_time_checked()
        today = datetime.now()
        diff = (today - last_check).days
        if diff >= 48:
            return 48
        else:
            return diff + 1

    def __print_media_log(self, message: str):
        print(f'media {self.__log_counter}: {message}')
        self.__log_counter += 1

    def __format_media(self, media: Media):
        is_restaurant = False
        # in teoria instagrapi capisce la categoria senza lat e lng, per ora escludo
        if media.location is None or media.location.name is None or media.location.lat is None or media.location.lng is None:
            self.__print_media_log('no geotag')
            return
        location_name = media.location.name
        location_lat = round(media.location.lat, 4)
        location_lng = round(media.location.lng, 4)
        location_db = self.__repository.select_location(location_name, location_lat, location_lng)
        if len(location_db) == 1:
            if location_db[0]['is_restaurant'] is True:
                location = LocationFactory().build_from_db(location_db[0])
                is_restaurant = True
                self.__print_media_log('location found in db, restaurant!')
            else:
                self.__print_media_log('location found in db, not a restaurant')
                return
        else:
            instagrapi_location = self.__crawler.get_detailed_location(location_name, location_lat, location_lng)
            if instagrapi_location is None:
                self.__print_media_log('fbsearch cannot find location')
                return
            location = LocationFactory().build_from_instagrapi_location(instagrapi_location)

            if location.is_restaurant():
                self.__print_media_log('new location, restaurant!')
                is_restaurant = True
            else:
                self.__print_media_log(f'new location, not a restaurant -> {location.get_category()}')

            # save location in both cases
            response = self.__repository.save_location(location)
            location.set_db_id(response['generatedFields'][0]['longValue'])

        # save media
        if is_restaurant is True:
            crawled_data = CrawledDataFactory().build_from_media_and_location(media, location)
            status = self.__repository.save_crawled_data(crawled_data)
            # enqueue crawled data
            if status == 0:
                sqs = SQSHandler('coda-crawler.fifo')
                sqs.enqueue_message(crawled_data)

    def start_crawling(self):
        self.__crawler.login_from_cookies()  # TODO: #2 gestire errori login
        profile_for_crawling = ProfileFactory().build_from_db(self.__profile_repository.get_profile_for_crawling_level_1()[0])
        medias = self.__crawler.get_media(profile_for_crawling.get_username(), self.__get_amount_to_crawl(profile_for_crawling))
        for media in medias:
            self.__format_media(media)
