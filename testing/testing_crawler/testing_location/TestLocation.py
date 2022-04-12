import unittest
from crawler.location.Location import Location


class TestLocation(unittest.TestCase):
    def setUp(self) -> None:
        self.location = Location('location_name', 43.3, 12.2134, 'fast food', '1234567890', 'http://www.google.com', 1)
        self.location2 = Location('location_name', 43.3, 12.2134, 'City', '1234567890', 'http://www.google.com', 1)

    def test_location_is_restaurant(self):
        self.assertTrue(self.location.is_restaurant())
        self.assertFalse(self.location2.is_restaurant())

    def test_get_location_name(self):
        self.assertEqual(self.location.get_location_name(), 'location_name')

    def test_get_lat(self):
        self.assertEqual(self.location.get_lat(), 43.3)

    def test_get_lng(self):
        self.assertEqual(self.location.get_lng(), 12.2134)

    def test_get_category(self):
        self.assertEqual(self.location.get_category(), 'fast food')

    def test_get_phone(self):
        self.assertEqual(self.location.get_phone(), '1234567890')

    def test_get_website(self):
        self.assertEqual(self.location.get_website(), 'http://www.google.com')

    def test_get_db_id(self):
        self.assertEqual(self.location.get_db_id(), 1)

    def test_set_db_id(self):
        self.location.set_db_id(2)
        self.assertEqual(self.location.get_db_id(), 2)

    def test_to_dict(self):
        self.assertEqual(self.location.to_dict(), {'location_name': 'location_name', 'lat': 43.3, 'lng': 12.2134, 'category': 'fast food', 'phone': '1234567890', 'website': 'http://www.google.com'})


if __name__ == '__main__':
    unittest.main()
