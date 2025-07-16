import unittest
from app import add, app

class BasicTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello from Flask!')

if __name__ == "__main__":
    unittest.main()
