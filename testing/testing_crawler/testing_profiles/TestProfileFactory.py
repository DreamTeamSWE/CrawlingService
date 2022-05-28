import unittest
from datetime import datetime
from crawler.profiles.ProfileFactory import ProfileFactory


class TestLocationFactory(unittest.TestCase):
    def test_build_from_db(self):
        db_data = {'username': 'username', 'data_ultimo_check': None, 'post_visti': 0, 'post_utili': 0}
        profile = ProfileFactory.build_from_db(db_data)
        self.assertEqual(profile.get_username(), db_data['username'])
        self.assertEqual(profile.get_last_time_checked(), db_data['data_ultimo_check'])
        self.assertEqual(profile.get_viewed_posts(), db_data['post_visti'])
        self.assertEqual(profile.get_usefull_posts(), db_data['post_utili'])

        db_data = {'username': 'username', 'post_visti': 0, 'post_utili': 0,
                   'data_ultimo_check': '2019-01-01 00:00:00'}
        profile = ProfileFactory.build_from_db(db_data)
        self.assertEqual(profile.get_username(), db_data['username'])
        self.assertEqual(profile.get_last_time_checked(), datetime(2019, 1, 1, 0, 0))
        self.assertEqual(profile.get_viewed_posts(), db_data['post_visti'])
        self.assertEqual(profile.get_usefull_posts(), db_data['post_utili'])


if __name__ == '__main__':
    unittest.main()
