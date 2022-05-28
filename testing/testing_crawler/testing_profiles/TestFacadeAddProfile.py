import unittest
from unittest.mock import patch
from crawler.profiles.FacadeAddProfile import FacadeAddProfile
from crawler.profiles.FacadeAddProfile import AddProfileReturn


class TestFacadeAddProfile(unittest.TestCase):
    def setUp(self) -> None:
        with patch('repository.ProfilesRepository.ProfilesRepository.__init__') as mock_constructor:
            mock_constructor.return_value = None
            self.facade = FacadeAddProfile('profile')

    def test_add_profile_in_db(self):
        with patch('repository.ProfilesRepository.ProfilesRepository.select_profile') as mock_select_profile:
            mock_select_profile.return_value = ['profile']
            self.assertEqual(self.facade.add_profile(), AddProfileReturn.ALREADY_IN_DB)

    def test_add_profile_not_exists(self):
        with patch('repository.ProfilesRepository.ProfilesRepository.select_profile') as mock_select_profile,\
                patch('crawler.Crawler.Crawler.__init__') as mock_constructor,\
                patch('crawler.Crawler.Crawler.login_from_cookies') as mock_login,\
                patch('crawler.Crawler.Crawler.does_profile_exists') as mock_profile_exists:
            mock_constructor.return_value = None
            mock_select_profile.return_value = []
            mock_login.return_value = True
            mock_profile_exists.return_value = False
            self.assertEqual(self.facade.add_profile(), AddProfileReturn.DOES_NOT_EXIST)

    def test_add_profile_private(self):
        with patch('repository.ProfilesRepository.ProfilesRepository.select_profile') as mock_select_profile,\
                patch('crawler.Crawler.Crawler.__init__') as mock_constructor,\
                patch('crawler.Crawler.Crawler.login_from_cookies') as mock_login,\
                patch('crawler.Crawler.Crawler.does_profile_exists') as mock_profile_exists,\
                patch('crawler.Crawler.Crawler.is_profile_private') as mock_is_private:
            mock_constructor.return_value = None
            mock_select_profile.return_value = []
            mock_login.return_value = True
            mock_profile_exists.return_value = True
            mock_is_private.return_value = True
            self.assertEqual(self.facade.add_profile(), AddProfileReturn.PRIVATE_PROFILE)

    def test_add_profile_success(self):
        with patch('repository.ProfilesRepository.ProfilesRepository.select_profile') as mock_select_profile,\
                patch('crawler.Crawler.Crawler.__init__') as mock_constructor,\
                patch('crawler.Crawler.Crawler.login_from_cookies') as mock_login,\
                patch('crawler.Crawler.Crawler.does_profile_exists') as mock_profile_exists,\
                patch('crawler.Crawler.Crawler.is_profile_private') as mock_is_private,\
                patch('repository.ProfilesRepository.ProfilesRepository.insert_profile') as mock_insert_profile:
            mock_constructor.return_value = None
            mock_select_profile.return_value = []
            mock_login.return_value = True
            mock_profile_exists.return_value = True
            mock_is_private.return_value = False
            self.assertEqual(self.facade.add_profile(), AddProfileReturn.SUCCESS)


if __name__ == '__main__':
    unittest.main()
