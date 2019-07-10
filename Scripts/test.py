import word_functions

#a=(word_functions.number_to_words(input()))
#print(a)
#print(word_functions.words_to_number(input()))

test_number_list = list()
test_word_list = list()

for test in open('test_number.txt').read().split('\n'):
    test_number_list.append(test)

for test in open('test_word.txt').read().split('\n'):
    test_word_list.append(test)

test_number_list.remove('')
test_word_list.remove('')

#print(test_number_list)
#print(test_word_list)

## CHECKER

for i in range(len(test_number_list)):
    if test_word_list[i] != word_functions.number_to_words(test_number_list[i]):
        print("Test Failed for "+test_number_list[i]+" \n Expected "+test_word_list[i]+" \n Got "+ word_functions.number_to_words(test_number_list[i]))

    else:
        print("Input: "+test_number_list[i]+" \nOutput: "+test_word_list[i]+" \n Test Passed \n")


for i in range(len(test_word_list)):
    if test_number_list[i] != word_functions.words_to_number(test_word_list[i]):
        print("Test Failed for "+test_word_list[i]+" \n Expected "+test_number_list[i]+" \n Got "+ word_functions.words_to_number(test_word_list[i]))

    else:
        print("Input: "+test_word_list[i]+" \nOutput: "+test_number_list[i]+" \n Test Passed \n")


for i in range(len(test_number_list)):
    print(word_functions.all_wordifications(test_number_list[i]))
    print("\n")
