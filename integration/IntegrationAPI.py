import unittest
import requests


class TestCrawledData(unittest.TestCase):
    def test_get_ranking(self):
        endpoint = 'https://eultdbw3g5.execute-api.eu-central-1.amazonaws.com/dev/test_post'
        params = {'name': 'lorenzolinguini'}
        response = requests.post(endpoint, json=params)
        self.assertEqual(response.status_code, 200)

        self.assertIn('message', response.json())
        self.assertIn('status', response.json())


if __name__ == '__main__':
    unittest.main()