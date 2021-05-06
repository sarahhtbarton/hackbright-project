"""Script to seed database."""

import os
import json
import crud
import model
import server

os.system('dropdb solver')
os.system('createdb solver') 

model.connect_to_db(server.app)
model.db.create_all()


with open('data/words_dictionary.json') as word_file:
    valid_words = json.loads(word_file.read())

word_list = list(valid_words)
for word in word_list:
    if len(word) > 3:
        crud.create_word(word, 0, 0)