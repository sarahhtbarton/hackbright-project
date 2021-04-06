""" Models for Spelling Bee Solver app. """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime #only if i use a timestamp

db = SQLAlchemy()

class LetterInput(db.Model):
    """The day's Spelling Bee letters."""

    __tablename__ = 'letter_input'

    letter_input_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True
                                )
    date = db.Column(db.DateTime)
    required_letter = db.Column(db.String(1))
    additional_letters = db.Column(db.String(6))

    # do I need a relationship???

    def __repr__(self):
        return f'<LetterInput
                letter_input_id={self.letter_input_id}
                date={self.date}
                required_letter={self.required_letter}
                additional_letters={self.additional_letters}
                >'

class LetterWordAssoc(db.Model):
    """An association table that holds the words for the day's Spelling Bee letters"""

    __tablename__ = 'LetterWordAssoc' #does CamelCase work here?

    letterword_id = db.Column(db.Integer,
                              autoincrement=True,
                              primary_key=True
                              )
    letter_input_id = db.Column(db.Integer, 
                                db.ForeignKey('letter_input.letter_input_id')
                                )
    word_masterlist_id = db.Column(db.Integer,
                                   db.ForeignKey('word_masterlist.word_masterlist_id')
                                   )
    
    # do I need a relationship???

    def __repr__(self):
        return f'<LetterWordAssoc
                letterword_id={self.letterword_id}
                letter_input_id={self.letter_input_id}
                word_masterlist_id={self.word_masterlist_id}
                >'


class WordMasterlist(db.Model):
    """All the words that are valid entries on Spelling Bee"""

    __tablename__ = 'word_masterlist'

    word_masterlist_id = db.Column(db.Integer,
                                  autoincrement=True,
                                  primary_key=True
                                  )
    word = db.Column(db.String)

     # do I need a relationship???

    def __repr__(self):
        return f'<WordMasterList
                word_masterlist_id={self.word_masterlist_id}
                word={self.word}
                >'


class WordFeedback(db.Model):
    """User input on words Solver said were valid but Spelling Bee said were not
       or visa versa"""
    
    __tablename__ = 'word_feedback'
    
    word_feedback_id = db.Column(db.Integer,
                                 autoincrement=True,
                                 primary_key=True
                                 )
    word_masterlist_id = db.Column(db.Integer,
                                   db.ForeignKey('word_masterlist.word_masterlist_id')
                                   )
    is_blacklisted = db.Column(db.Boolean) #is this how you do boolean?
    is_whitelisted = db.Column(db.Boolean))

# do I need a relationship???

    def __repr__(self):
        return f'<WordFeedback
                word_feedback_id={self.word_feedback_id}
                word_masterlist_id={self.word_masterlist_id}
                is_blacklisted={self.is_blacklisted}
                is_whitelisted={self.is_whitelisted}
                >'

#i copy-pasted everything below from the ratings lab. What should I keep (and what does it do?)

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)