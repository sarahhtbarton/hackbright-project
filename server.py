"""Server for Spelling Bee Solver app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, LetterInput, LetterWordAssoc, WordMasterlist
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

    letters_record = crud.create_letters(entry_date, all_letters, required_letter)
    crud.create_assoc_logic(letters_record)

    todays_valid_words = LetterWordAssoc.query.filter_by(letter_input_id=letters_record.letter_input_id).all()
    dict_for_jsonify = {"words": []}
    for object in todays_valid_words:
        dict_for_jsonify["words"].append(object.words_assoc.word)
    
    return jsonify(dict_for_jsonify)


@app.route('/ajax-create-feedback', methods=['POST'])
def get_word_feedback():
    """Adds words to the whitelist or blacklist"""

    word = request.form.get('word-feedback')
    feedback = request.form.get('feedback')

    if feedback == 'blacklisted':
        crud.update_blacklist_count(word)
    
    if feedback == 'whitelisted':
        crud.create_word(word, 0, 1)
    
    return 'got feedback'


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)