"""CRUD operations."""

from model import db, LetterInput, LetterWordAssoc, WordMasterlist, WordFeedback, connect_to_db
import json #do i have that part here?

def create_letters(entry_date, all_letters, required_letter):
    """Create and return the Spelling Bee letters for the day."""

    letters = LetterInput(entry_date=entry_date, 
                          all_letters=all_letters,
                          required_letter=required_letter)
    
    db.session.add(letters)
    db.session.commit()

    return letters



def create_word(word):
    """Create and return a new word."""
    
    # Load words from JSON file -- here or seed.py?
    with open('data/words_dictionary.json') as word_file:
        valid_words = json.loads(word_file.read())
    
    word_list = list(valid_words)
    for word in word_list:
        if len(word) > 3:
            db.session.add(word)
            db.session.commit()

    return word #not sure about this.....



def create_assoc(letter, worda): #do you do this with association tables????
    """Create and return an association."""

    assoc = LetterWordAssoc(letter=letter,
                            worda=worda)
    
    db.session.add(assoc)
    db.session.commit()

    return assoc



def create_listed(wordf, is_blacklisted, is_whitelisted): #do you put foreign keys up here? NO, but the variables you defined for the backref!
    """Create and return a white or blacklisted word"""

    listed = WordFeedback(wordf=wordf, is_blacklisted=is_blacklisted, is_whitelisted=is_whitelisted)
    
    db.session.add(listed)
    db.session.commit()

    return listed



if __name__ == '__main__':
    from server import app
    connect_to_db(app)