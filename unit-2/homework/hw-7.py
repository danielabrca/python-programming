#random module
import random

messages = ['You are awesome', 'Thanks for trying!', 'You should do something fun today!',
            'I knew it was you!', 'Let\'s go out!']

name = input('Enter you name or the letter \'e\' to finish the game: ')

while name != 'e':
    print(random.sample(messages, 1))
    name = input('Enter you name or the letter \'e\' to finish the game: ')
if name == 'e':
    print('End of game')