import unittest

from src.flaskframework import app


class TestEndpointStatus(unittest.TestCase):

    def test_home_status_code(self):
        with app.test_client() as client:
            result = client.get('/')
            self.assertEqual(result.status_code, 200)

