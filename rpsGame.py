import random
import time
import sys

print('ROCK, PAPER, SCISSOR')
data = {'r': 'ROCK',
        'p': 'PAPER',
        's': 'SCISSOR',
        'q': 'QUIT'}
win = 0
lose = 0
tie = 0

while True:
    print(f'{win} Wins, {lose} Loses, {tie} Ties')
    print('Enter your move: (r)rock, (p)paper, (s)scissor')
    
    user = data[input()]
    
    if user == 'QUIT': 
        sys.exit() 
    computer = list(data.values())[random.randint(0,2)]
    
    print(f'{user} versus ...')
    time.sleep(2)
    print(computer)

    if user == computer:
        tie += 1 
        print('It is tie!')
    if user == 'ROCK' and computer == 'PAPER':
        lose += 1
        print('You lose.')
    if user == 'ROCK' and computer == 'SCISSOR':
        win += 1
        print('You win.')
    if user == 'PAPER' and computer == 'ROCK':
        win += 1
        print('You win.')
    if user == 'PAPER' and computer == 'SCISSOR':
        lose += 1
        print('You lose.')
    if user == 'SCISSOR' and computer == 'ROCK':
        lose += 1
        print('You lose.')
    if user == 'SCISSOR' and computer == 'PAPER':
        win += 1
        print('You win.')

    


