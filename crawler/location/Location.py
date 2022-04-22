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
        """
        This method checks if the location is a restaurant or any other location related to food (e.g. bar, cafe, etc.).

        :return: True if the location is a restaurant, False otherwise
        """
        restaurant_tags = ['Restaurant', 'Bar', 'Grocery ', 'Wine', 'Diner', 'Food', 'Meal', 'Breakfast', 'Lunch',
                           'Dinner', 'Cafe', 'Tea Room', 'Hotel', 'Pizza', 'Coffee', 'Bakery', 'Dessert', 'Gastropub',
                           'Sandwich', 'Ice Cream', 'Steakhouse']  # da aggiungere se ne troviamo altri
        for tag in restaurant_tags:
            if tag.upper() in self.__category.upper():
                return True
        return False

    def get_location_name(self) -> str:
        """
        Get the name of the location.
        """
        return self.__location_name

    def get_lat(self) -> float:
        """
        Get the latitude of the location.

        :return: float (4 decimal places)
        """
        return self.__lat

    def get_lng(self) -> float:
        """
        Get the longitude of the location.

        :return: float (4 decimal places)
        """
        return self.__lng

    def get_category(self) -> str:
        """
        Get the category of the location.
        """
        return self.__category

    def get_phone(self) -> str:
        """
        Get the phone number of the location.
        """
        return self.__phone

    def get_website(self) -> str:
        """
        Get the website url of the location.
        """
        return self.__website

    def get_db_id(self) -> int:
        """
        Get the id of the location in the db.
        """
        return self.__db_id

    # setters
    def set_db_id(self, db_id) -> None:
        """
        Set the db_id of the location.
        """
        self.__db_id = db_id

    def to_dict(self) -> dict:
        """
        Convert the location object to a dictionary with the following keys:

        - location_name: the name of the location
        - lat: the latitude of the location
        - lng: the longitude of the location
        - category: the category of the location
        - phone: the phone number of the location
        - website: the website url of the location
        - db_id: the id of the restaurant in the database

        :return: a dictionary containing the location's data as explained above
        """
        json_obj = {
            "location_name": self.__location_name,
            "lat": self.__lat,
            "lng": self.__lng,
            "category": self.__category,
            "phone": self.__phone,
            "website": self.__website,
            "db_id": self.__db_id
        }
        return json_obj
