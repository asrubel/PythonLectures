import unittest
from lecture_28_mock_requests import log_request, get_data
from unittest.mock import patch


class TestAPI(unittest.TestCase):
    @patch('lecture_28_mock_requests.requests')
    def test_data_logging(self, mock_requests):
        mock_requests.get.side_effect = log_request
        get_data()
        assert get_data()['key'] == "value"
        assert mock_requests.get.call_count == 2

    def test_data_logging_with(self):
        with patch('lecture_28_mock_requests.requests') as mock_requests:
            mock_requests.get.side_effect = log_request
            get_data()
            assert get_data()['key'] == "value"
            assert mock_requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()
