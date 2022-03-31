from crawler.CrawledData import CrawledData
from crawler.Location import Location

class InternalRepository:
    def select_location (self, name, lat, lng):
        #cerca nel db location e ritorna la tupla o None
        pass

    def save_crawled_data (self, data: CrawledData):
        #salva un post nel db
        pass

    def save_location (self, location: Location):
        #salva location nel db
        pass