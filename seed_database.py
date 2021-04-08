"""Script to seed database."""

import os
import json
from random import choice #, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb solver')
os.system('createdb solver')

model.connect_to_db(server.app)
model.db.create_all()

# Load words from JSON file
with open('data/words_dictionary.json') as word_file:
    valid_words = json.loads(word_file.read())

# Seed Word Masterlist table
word_list = list(valid_words)
for word in word_list:
    if len(word) > 3:
        crud.create_word(word)



