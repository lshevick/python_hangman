import random
words = ['fish', 'food', 'represent', 'quick', 'edible', 'imaginary', 'lost', 'duck', 'lettuce', 'magic', 'mandatory', 'latent', 'escapade', 'garage', 'friends', 'search', 'match', 'loop', 'lamp', 'loot', 'steal', 'internet', 'grass', 'rocket', 'blade', 'swim', 'sword', 'axe', 'eye', 'knife', 'jar', 'rifle', 'revolver', 'sentry', 'dispenser', 'robot', 'baseball']

word = random.choice(words)
# print(word)

test = 'stand'

mystery = list(test)

def display_word(test):
    blanks = []
    for l in test:
        space = '_'
        blanks += space
    print(''.join(blanks))
    # print(mystery)
    return blanks



display_word(test)

user = input('Try to guess a letter in this mystery word: ')

def eval_letter(user):
    if user in mystery:
        print('yay!')
    else:
        print('nope!')




eval_letter(user)