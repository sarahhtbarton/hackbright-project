from server import app
from unittest import TestCase
from model import connect_to_db, db #for database tests...
import crud
from datetime import date

# class SolverUnitTests(TestCase):
#     """ Unit Tests -- checks pure function logic -- needs to not touch anything else."""

#     def test_regex(self):
#         """Tests REGEX logic"""
#         letters_record = LetterInput.query.filter(LetterInput.all_letters == 'zzzzzzz', LetterInput.required_letter == 'z').one()
#         test_assoc = crud.create_assoc_logic(letters_record) 
#         assert test_assoc.word == 'zzzzzzzzzzzzzzzzzzz'
#         # the return is create_assoc_table return -- assoc


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

    letters_record = crud.create_letters(date.today(), 'azzzzzz', 'z') #can i give it an object directly instead of creating one? Yes -- query it -- query for the letters
    test_case = crud.create_assoc_logic(letters_record)

    def database_tests():
        """Tests database relationships"""
        test = [test_case.word_masterlist_id for test_case in test_case.association]
        assert test == [367518]
    
    def database_relationship_test():
        assoc_object = test_case.association
        assert assoc_object.words_assoc.word == 'zzzzzzzzzzzzzzzzzzz'
    
    def delete_record():
        """Deletes test data"""
        LetterWordAssoc.query.filter(LetterWordAssoc.letterword_id == test_case.letterword_id).delete()
        db.session.commit()
        #do the same with the letters record. 
        #make sure they're deleted-- call letter_record and test_case, make sure nothing shows up



if __name__ == "__main__": # If called like a script, run our tests
    unittest.main()