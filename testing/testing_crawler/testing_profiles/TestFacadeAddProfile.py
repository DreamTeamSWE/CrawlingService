import unittest
from unittest.mock import patch
from crawler.profiles.FacadeAddProfile import FacadeAddProfile
from crawler.profiles.FacadeAddProfile import AddProfileReturn


class TestFacadeAddProfile(unittest.TestCase):
    def setUp(self) -> None:
        self.facade = FacadeAddProfile('profile')

    def test_add_profile(self):
        with patch('repository.ProfilesRepository.ProfilesRepository.select_profile') as mock_select_profile:
            mock_select_profile.return_value = [1, 1, 1]
            self.assertEqual(self.facade.add_profile(), AddProfileReturn.ALREADY_IN_DB)


if __name__ == '__main__':
    unittest.main()
