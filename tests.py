from server import app
from unittest import TestCase
from model import connect_to_db, db #for database tests...

class SolverUnitTests(TestCase):
    """ Unit Tests -- checks function logic."""

    def test_    (self):
        self.assert


class SolverIntegrationTests(TestCase):
    """Integration Tests -- Testing Flask app/server -- checks routes."""

    def setUp(self):
        self.client = app.test_client() # Get the Flask test client
        app.config['TESTING'] = True # Show Flask errors that happen during tests
    
    def homepage_test(self):
        """“Does this URL path map to a route function?”"""
        result = client.get('/')
        self.assertEqual(result.status_code, 200)
    
    def get_request_test(self):
        """“Does this route function return the right HTML?”"""
        result = self.client.get('/')
        self.assertIn(b'<h1>Welcome to Spelling Bee Solver</h1>', result.data) #revisit if change the copy
    
    def post_form_test(self):
        result = client.post('/ajax-create-letters', data={'required-letter': 'l', 'all-letters': 'ncweaol'})
        self.assertIn(b'l is the twelth letter in the alphabet', result.data) #`data` is a dictionary of form key/value pairs. `result.data` is the html response string

class SolverFlaskDatabaseTests(TestCase):
    """Flask tests that use the database."""

    def

if __name__ == "__main__": # If called like a script, run our tests
    unittest.main()