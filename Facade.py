from msilib.schema import Media
from crawler.CrawledData import CrawledData
from crawler.CrawledDataFactory import CrawledDataFactory
from crawler.Crawler import Crawler
from repository.InternalRepository import InternalRepository
from crawler.LocationFactory import LocationFactory
class Facade:
    def __init__(self) -> None:
        self.__crawler = Crawler()
        self.__repository = InternalRepository()
        self.__log_counter = 0

    def __print_media_log(self, message:str):
        print(f'media {self.__log_counter}: {message}')
        self.__log_counter += 1

    
    def __format_media(self, media:Media):
        # in teoria instagrapi capisce la categoria senza lat e lng, per ora escludo
        if media.location is None or media.location.name is None or media.location.lat is None or media.location.lng is None:
            self.__print_media_log('no geotag')
            return
        location_name = media.location.name
        location_lat = round(media.location.lat, 4)
        location_lng = round(media.location.lng, 4)
        location_db = self.__repository.select_location(location_name, location_lat, location_lng)
        if len(location_db) == 1:
            if (location_db[0]['is_restaurant'] == True):
                location = LocationFactory().build_from_db(location_db[0])
                crawled_data = CrawledDataFactory().build_from_media_and_location(media, location)
                self.__print_media_log('location found in db, restaurant!')
            else:
                self.__print_media_log('location found in db, not a restaurant')
                return
        else:
            instagrapi_location = self.__crawler.get_detailed_location(location_name, location_lat, location_lng)
            location = LocationFactory().build_from_instagrapi_location(instagrapi_location)
            
            if location.is_restaurant():
                self.__print_media_log('new location, restaurant!')
            else: self.__print_media_log(f'new location, not a restaurant -> {location.get_category()}')
            # save location in both cases
            
            self.__repository.save_location(location)
            # crawled_data = CrawledDataFactory().build_from_media_and_location(media, location)
    
            # salva nel db

    def start_crawling(self):
        #devo ancora prendere i profili
        self.__crawler.login_from_cookies() #TODO: #2 gestire errori login 
        profiles_for_crawling = ['marco_food_details'] #lorenzolinguini, paolo_vizzari, marco_food_details
        for profile in profiles_for_crawling:
            medias = self.__crawler.get_media(profile, 100) #poi da togliere il 10
            for media in medias:
                self.__format_media(media)