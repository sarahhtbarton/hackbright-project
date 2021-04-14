def test_middle_table_logic(required_letter, additional_letters, word_list):

    for word in word_list:
        if (required_letter in word) and all(character in additional_letters for character in word):
            print(word)
            crud.create_assoc()

#####
def test_logic_w_sql_alchemy(): #do I pass in my model.py classes?? If imported up top, act as global variables, dont need to pass as parameters

    words = db.session.query(WordMasterlist.word).all()
    word_list = [word for (word,) in words]

    todays_letters = db.session.query(LetterInput).filter_by(entry_date=date.today()).first()
    todays_required = todays_letters.required_letter
    todays_all = todays_letters.all_letters

    for word in word_list:
        if (todays_required in word) and all(character in todays_all for character in word):
            print(word)
    
    crud.create_assoc() #what do i put in my crud operator? def create_assoc(letters_assoc, words_assoc). 


####
def test_assoc_table_creation(): #put in server.py
    word_masterlist_objects = db.session.query(WordMasterlist).all()
    letter_input_objects = db.session.query(LetterInput).filter_by(entry_date=date.today()).first()

    for object in word_masterlist_objects:
        if (letter_input_objects.required_letter in object.word) and all(character in letter_input_objects.all_letters for character in object.word):
            letters_assoc = letter_input_objects.letter_input_id
            words_assoc = object.word_masterlist_id

            crud.create_assoc(letters_assoc, words_assoc)






#need word_id and letter_id -- keep track of them too
# crud only wants the id of the letters id and the words id
# letters_assoc = the foreign key from the LetterInput Table
# words_assoc = the foreign key from the WordMasterlist Table

#look up the word through a join.