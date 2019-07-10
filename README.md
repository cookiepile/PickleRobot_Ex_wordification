# READ ME #

Steps to RUN Automated test case(works for linux based system (require bash and python3))
```bash
git clone https://github.com/explorerneha/PickleRobot_Ex_wordification.git
cd PickleRobot_Ex_wordification/Scripts/
python3 test.py
```
To expand the test cases modify test_number.txt and test_word.txt and add the phone number and its respective wordified phone number
Note: The function number_to_words returns the string which has maximum word length. If there is a possibility of 2 or more words of equal length, it returns first word found in dictionary

Steps to RUN for user input(works for linux based system (require bash and python3))
```bash
git clone https://github.com/explorerneha/PickleRobot_Ex_wordification.git
cd PickleRobot_Ex_wordification/Scripts/
python3 main.py
```

Otherwise import this repository as PyCharm project

## word_function ##
consists 3 functions namely:
```bash
number_to_words()
words_to_number()
all_wordifications()
```
1. number_to_words(), which takes as an argument a string representing a US phone
number and which outputs a string which has transformed part or all of the phone
number into a single "wordified" phone number that can be typed on a US telephone (for
example, a valid output of number_to_words("1-800-724-6837") could be
"1-800-PAINTER"). If you find it makes things simpler, feel free to constrain this function
to only output "wordifications" in English.

2. words_to_number(), which does the reverse of the above function (for example, the
output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")

3. all_wordifications(), which outputs all possible combinations of numbers and English
words in a phone number.

# Folder Description #

## Scripts ##
Contains python scripts and relevant files needed to run the project without IDE

## Test ##
Contains python script called test which runs test cases using test_number and test_word files which can be edited to add more test cases

## venv ##
Virtual environment folder containing dependencies to run main script
Consists of word_function script

## Lib ##
consists of detectEnglish script that checks if any word input exists in the dictionary.txt file. returns boolean True/False
Script and dictionary.txt file found on https://inventwithpython.com/hacking/chapter12.html







