import random
from hangman_ascii import HANGMANPICS
words = ['fish', 'food', 'python', 'javascript', 'linux', 'apple', 'code', 'react', 'represent', 'quick', 'edible', 'imaginary', 'lost', 'duck', 'lettuce', 'magic', 'mandatory', 'latent', 'escapade', 'garage', 'friends', 'search', 'match', 'loop', 'lamp', 'loot', 'steal', 'internet', 'grass', 'rocket', 'blade', 'swim', 'sword', 'axe', 'eye', 'knife', 'jar', 'rifle', 'revolver', 'sentry', 'dispenser', 'robot', 'baseball']

word = random.choice(words)
# print(word)

test = 'flavor'

mystery = list(word)

# global variables
turns = 6
correct = ''
incorrect = ''
blanks = []


def eval_letter(user):
    # script will need to check wether the user guessed a letter that exists in the mystery word. 
    # script will need to keep track of which letters go where and when a letter is correctly guessed, will need to replace the blank space with that letter
    # maybe use the list that has been assigned to the mystery varaible and change those 
    if user in mystery:
        global correct, blanks
        correct += user
        print('You got it!')
        print('*****************************************************')
    else:
        global turns, incorrect
        turns -= 1
        incorrect += user
        print('Nope, wrong letter. Try again!')
        print('*****************************************************')

def display_word(mystery):
    global blanks
    for l in range(len(mystery)):
        if mystery[l] in correct:
            blanks = blanks[:l] + mystery[l] + blanks[l+1:]
    print('')
    print(''.join(blanks))
    print('')
    # print(mystery)
    return blanks

# this code displays blanks at start of game so users know how long the word is 
blanks = '_' * len(mystery)
print(''.join(blanks))

# this is the game loop
while turns > 0:
    print(HANGMANPICS[turns])
    print(f"Incorrect letters: {incorrect}")
    print(' ')
    user = input('Try to guess a letter in this mystery word: ')

    eval_letter(user)
    display_word(mystery)

    if blanks == word:
        print('✨ you won! ✨')
        break

    if turns == 0:
        print(HANGMANPICS[0])
        print(f"This is what the mystery word was: {word}")

