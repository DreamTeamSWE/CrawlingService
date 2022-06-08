import unittest
from repository.DatabaseHandler import DatabaseHandler


class TestCrawledData(unittest.TestCase):
    def setUp(self) -> None:
        self.data_base_handelr = DatabaseHandler('crawler_integration')

    def test_select_location(self):
        query = "SELECT * FROM location WHERE id = 1"
        response = self.data_base_handelr.do_read_query(query)
        self.assertEqual(response[0]['lat'], '12.5600')
        self.assertEqual(response[0]['lng'], '14.3000')
        self.assertEqual(response[0]['loc_name'], 'ristorante')
        self.assertEqual(response[0]['category'], 'pizza place')
        self.assertEqual(response[0]['phone'], '1234567890')
        self.assertEqual(response[0]['website'], 'www.website.com')
        self.assertEqual(response[0]['is_restaurant'], True)

    def test_select_profilo_instagram(self):
        query = "SELECT * FROM profilo_instagram WHERE username = 'user'"
        response = self.data_base_handelr.do_read_query(query)
        self.assertEqual(response[0]['username'], 'user')
        self.assertEqual(response[0]['data_ultimo_check'], '2022-01-12 00:00:00')
        self.assertEqual(response[0]['post_utili'], 12)
        self.assertEqual(response[0]['post_visti'], 20)
        self.assertEqual(response[0]['level'], 2)

    def test_select_post(self):
        query = "SELECT * FROM post WHERE id = 1"
        response = self.data_base_handelr.do_read_query(query)
        self.assertEqual(response[0]['crawler_id'], '1')
        self.assertEqual(response[0]['testo'], 'bello')
        self.assertEqual(response[0]['data_pubb'], '2022-01-01')
        self.assertEqual(response[0]['username_autore'], 'user')
        self.assertEqual(response[0]['id_location'], 1)

    def test_select_immagine(self):
        query = "SELECT * FROM immagine WHERE id = 1"
        response = self.data_base_handelr.do_read_query(query)
        self.assertEqual(response[0]['post_id'], 1)


if __name__ == '__main__':
    unittest.main()
