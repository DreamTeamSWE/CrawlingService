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
        #save crawled data in db
        username_param = {'name':'username', 'value': {'stringValue': data.get_username()}}
        post_id_param = {'name':'post_id', 'value': {'stringValue': data.get_post_id()}}
        date_param = {'name':'date', 'value': {'stringValue': data.get_date()}}
        caption_text_param = {'name':'caption_text', 'value': {'stringValue': data.get_caption_text()}}
        id_location_param = {'name':'id_location', 'value': {'longValue': data.get_id_location()}}
        paramset = [username_param, post_id_param, date_param, caption_text_param, id_location_param]
        return self.__db.do_write_query('insert into post (crawler_id, testo, data_pubb, username_autore, id_location) values (:post_id, :caption_text, :date, :username, :id_location)', paramset)

    def save_location (self, location: Location):
        #salva location nel db
        name_param = {'name':'loc_name', 'value': {'stringValue': location.get_location_name()}}
        lat_param = {'name':'lat', 'value':{'doubleValue': location.get_lat()}}
        lng_param = {'name':'lng', 'value':{'doubleValue': location.get_lng()}}
        category_param = {'name':'category', 'value':{'stringValue': location.get_category()}}
        if location.get_phone() is not None:
            phone_param = {'name':'phone', 'value':{'stringValue': location.get_phone()}}
        else: phone_param = {'name':'phone', 'value':{'stringValue': ''}}
        if location.get_website() is not None:
            website_param = {'name':'website', 'value':{'stringValue': location.get_website()}}
        else: website_param = {'name':'website', 'value':{'stringValue': ''}}
        is_restaurant_param = {'name':'is_restaurant', 'value':{'booleanValue': location.is_restaurant()}}
        paramset = [lat_param, lng_param, name_param, category_param, phone_param, website_param, is_restaurant_param]
        return self.__db.do_write_query('insert into location (lat, lng, loc_name, category, phone, website, is_restaurant) values (:lat, :lng, :loc_name, :category, :phone, :website, :is_restaurant)', paramset)