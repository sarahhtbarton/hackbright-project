"""CRUD operations."""

from model import db, LetterInput, LetterWordAssoc, WordMasterlist, WordFeedback, connect_to_db

def create_letters(date, required_letter, additional_letters):
    """Create and return the Spelling Bee letters for the day."""

    letters = LetterInput(date=date, 
                          required_letter=required_letter,
                          additional_letters=additional_letters)
    
    db.session.add(letters)
    db.session.commit()

    return letters



def create_word(word):
    """Create and return a new word."""

    word = WordMasterlist(word=word)

    db.session.add(word)
    db.session.commit()

    return word



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