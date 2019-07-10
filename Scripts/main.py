import word_functions

print("Enter 11 digit US telephone number to wordify!")
print(word_functions.number_to_words(input()))
print("Enter wordified 11 character telephone number to know relevant the keypad number!")
print(word_functions.words_to_number(input()))
print("Enter 11 digit US telephone number to generate all possible wordified telephone numbers!")
print(word_functions.all_wordifications(input()))


