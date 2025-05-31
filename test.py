import unittest
import requests
from app import app  # Import your Flask app (replace 'app' with your actual module name if different)

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello from your containerized Flask app!', response.data)

    def test_404_response(self):
        # Test a non-existent route
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

def manual_test():
    # Manual test (run this if you want to test against a running server)
    try:
        response = requests.get('http://localhost:5000/')
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
    except requests.ConnectionError:
        print("Could not connect to the server. Is it running?")

if __name__ == '__main__':
    # Run the unit tests
    unittest.main(exit=False)
    
    # Then run manual test (comment out if not needed)
    print("\nRunning manual test...")
    manual_test()