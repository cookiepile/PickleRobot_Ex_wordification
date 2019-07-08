import detectEnglish
import word_functions
import re

# input phone number
phone_number=input()

# removing delimiters from the phone number extracting only numbers
number = re.findall("\d+", phone_number)
number = ''.join(number)

# find all possible combinations that can be formed using 2 or more letters from the wordified phone number
[combinations,f_index] = word_functions.number_to_words(number)

# create empty list words to store list of english words
words=[]

# create empty list word_index to store index of wordified alphabet respective to the english word in words list
word_index=[]

# iterate in all possible combinations to find english words
for word in combinations:

    # detect is true when word in combinations list belongs to the english dictionary
    detect = detectEnglish.isEnglish(word)

    # if english word detected, append english word in the list of words
    if detect:
        words.append(word)

        # note index of the first letter of the word from combinations
        word_index.append(combinations.index(word))

# consider longest word from words list to replace numbers in the telephone number
longest_word=max(words,key=len)

# find index of the longest word to use while replacing relative number in telephone number
longest_word_index = words.index(longest_word)

# changing the index value to print to get into telephone number with hyphen format
final_index = f_index[word_index[longest_word_index]]
if final_index>6:
    final_index+=3
elif final_index>3:
    final_index+=2
elif final_index>0:
    final_index+=1

# replacing numbers in telephone number with their wordified version
answer=str(phone_number[0:final_index])+longest_word+phone_number[final_index+len(longest_word)+1:len(phone_number)]
print(answer)
