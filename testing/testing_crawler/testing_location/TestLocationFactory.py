import unittest
from instagrapi.types import Location as InstagrapiLocation
from crawler.location.LocationFactory import LocationFactory


class TestLocationFactory(unittest.TestCase):
    def test_build_from_instagrapi_location(self):
        instagrapi_location = InstagrapiLocation(name="test", lat=1.0, lng=1.0, category="category_test",
                                                 phone="phone_test", website="website_test")
        location = LocationFactory.build_from_instagrapi_location(instagrapi_location)
        self.assertEqual(location.get_location_name(), 'test')
        self.assertEqual(location.get_lat(), 1.0)
        self.assertEqual(location.get_lng(), 1.0)
        self.assertEqual(location.get_category(), 'category_test')
        self.assertEqual(location.get_phone(), 'phone_test')
        self.assertEqual(location.get_website(), 'website_test')

    def test_build_from_db(self):
        db_data = {'loc_name': 'test_name', 'lat': '1.0', 'lng': '1.0', 'category': 'test_category',
                   'phone': 'test_phone', 'website': 'test_website', 'id': 'test_id'}
        location = LocationFactory.build_from_db(db_data)
        self.assertEqual(location.get_location_name(), 'test_name')
        self.assertEqual(location.get_lat(), 1.0)
        self.assertEqual(location.get_lng(), 1.0)
        self.assertEqual(location.get_category(), 'test_category')
        self.assertEqual(location.get_phone(), 'test_phone')
        self.assertEqual(location.get_website(), 'test_website')
        self.assertEqual(location.get_db_id(), 'test_id')


if __name__ == '__main__':
    unittest.main()
