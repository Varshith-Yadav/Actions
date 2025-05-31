import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello from your containerized Flask app!', response.data)

    def test_404(self):
        response = self.client.get('/doesnotexist')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
