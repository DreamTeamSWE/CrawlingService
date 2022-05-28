import unittest
from unittest.mock import patch
from crawler.Crawler import Crawler
import instagrapi.exceptions
from instagrapi.types import User, Location


class TestFacadeAddProfile(unittest.TestCase):
    def setUp(self) -> None:
        with patch('instagrapi.Client.__init__') as mock_constructor:
            mock_constructor.return_value = None
            self.crawler = Crawler()

    def test_login_from_account_error(self):
        with patch('instagrapi.Client.login') as mock_login:
            mock_login.side_effect = instagrapi.exceptions.ClientError('Error')
            self.crawler.login_from_account('username', 'password')

    def test_login_from_account_success(self):
        with patch('instagrapi.Client.login') as mock_login:
            mock_login.return_value = None
            self.crawler.login_from_account('username', 'password')

    def test_save_cookies(self):
        with patch('instagrapi.Client.get_settings') as mock_save_cookies, \
                patch('json.dump') as mock_json_dump, \
                patch('builtins.open') as mock_open:
            mock_save_cookies.return_value = {'cookies': 'cookies'}
            mock_json_dump.return_value = None
            mock_open.return_value = None
            self.crawler.save_cookies()

    def test_get_media(self):
        with patch('crawler.Crawler.Crawler.get_id_from_username') as mock_get_id_from_username, \
                patch('instagrapi.Client.user_medias_v1') as mock_user_medias_v1:
            mock_get_id_from_username.return_value = 4213
            mock_user_medias_v1.return_value = 'media'
            self.assertEqual(self.crawler.get_media('username'), 'media')

    def test_does_profile_exists_true(self):
        with patch('crawler.Crawler.Crawler.get_id_from_username') as mock_get_id_from_username:
            mock_get_id_from_username.return_value = 4213
            self.assertTrue(self.crawler.does_profile_exists('username'))

    def test_does_profile_exists_false(self):
        with patch('crawler.Crawler.Crawler.get_id_from_username') as mock_get_id_from_username:
            mock_get_id_from_username.side_effect = instagrapi.exceptions.UserNotFound('Error')
            self.assertFalse(self.crawler.does_profile_exists('username'))

    def test_is_profile_private_true(self):
        with patch('instagrapi.Client.user_info_by_username') as mock_user_info:
            mock_user_info.return_value = User(is_private=True, username='username', full_name='full_name', pk='pk',
                                               profile_pic_url='http://profile_pic_url.png', is_verified=False,
                                               media_count=1, follower_count=1, following_count=1, is_business=False)
            self.assertTrue(self.crawler.is_profile_private('username'))

    def test_get_detailed_location_none(self):
        with patch('instagrapi.Client.fbsearch_places') as mock_fbsearch_places, \
                patch('time.sleep') as mock_sleep:
            mock_fbsearch_places.return_value = []
            mock_sleep.return_value = None
            self.assertEqual(self.crawler.get_detailed_location('location', 1, 1), None)

    def test_get_detailed_location_not_none(self):
        with patch('instagrapi.Client.fbsearch_places') as mock_fbsearch_places, \
                patch('time.sleep') as mock_sleep, \
                patch('instagrapi.Client.location_info_v1') as mock_location_info:
            mock_fbsearch_places.return_value = [Location(name='name', id='id', latitude='latitude', pk=1234)]
            mock_sleep.return_value = None
            mock_location_info.return_value = Location(name='name', id='id', latitude='latitude')
            location = self.crawler.get_detailed_location('name', 1, 1)
            self.assertEqual(location.name, 'name')
            self.assertEqual(location.lat, 1)
            self.assertEqual(location.lng, 1)

    def test_get_id_from_username(self):
        with patch('instagrapi.Client.user_id_from_username') as mock_user_id_from_username:
            mock_user_id_from_username.return_value = 'id'
            self.assertEqual(self.crawler.get_id_from_username('username'), 'id')

    def test_get_public_following_list(self):
        with patch('crawler.Crawler.Crawler.get_id_from_username') as mock_get_id_from_username, \
                patch('instagrapi.Client.user_following_v1') as mock_user_following_v2:
            mock_get_id_from_username.return_value = 'id'
            mock_user_following_v2.return_value = [User(username='username', full_name='full_name', pk='pk',
                                                        profile_pic_url='http://profile_pic_url.png',
                                                        is_verified=False, media_count=1, follower_count=1,
                                                        following_count=1, is_business=False, is_private=False)]
            self.assertEqual(self.crawler.get_public_following_list('id'), ['username'])

    # def test_login_from_cookies(self):
    #     with patch('boto3.client.__init__') as mock_boto3_client, \
    #             patch('boto3.client.get_object') as mock_get_object, \
    #             patch('builtins.read') as mock_read, \
    #             patch('builtins.decode') as mock_decode, \
    #             patch('json.loads') as mock_loads, \
    #             patch('instagrapi.Client.__init__') as mock_instagrapi_client:
    #         mock_boto3_client.return_value = None
    #         mock_get_object.return_value = {'Body': '{"username": "username", "password": "password"}'}
    #         mock_read.return_value = 'username'
    #         mock_decode.return_value = 'username'
    #         mock_loads.return_value = {'username': 'username', 'password': 'password'}
    #         mock_instagrapi_client.return_value = None
    #         self.crawler.login_from_cookies()


if __name__ == '__main__':
    unittest.main()
