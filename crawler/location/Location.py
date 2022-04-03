import json


class Location:
    def __init__(self, location_name, lat, lng, category, phone, website, db_id=None) -> None:
        self.__location_name = location_name  # nome della location del post
        self.__lat = round(lat, 4)  # latitudine della location del post
        self.__lng = round(lng, 4)  # longitudine della location del post
        self.__category = category  # categoria della location
        self.__phone = phone  # numero di telefono della location
        self.__website = website  # sito web della location
        self.__db_id = db_id  # id della location nel db

    def is_restaurant(self) -> bool:
        restaurant_tags = ['Restaurant', 'Bar', 'Grocery ', 'Wine', 'Diner', 'Food', 'Meal', 'Breakfast', 'Lunch',
                           'Dinner', 'Cafe', 'Tea Room', 'Hotel']  # da aggiungere se ne troviamo altri
        for tag in restaurant_tags:
            if tag in self.__category:
                return True
        return False

    def get_location_name(self) -> str:
        return self.__location_name

    def get_lat(self) -> float:
        return self.__lat

    def get_lng(self) -> float:
        return self.__lng

    def get_category(self) -> str:
        return self.__category

    def get_phone(self) -> str:
        return self.__phone

    def get_website(self) -> str:
        return self.__website

    def get_db_id(self) -> int:
        return self.__db_id

    #setters
    def set_db_id(self, db_id) -> None:
        self.__db_id = db_id
    

    def to_dict(self) -> str:
        json_obj = {
            "location_name": self.__location_name,
            "lat": self.__lat,
            "lng": self.__lng,
            "category": self.__category,
            "phone": self.__phone,
            "website": self.__website
        }
        return json_obj
