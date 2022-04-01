class Location:
    def __init__(self, locationName, lat, lng, category, phone, website) -> None:
        self.__locationName = locationName  # nome della location del post
        self.__lat = lat  # latitudine della location del post
        self.__lng = lng  # longitudine della location del post
        self.__category = category #categoria della location
        self.__phone = phone #numero di telefono della location
        self.__website = website #sito web della location
    def is_restaurant(self) -> bool:
        resaurant_tags = ['Restaurant', 'Bar', 'Grocery ', 'Wine'] #da aggiungere se ne troviamo altri
        for tag in resaurant_tags:
            if tag in self.__category: return True
        return False