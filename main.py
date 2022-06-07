import random
words = ['fish', 'food', 'represent', 'quick', 'edible', 'imaginary', 'lost', 'duck', 'lettuce', 'magic', 'mandatory', 'latent', 'escapade', 'garage', 'friends', 'search', 'match', 'loop', 'lamp', 'loot', 'steal', 'internet', 'grass', 'rocket', 'blade', 'swim', 'sword', 'axe', 'eye', 'knife', 'jar', 'rifle', 'revolver', 'sentry', 'dispenser', 'robot', 'baseball']

word = random.choice(words)
# print(word)

test = 'flavor'

mystery = list(test)


turns = 6

correct = ''
blanks = []


def eval_letter(user):
    # script will need to check wether the user guessed a letter that exists in the mystery word. 
    # script will need to keep track of which letters go where and when a letter is correctly guessed, will need to replace the blank space with that letter
    # maybe use the list that has been assigned to the mystery varaible and change those 
    if user in mystery:
        global correct, blanks
        correct += user
        print('You got it!')
    else:
        global turns
        turns -= 1
        print('Nope, wrong letter. Try again!')

def display_word(mystery):
    global blanks
    blanks = '_' * len(mystery)
    for l in range(len(mystery)):
        if mystery[l] in correct:
            blanks = blanks[:l] + mystery[l] + blanks[l+1:]
    print(''.join(blanks))
    print('')
    print('')
    # print(mystery)
    return blanks



while turns > 0:
    print(f"Remaining Turns: {turns}")
    user = input('Try to guess a letter in this mystery word: ')

    eval_letter(user)
    display_word(mystery)


