'''
#DebuggingCoinToss.py
#Original Code
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
    print('You got it!')
    else:
    print('Nope. You are really bad at this game.')
    '''
import random
toss = random.randint(0, 1) 
print('0 is tails, 1 is heads')
#Debug
print('Actual num is:'+str(toss))
guess = None
try:
    while guess not in (0,1):
        guess = int(input('Guess the coin toss! Enter heads or tails:'))
except ValueError:
    print('Please enter 0 or 1')
if toss == guess:
    print('You got it!')
else:
    try:
        guess = int(input('Nope! Guess again!'))
    except ValueError:
        print('Please enter 0 or 1')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
