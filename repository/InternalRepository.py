# from crawler.CrawledData import CrawledData
from repository.DatabaseHandler import DatabaseHandler
from crawler.CrawledData import CrawledData
from crawler.Location import Location

class InternalRepository:

    def __init__(self) -> None:
        self.__db = DatabaseHandler('crawler_test')

    def select_location (self, name: str, lat: float, lng:float):
        name_param = {'name':'loc_name', 'value': {'stringValue': name}}
        lat_param = {'name':'lat', 'value':{'doubleValue': lat}}
        lng_param = {'name':'lng', 'value':{'doubleValue': lng}}
        paramset = [lat_param, lng_param, name_param]
        query = 'select * from location where lat = :lat and lng = :lng and loc_name = :loc_name'
        return self.__db.do_read_query(query, paramset)

    def save_crawled_data (self, data: CrawledData):
        #salva un post nel db
        pass

    def save_location (self, location: Location):
        #salva location nel db
        pass