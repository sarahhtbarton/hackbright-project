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


with open('data/words.txt') as word_file:
    words = word_file.read().split()

for word in words:
    crud.create_word(word, 0, 0)