import unittest

import requests
from requests.exceptions import Timeout
from unittest.mock import Mock

requests = Mock()


def get_data():
    r = requests.get("http://localhost/api/data")
    if r.status_code == 200:
        return r.json()
    return None


# get_data()


def log_request(url):
    print(f"Making request to {url}")

    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "key": "value"
    }
    return response


class TestAPI(unittest.TestCase):
    def test_get_data_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_data()

    def test_data_logging(self):
        requests.get.side_effect = log_request
        get_data()
        assert get_data()['key'] == "value"
        assert requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()
