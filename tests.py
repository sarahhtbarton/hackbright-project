import unittest
import server
from model import connect_to_db


class SolverIntegrationTests(unittest.TestCase):
    """Integration Tests -- Testing Flask app/server -- checks routes."""

    def setUp(self):
        self.client = server.app.test_client() # Get the Flask test client
        server.app.config['TESTING'] = True # Show Flask errors that happen during tests
        connect_to_db(server.app, "postgresql:///solver")
    
    def test_homepage(self):
        """“Does this URL path map to a route function?”"""
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
    
    def test_get_request(self):
        """“Does this route function return the right HTML?”"""
        result = self.client.get('/')
        self.assertIn(b'<h1>Welcome to Spelling Bee Solver</h1>', result.data) #revisit if change the copy
    
    def test_post_form(self):
        result = self.client.post('/ajax-create-letters', data={'required-letter': 'l', 'all-letters': 'ncweaol'})
        self.assertIn(b'allowance', result.data) #`data` is a dictionary of form key/value pairs. `result.data` is the html response string


if __name__ == "__main__": # If called like a script, run our tests
    unittest.main()