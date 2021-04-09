"""Server for Spelling Bee Solver app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
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


def get_todays_letters():
    """Creates an entry for today's Spelling Bee letters"""

    entry_date = date.today()
    all_letters = request.form.get('all-letters')
    required_letter = request.form.get('required-letter') #prob want to make sure all lowercase or uppercase

    crud.create_letters(entry_date, all_letters, required_letter)


def get_word_feedback():
    """Adds words to the whitelist or blacklist"""

    wordf = request.form.get('word-feedback')

    if request.form.get('feedback') == 'blacklisted':
        is_blacklisted = True #need return statements here?
        is_whitelisted = False
    else:
        is_blacklisted = False
        is_whitelisted = True

    crud.create_listed(wordf, is_blacklisted, is_whitelisted)

def make_word_masterlist():
    """Populates word_masterlist table from words_dictionary.json"""

    with open('data/words_dictionary.json') as word_file:
        valid_words = json.loads(word_file.read())
    
    word_list = list(valid_words)
    for word in word_list:
        if len(word) > 3:
            return word
            
    
    crud.create_word(word)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)