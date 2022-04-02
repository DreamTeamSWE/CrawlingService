import json


class Location:
    def __init__(self, locationName, lat, lng, category, phone, website) -> None:
        self.__location_name = locationName  # nome della location del post
        self.__lat = round(lat, 4)  # latitudine della location del post
        self.__lng = round(lng, 4)  # longitudine della location del post
        self.__category = category #categoria della location
        self.__phone = phone #numero di telefono della location
        self.__website = website #sito web della location

    def is_restaurant(self) -> bool:
        resaurant_tags = ['Restaurant', 'Bar', 'Grocery ', 'Wine', 'Diner', 'Food', 'Meal', 'Breakfast', 'Lunch', 'Dinner', 'Cafe'] #da aggiungere se ne troviamo altri
        for tag in resaurant_tags:
            if tag in self.__category: return True
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
    


    def to_json(self) -> str:
        json_obj = {
            "locationName": self.__locationName,
            "lat": self.__lat,
            "lng": self.__lng,
            "category": self.__category,
            "phone": self.__phone,
            "website": self.__website
        }
        return json.dumps(json_obj)
