"""Script to seed database."""

import os
import json
from datetime import date

import crud
import model
import server

os.system('dropdb solver') #i'm going to want to get rid of this eventually? Cause ill want changes to WordMasterlist to persist...
os.system('createdb solver')

model.connect_to_db(server.app)
model.db.create_all()

# Load words from JSON file
with open('data/words_dictionary.json') as word_file:
    valid_words = json.loads(word_file.read())

# Seed WordMasterlist table
word_list = list(valid_words)
for word in word_list:
    if len(word) > 3:
        crud.create_word(word, 0, 0) #do you need to pass values for default variables blacklist & whitelist?