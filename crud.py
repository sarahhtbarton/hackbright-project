"""CRUD operations."""

from model import db, LetterInput, LetterWordAssoc, WordMasterlist, connect_to_db
import re #use regex

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


def create_assoc_table(letter_input_id, word_masterlist_id): #need to use the foreign keys, not the backref variable
    """Create and return an association."""

    print('crud.py line 36')

    assoc = LetterWordAssoc(letter_input_id=letter_input_id,
                            word_masterlist_id=word_masterlist_id)
    
    db.session.add(assoc)
    db.session.commit()

    return assoc


def create_assoc_logic(letters_record): #belongs in crud (anything that does database operations should live in crud)
    """Creates an association table for today's valid words"""
    
    word_masterlist_objects = WordMasterlist.query.all()

    all_letters = letters_record.all_letters
    required_letter = letters_record.required_letter
    pattern = f"[{all_letters}]*{required_letter}+[{all_letters}]*"
    compiled = re.compile(pattern)

    for object in word_masterlist_objects:
        if compiled.fullmatch(object.word) is not None:
            create_assoc_table(letters_record.letter_input_id, object.word_masterlist_id)
    
"""    
    print('crud.py line 49')
    
    word_masterlist_objects = WordMasterlist.query.all()

    print('crud.py line 53')

    for object in word_masterlist_objects:
        if (letters_record.required_letter in object.word) and all(character in letters_record.all_letters for character in object.word):
            letter_input_id = letters_record.letter_input_id
            word_masterlist_id = object.word_masterlist_id

            create_assoc_table(letter_input_id, word_masterlist_id)
    
    print('crud.py line 62')
"""


if __name__ == '__main__':
    from server import app
    connect_to_db(app)