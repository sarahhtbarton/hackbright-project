
def test_middle_table_logic(required_letter, additional_letters, word_list):

    for word in word_list:
        if (required_letter in word) and all(character in additional_letters for character in word):
            print(word)
    
    # has_required_list = []
    # for word in word_list:
    #     if required_letter in word:
    #         has_required_list.append(word)

    # print(has_required_list)

    # for word in has_required_list:
    #     if all(character in additional_letters for character in word):
    #         print(word)

# test_middle_table_logic('m', 'mibnadr', ['damn', 'brim', 'main', 'drama', 'bird', 'drain', 'helicopter', 'matinee', 'child'])
# test_middle_table_logic('m', 'ibnadr', ['damn', 'brim', 'main', 'drama', 'bird', 'drain', 'helicopter', 'matinee', 'child'])
    #works: 'damn', 'brim', 'main', 'drama'
    #missing middle letter: 'bird', 'drain'
    #too short: 
    # wrong entirely: 'helicopter', 'matinee', 'child'




# for word ...
#   append word to div in html

def trying_all(word, additional_letters):
    if all(character in additional_letters for character in word) == True:
        print(word)

# trying_all('matinee', 'mibnadr')
# trying_all('damn', 'mibnadr')