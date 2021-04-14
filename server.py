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


@app.route('/ajax-create-letters', methods=['POST'])
def get_todays_letters():
    """Creates an entry for today's Spelling Bee letters"""

    entry_date = date.today()
    all_letters = request.form.get('all-letters')
    required_letter = request.form.get('required-letter') #prob want to make sure all lowercase

    letters_record = crud.create_letters(entry_date, all_letters, required_letter) #crud returns a letters record -> setting it equal to a variable tht i can use and pass to the next crud operator

    crud.create_assoc_logic(letters_record)

    return 'success' #revisit the message...


@app.route('/ajax-create-feedback', methods=['POST'])
def get_word_feedback():
    """Adds words to the whitelist or blacklist"""

    word = request.form.get('word-feedback')
    feedback = request.form.get('feedback')

    if feedback == 'blacklisted':
        #is this right? test it out
        blacklist_count = db.session.query(WordMasterlist).filter(WordMasterlist.word == word).one()
        blacklist_count += 1
        # #do you need the next two lines or is the blacklist_count updated now?
        # whitelist_count = db.session.query(WordMasterlist.whitelist_count).filter(WordMasterlist.word == word).one()
        # crud.create_word(word, blacklist_count, whitelist_count) #does create_word override a previous entry?
    
    if feedback == 'whitelisted':
        crud.create_word(word, 0, 1)
    
    return 'got feedback'



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)