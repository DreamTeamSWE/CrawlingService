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

    
    def __format_media(self, media:Media):
        # analisi location
        location_name = media.location.name
        location_lat = media.location.lat
        location_lng = media.location.lng
        location_db = self.__repository.select_location(location_name, location_lat, location_lng)
        if len(location_db) == 1:
            if (location_db['is_restaurant'] == True):
                location = LocationFactory().build_from_db(location_db)
                crawled_data = CrawledDataFactory().build_from_media_and_location(media, location)
            else:
                print ('log info')
                return
        else:
            instagrapi_location = self.__crawler.get_detailed_location(location_name, location_lat, location_lng)
            location = LocationFactory().build_from_instagrapi_location(instagrapi_location)
            if location.is_restaurant():
                pass
            else: pass
            # save location in both cases
            crawled_data = CrawledDataFactory().build_from_media_and_location(media, location)
    
            # salva nel db
    def start_crawling(self):
        #devo ancora prendere i profili
        profiles_for_crawling = []
        for profile in profiles_for_crawling:
            medias = self.__crawler.get_media(profile)
            for media in medias:
                self.__format_media(media)