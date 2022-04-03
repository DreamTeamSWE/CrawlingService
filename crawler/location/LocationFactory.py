from crawler.location.Location import Location
from instagrapi.types import Location as InstagrapiLocation


class LocationFactory:

    @staticmethod
    def build_from_instagrapi_location(location: InstagrapiLocation):
        return Location(location.name, location.lat, location.lng, location.category, location.phone, location.website)

    @staticmethod
    def build_from_db(db_data: dict):
        return Location(db_data['loc_name'], float(db_data['lat']), float(db_data['lng']), db_data['category'],
                        db_data['phone'], db_data['website'], db_data['id'])
