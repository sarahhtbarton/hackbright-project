""" Models for Spelling Bee Solver app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class LetterInput(db.Model):
    """The day's Spelling Bee letters."""

    __tablename__ = 'letter_input'

    letter_input_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True)
    entry_date = db.Column(db.DateTime)
    all_letters = db.Column(db.String(7))
    required_letter = db.Column(db.String(1))

    # association = a list of LetterWordAssoc objects

    def __repr__(self):
        """Show info about LetterInput"""
        return f'<LetterInput letter_input_id={self.letter_input_id} entry_date={self.entry_date} all_letters={self.all_letters} required_letter={self.required_letter}>'


class LetterWordAssoc(db.Model):
    """An association table that holds the words for the day's Spelling Bee letters"""

    __tablename__ = 'letterword_assoc'

    letterword_id = db.Column(db.Integer,
                              autoincrement=True,
                              primary_key=True)
    letter_input_id = db.Column(db.Integer, 
                                db.ForeignKey('letter_input.letter_input_id'))
    word_masterlist_id = db.Column(db.Integer,
                                   db.ForeignKey('word_masterlist.word_masterlist_id'))
    pentagram = db.Column(db.Boolean)
    
    letters_assoc = db.relationship('LetterInput', backref='association')
    words_assoc = db.relationship('WordMasterlist', backref='association')
    
    def __repr__(self):
        """Show info about LetterWordAssoc"""
        return f'<LetterWordAssoc letterword_id={self.letterword_id} letter_input_id={self.letter_input_id} word_masterlist_id={self.word_masterlist_id} pentagram={self.pentagram}>'


class WordMasterlist(db.Model):
    """All the words that are valid entries on Spelling Bee"""

    __tablename__ = 'word_masterlist'

    word_masterlist_id = db.Column(db.Integer,
                                  autoincrement=True,
                                  unique=True,
                                  primary_key=True)
    word = db.Column(db.String)
    blacklist_count = db.Column(db.Integer,
                                default=0)
    whitelist_count = db.Column(db.Integer,
                                default=0)

    # association = a list of LetterWordAssoc objects

    def __repr__(self):
        """Show info about WordMasterlist"""
        return f'<WordMasterlist word_masterlist_id={self.word_masterlist_id} word={self.word} blacklist_count={self.blacklist_count} whitelist_count={self.whitelist_count}>'


def connect_to_db(flask_app,
                  db_uri='postgresql:///solver',
                  echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)