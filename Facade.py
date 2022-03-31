from Crawler import Crawler
from InternalRepository import InternalRepository

class Facade:
    def start_crawling():
        profiles_for_crawling = []
        crawler = Crawler()
        repository = InternalRepository()
        for profile in profiles_for_crawling:
            medias = crawler.get_media(profile)
            for media in medias:
                # analisi location
                location_name = media.location.name
                location_lat = media.location.lat
                location_lng = media.location.lng
                location_db = repository.select_location(location_name, location_lat, location_lng)
                if location_db is None:
                    #uso il crawler e poi salvo la location
                    pass
                if location_db['isRestaurant'] is True:
                    pass
                    #va salvato e segnalato al servizio
                else: 
                    pass
                    #termino
            
                # factory per i media
                # salva nel db