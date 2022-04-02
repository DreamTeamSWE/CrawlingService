from crawler.Location import Location
from instagrapi.types import Location as InstagrapiLocation
class LocationFactory:

    def build_from_instagrapi_location(self, location: InstagrapiLocation):
        return Location (location.name, location.lat, location.lng, location.category, location.phone, location.website)

    def build_from_db(self, db_data: dict):
        return Location(db_data['loc_name'], float(db_data['lat']), float(db_data['lng']), db_data['category'], db_data['phone'], db_data['website'])