"""CRUD operations."""

from model import db, LetterInput, LetterWordAssoc, WordMasterlist, connect_to_db

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



def create_assoc(letter_input_id, word_masterlist_id): #need to use the foreign keys, not the backref variable
    """Create and return an association."""

    assoc = LetterWordAssoc(letter_input_id=letter_input_id,
                            word_masterlist_id=word_masterlist_id)
    
    db.session.add(assoc)
    db.session.commit()

    return assoc



if __name__ == '__main__':
    from server import app
    connect_to_db(app)