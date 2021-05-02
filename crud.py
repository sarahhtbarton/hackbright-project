"""CRUD operations."""

from model import db, LetterInput, LetterWordAssoc, WordMasterlist, connect_to_db
import re


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


def update_blacklist_count(word):
    """Increments an existing word's blacklist count by one"""
    word_object = db.session.query(WordMasterlist).filter(WordMasterlist.word == word).one()
    word_object.blacklist_count += 1
    db.session.commit()

    return word_object


def create_assoc_table(letter_input_id, word_masterlist_id, pentagram):
    """Create and return an association."""

    assoc = LetterWordAssoc(letter_input_id=letter_input_id,
                            word_masterlist_id=word_masterlist_id,
                            pentagram=pentagram)
    
    db.session.add(assoc)
    db.session.commit()

    return assoc


def create_assoc_logic(letters_record):
    """Creates an association table for today's valid words"""
    
    pattern = f"^[{letters_record.all_letters}]*{letters_record.required_letter}+[{letters_record.all_letters}]*$"
    word_masterlist_objects = WordMasterlist.query.filter(WordMasterlist.word.op('~')(f"{pattern}")).all()

    for object in word_masterlist_objects:
        pentagram = all(char in object.word for char in letters_record.all_letters)
        create_assoc_table(letters_record.letter_input_id, object.word_masterlist_id, pentagram)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)