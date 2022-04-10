# from crawler.CrawledData import CrawledData
from repository.DatabaseHandler import DatabaseHandler
from crawler.crawled_data.CrawledData import CrawledData
from crawler.location.Location import Location
import requests
import boto3
import logging


class InternalRepository:

    def __init__(self) -> None:
        self.__db = DatabaseHandler('crawler_test')

    @staticmethod
    def __save_img_s3(img_url: str, id_img: int):
        source_bytes = requests.get(img_url).content
        s3 = boto3.client('s3')
        s3.put_object(Body=source_bytes, Bucket='dream-team-img-test',
                      Key=str(id_img) + '.jpg',
                      ContentType='image/jpg')

    def select_location(self, name: str, lat: float, lng: float):
        name_param = {'name': 'loc_name', 'value': {'stringValue': name}}
        lat_param = {'name': 'lat', 'value': {'doubleValue': lat}}
        lng_param = {'name': 'lng', 'value': {'doubleValue': lng}}
        paramset = [lat_param, lng_param, name_param]
        query = 'select * from location where lat = :lat and lng = :lng and loc_name = :loc_name'
        return self.__db.do_read_query(query, paramset)

    def check_if_post_already_saved(self, crawler_id: str) -> bool:
        crawler_id_param = {'name': 'crawler_id', 'value': {'stringValue': crawler_id}}
        paramset = [crawler_id_param]
        query = 'select * from post where crawler_id = :crawler_id'
        response = self.__db.do_read_query(query, paramset)
        return len(response) == 1

    def save_crawled_data(self, data: CrawledData) -> int:
        # PRE: location e profilo già salvati nel db
        # salva crawled data nel db
        if self.check_if_post_already_saved(data.get_post_id()):
            logging.info('warning: you are scraping a post that is already saved, skipping')
            return -1
        username_param = {'name': 'username', 'value': {'stringValue': data.get_username()}}
        post_id_param = {'name': 'post_id', 'value': {'stringValue': data.get_post_id()}}
        date_param = {'name': 'date', 'value': {'stringValue': data.get_date()}, 'typeHint': 'TIMESTAMP'}
        caption_text_param = {'name': 'caption_text', 'value': {'stringValue': data.get_caption_text()}}
        id_location_param = {'name': 'id_location', 'value': {'longValue': data.get_id_location()}}
        paramset = [username_param, post_id_param, date_param, caption_text_param, id_location_param]
        response = self.__db.do_write_query(
            'insert into post (crawler_id, testo, data_pubb, username_autore, id_location) values (:post_id, :caption_text, :date, :username, :id_location)',
            paramset)
        db_id = response['generatedFields'][0]['longValue']

        # salvo le foto
        for img_url in data.get_img_url():
            db_id_param = {'name': 'id_post', 'value': {'longValue': db_id}}
            response = self.__db.do_write_query('insert into immagine (post_id) values (:id_post)', [db_id_param])
            id_photo = response['generatedFields'][0]['longValue']
            self.__save_img_s3(img_url, id_photo)
            data.add_s3_id(id_photo)

        return 0

    def save_location(self, location: Location):
        # salva location nel db
        name_param = {'name': 'loc_name', 'value': {'stringValue': location.get_location_name()}}
        lat_param = {'name': 'lat', 'value': {'doubleValue': location.get_lat()}}
        lng_param = {'name': 'lng', 'value': {'doubleValue': location.get_lng()}}
        category_param = {'name': 'category', 'value': {'stringValue': location.get_category()}}
        if location.get_phone() is not None:
            phone_param = {'name': 'phone', 'value': {'stringValue': location.get_phone()}}
        else:
            phone_param = {'name': 'phone', 'value': {'stringValue': ''}}
        if location.get_website() is not None:
            website_param = {'name': 'website', 'value': {'stringValue': location.get_website()}}
        else:
            website_param = {'name': 'website', 'value': {'stringValue': ''}}
        is_restaurant_param = {'name': 'is_restaurant', 'value': {'booleanValue': location.is_restaurant()}}
        paramset = [lat_param, lng_param, name_param, category_param, phone_param, website_param, is_restaurant_param]
        return self.__db.do_write_query(
            'insert into location (lat, lng, loc_name, category, phone, website, is_restaurant) values (:lat, :lng, :loc_name, :category, :phone, :website, :is_restaurant)',
            paramset)
