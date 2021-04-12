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



def create_word(word, blacklist_count, whitelist_count):
    """Create and return a new word, or mark word as whitelisted/blacklisted."""
    
    word = WordMasterlist(word=word,
                          blacklist_count=blacklist_count,
                          whitelist_count=whitelist_count)

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



if __name__ == '__main__':
    from server import app
    connect_to_db(app)