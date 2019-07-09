import re

# digit_map is a dictionary data type to map numbers with alphabets according to mobile keypad notation
digit_map = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
}

letter_map = {
    ('A','B','C')     : '2',
    ('D','E','F')     : '3',
    ('G','H','I')     : '4',
    ('J','K','L')     : '5',
    ('M','N','O')     : '6',
    ('P','Q','R','S') : '7',
    ('T','U','V')     : '8',
    ('W','X','Y','Z') : '9',
}

# word_numbers function takes number as string input of phone number with delimeters removed and returns all possible combinations of 2 or more alhabet words that can be formed
# word_numbers('543') returns an array of size 45 combinations of alphabets represented by number input like ['JG', 'JH', 'JI', 'KG', 'KH', 'KI','KHF', 'KID', 'KIE'.... ]along with index in number input of the first alphabet of the word created

def number_to_words(input):
  string_input = input

  # flag, flag2 used to offset single character words and empty string from array of combinations
  flag = 0

  # declare an empty list of final word combinations that have to be returned
  word_combinations = ['']

  # fixing index1(id1) to iterate till length-1 to not consider single alphabet as word
  for id1 in range(len(string_input) - 1):

      # declare empty list letter_Combinations to store n letter combinations in each loop of n
      letter_combinations = ['']

      temp = ['']
      flag2 = 0

      # second index (id2) iterating from next character from id1 to create combinations of 2 or more letter words till end of string
      for id2 in string_input[id1:len(string_input)]:

          # fetch alphabets represented by number from digit_map
          letters = digit_map.get(str(id2), '')

          # generate all combination from each alphabet in letters
          temp = [prefix + letter for prefix in temp for letter in letters]

          # check flag2 for single character word and empty string in case of 0 and 1 as input
          if flag2 < 2:
              letter_combinations = temp

          # start storing combinations of 2 and more letter words in each loop
          else:
              letter_combinations = letter_combinations + temp
          flag2 += 1

      # fill empty list word_combinations for the first iteration at flag=0
      if flag < 1:
          word_combinations = letter_combinations
          alphabet_index= [id1]*len(letter_combinations)

      # append letter combinations into the word_combinations list after flag set in more than 1 iterations
      else:
          word_combinations = word_combinations + letter_combinations
          alphabet_index = alphabet_index + [id1]*len(letter_combinations)

      flag += 1

  return word_combinations,alphabet_index

#debug check
#print(len(number_to_words('543')[0]))

# words_to_number function takes wordified telephone number as input and returns numbered telephone number
def words_to_number(input):

    # remove delimiters and words from telephone number
    original_numbers=''.join(re.findall("\d+", input))

    # extract words with hyphen from telephone number
    wordified_numbers = ''.join(re.findall("\D+", input))

    # remove hyphen from the wordified_numbers
    word_array = [c for c in wordified_numbers if c not in ' -']
    word=''.join(word_array)

    # create array to store number converted from the wordified phone number
    converted_number = []

    # convert each character of word to number by mapping from dictionary letter_map
    for char in word:
        number = (next(v for k, v in letter_map.items() if char in k))
        converted_number.append(number)
    numbers = ''.join(converted_number)

    # find index in the input of the first numbr that was converted from word
    for i in range(len(input)):
        if word_array[0]==input[i]:
            final_index=i

            # change the index to combine the converted number with original_numbers from input
            if i <5:
                final_index -= 1
            elif i< 9:
                final_index -= 2
            else:
                final_index -= 3
            break

    # combine the converted number with original_numbers from input and store in phone_number
    phone_number=original_numbers[0:final_index]+numbers[0:len(numbers)]+original_numbers[final_index:len(original_numbers)]

    # final_phone_number is the phone_number in telephone number format with hyphens
    final_phone_number=phone_number[0]+'-'+phone_number[1:4]+'-'+phone_number[4:7]+'-'+phone_number[7:11]
    return final_phone_number

# debug check
# print(words_to_number('1-232-324-923Z'))
