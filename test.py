import unittest
from crawler.location.Location import Location


class TestLocation(unittest.TestCase):
    def test_location_is_restaurant(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        location2 = Location('location_name', 43.3, 12.2134, 'City', '1234567890', 'http://www.google.com')
        self.assertTrue(location.is_restaurant())
        self.assertFalse(location2.is_restaurant())

    def test_get_location_name(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_location_name(), 'location_name')

    def test_get_lat(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_lat(), 43.3)

    def test_get_lng(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_lng(), 12.2134)

    def test_get_category(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_category(), 'Italian Restaurant')

    def test_get_phone(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_phone(), '1234567890')

    def test_get_website(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.get_website(), 'http://www.google.com')

    def test_get_db_id(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com', 1)
        self.assertEqual(location.get_db_id(), 1)

    def test_set_db_id(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        location.set_db_id(1)
        self.assertEqual(location.get_db_id(), 1)

    def test_to_dict(self):
        location = Location('location_name', 43.3, 12.2134, 'Italian Restaurant', '1234567890', 'http://www.google.com')
        self.assertEqual(location.to_dict(), {'location_name': 'location_name', 'lat': 43.3, 'lng': 12.2134, 'category': 'Italian Restaurant', 'phone': '1234567890', 'website': 'http://www.google.com'})


if __name__ == '__main__':
    unittest.main()
