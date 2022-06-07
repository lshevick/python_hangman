import random
words = ['fish', 'food', 'represent', 'quick', 'edible', 'imaginary', 'lost', 'duck', 'lettuce', 'magic', 'mandatory', 'latent', 'escapade', 'garage', 'friends', 'search', 'match', 'loop', 'lamp', 'loot', 'steal', 'internet', 'grass', 'rocket', 'blade', 'swim', 'sword', 'axe', 'eye', 'knife', 'jar', 'rifle', 'revolver', 'sentry', 'dispenser', 'robot', 'baseball']

word = random.choice(words)
# print(word)

test = 'stand'

def display_word(test):
    word = list(test)
    blank = []
    # print(word)
    for char in word:
        res = '_'
        blank += res
    print(''.join(blank))
    return ''.join(blank)



display_word(test)