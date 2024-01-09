import unittest
import requests
from password_checker import request_api, password_check, get_password_leaks
import hashlib


class TestPasswordChecker(unittest.TestCase):

    def test_request_api_success(self):
        fake_password = "pass"
        fake_hashed_password = hashlib.sha1(fake_password.encode('utf-8')).hexdigest().upper()
        query = fake_hashed_password[:5]
        response = request_api(query)
        self.assertEqual(response.status_code, 200)

    def test_request_api_failure(self):
        with self.assertRaises(RuntimeError):
            request_api("invalid_range")

    def test_password_check(self):
        response, tail = password_check("password123")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(tail)

    def test_get_password_leaks_with_leaks(self):
        fake_hashes_response = "001122:2\n334455:5\nAABBCC:10"
        fake_response = requests.Response()
        fake_response._content = fake_hashes_response.encode('utf-8')
        count = get_password_leaks(fake_response, "334455")
        self.assertEqual(count, 5)

    def test_get_password_leaks_without_leaks(self):
        fake_hashes_response = "001122:2\n334455:5\nAABBCC:10"
        fake_response = requests.Response()
        fake_response._content = fake_hashes_response.encode('utf-8')
        count = get_password_leaks(fake_response, "XYZ123")
        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
