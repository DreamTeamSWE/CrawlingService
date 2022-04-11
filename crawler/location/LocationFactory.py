from crawler.location.Location import Location
from instagrapi.types import Location as InstagrapiLocation


class LocationFactory:

    @staticmethod
    def build_from_instagrapi_location(location: InstagrapiLocation):
        """
        Builds a Location object from an Instagrapi.Location object

        :param location: an instagrapi.types.Location object
        :return: a Location object corresponding to the given instagrapi.types.Location object
        """
        return Location(location.name, location.lat, location.lng, location.category, location.phone, location.website)

    @staticmethod
    def build_from_db(db_data: dict):
        """
        Builds a Location object from a dictionary containing the data from the database obtained by a query like:
        'SELECT * FROM locations WHERE id = ?'.

        :param db_data: a dictionary containing the data from the database
        :return: a Location object corresponding to the given dictionary
        """
        return Location(db_data['loc_name'], float(db_data['lat']), float(db_data['lng']), db_data['category'],
                        db_data['phone'], db_data['website'], db_data['id'])
