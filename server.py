"""Server for Spelling Bee Solver app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, LetterInput, LetterWordAssoc, WordMasterlist #bringing in the classes so i can query them for assoc table creation
from jinja2 import StrictUndefined
from datetime import date
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


# this belongs in crud
# def make_word_masterlist():
#     """Populates word_masterlist table from words_dictionary.json"""

#     with open('data/words_dictionary.json') as word_file:
#         valid_words = json.loads(word_file.read())
    
#     word_list = list(valid_words)
#     for word in word_list:
#         if len(word) > 3:
#             return word
    
#     crud.create_word(word)


def get_todays_letters():
    """Creates an entry for today's Spelling Bee letters"""

    entry_date = date.today()
    all_letters = request.form.get('all-letters')
    required_letter = request.form.get('required-letter') #prob want to make sure all lowercase or uppercase

    crud.create_letters(entry_date, all_letters, required_letter)


# def get_word_feedback(): #have to import the classes from model.py??
#     """Adds words to the whitelist or blacklist"""

#     word = request.form.get('word-feedback')

#     if request.form.get('feedback') == 'blacklisted':
#         #is this right? test it out
#         blacklist_count = db.session.query(WordMasterlist).filter(WordMasterlist.word == word).one()
#         blacklist_count += 1
#         #do you need the next two lines or is the blacklist_count updated now?
#         whitelist_count = db.session.query(WordMasterlist.whitelist_count).filter(WordMasterlist.word == word).one()
#         crud.create_word(word, blacklist_count, whitelist_count) #does create_word override a previous entry?
    
#     if request.form.get('feedback') == 'whitelisted':
#         crud.create_word(word, 0, 1)



# # # def create_assoc_table(): #dont think you'd have in server.py

def create_assoc_table():
    "Creates an association table for today's valid words"
    word_masterlist_objects = db.session.query(WordMasterlist).all()
    letter_input_object = db.session.query(LetterInput).filter_by(entry_date=date.today()).first() #is this how i want to do the letters? relies on proper user input...

    for object in word_masterlist_objects:
        if (letter_input_object.required_letter in object.word) and all(character in letter_input_object.all_letters for character in object.word):
            letter_input_id = letter_input_object.letter_input_id
            word_masterlist_id = object.word_masterlist_id

            crud.create_assoc(letter_input_id, word_masterlist_id)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)