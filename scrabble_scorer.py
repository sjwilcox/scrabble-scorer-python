import string

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""
    old_point_structure = OLD_POINT_STRUCTURE
    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                
            
    print(letterPoints)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")

   user_word = input('Enter a word to score: ')
   return user_word


def simple_scorer(word):
    word = word.upper()
    count = 0
    for char in word:
        if char in string.ascii_uppercase:
            count += 1
    total = f'{word.lower()} is {count} points'
    print(total)
    return total

def vowel_bonus_scorer(word):
    word = word.upper()
    vowels = "AEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 3
        else:
            count += 1
    total = f'{word.lower()} is {count} points'
    print(total)
    return total
    

def scrabble_scorer(word):
    word = word.upper()
    total = 0
    for char in word:
        for key, value in new_point_structure.items():
            if char == key:
                total += value
    point_total = f'{word} is worth {total} points.'
    print(point_total)
    return point_total

scoring_algorithms = ({'Scrabble','The traditional scoring algorithm.','scrabble_scorer'},
{'Simple Score', 'Each letter is 1 point','simple_scorer'},{'Bonus Vowels','Vowels are 3 pts, consonants are 1 pt.', 'vowel_bonus_scorer'})

def scorer_prompt(word):
    print('Which scoring algorithm would you like to use? ')
    user_select =  int(input('0 - Simple: One point per character\n 1 - Vowel Bonus: Vowels are worth 3 points\n 2 - Scrabble: Uses scrabble point system\n Enter your choice: '))
    if user_select == 0:
        simple_scorer(word)
    elif user_select == 1:
        vowel_bonus_scorer(word)
    else:
        scrabble_scorer(word)
    return word

def transform(old_point_structure):
    new_point_structure = {}
    for key , value in old_point_structure.items():
        for index in value:
            new_point_structure[index] = key
            
    return new_point_structure
                
new_point_structure = transform(OLD_POINT_STRUCTURE)
    

def run_program():
   
    word = initial_prompt()
    scorer_prompt(word)
    