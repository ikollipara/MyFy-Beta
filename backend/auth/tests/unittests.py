# tests/unittests.py
# Ian Kollipara
# 2020.11.22
# Unit Tests for Auth Microservice

# Imports
import unittest
import requests
import app


class TestTokenFailFunctions(unittest.TestCase):
    def test_get_token(self):
        self.assertEqual(app.get_token(), {})

    def test_store_token(self):
        self.assertDictEqual(app.store_token(), {"Error": ["No Token Code"]})

    def test_refresh_token(self):
        self.assertEqual(app.refresh_token(), {})


if __name__ == "__main__":
    unittest.main()