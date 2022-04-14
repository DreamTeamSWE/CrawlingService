import unittest
from crawler.profiles.ProfileForCrawling import ProfileForCrawling
from datetime import datetime


class TestProfileForCrawling(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = ProfileForCrawling('username', '2022-12-15 11:23:35', 234, 12)
        self.profile2 = ProfileForCrawling('username2', '2022-12-15 11:23:35', 234, 0)
        self.profile3 = ProfileForCrawling('username3', '2022-12-15 11:23:35', 13, 0)

    def test_get_username(self):
        self.assertEqual(self.profile.get_username(), 'username')

    def test_get_last_time_checked(self):
        self.assertEqual(self.profile.get_last_time_checked(), datetime.strptime('2022-12-15 11:23:35', '%Y-%m-%d %H:%M:%S'))

    def test_get_viewed_posts(self):
        self.assertEqual(self.profile.get_viewed_posts(), 234)

    def test_get_usefull_posts(self):
        self.assertEqual(self.profile.get_usefull_posts(), 12)

    def test_set_last_time_checked(self):
        self.profile.set_last_time_checked('2021-12-05 11:33:05')
        self.assertEqual(self.profile.get_last_time_checked(), datetime.strptime('2021-12-05 11:33:05', '%Y-%m-%d %H:%M:%S'))

    def test_set_viewed_posts(self):
        self.profile.set_viewed_posts(123)
        self.assertEqual(self.profile.get_viewed_posts(), 123)

    def test_set_usefull_posts(self):
        self.profile.set_usefull_posts(123)
        self.assertEqual(self.profile.get_usefull_posts(), 123)

    def test_is_crawable(self):
        self.assertTrue(self.profile.is_crawable())
        self.assertFalse(self.profile2.is_crawable())
        self.assertTrue(self.profile3.is_crawable())

    def test_add_not_usefull_post(self):
        self.profile.add_not_usefull_post()
        self.assertEqual(self.profile.get_viewed_posts(), 235)
        self.assertEqual(self.profile.get_usefull_posts(), 12)

    def test_add_usefull_post(self):
        self.profile.add_usefull_post()
        self.assertEqual(self.profile.get_viewed_posts(), 235)
        self.assertEqual(self.profile.get_usefull_posts(), 13)


if __name__ == '__main__':
    unittest.main()
