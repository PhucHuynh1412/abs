import random 
import pyinputplus as pin

print('I am thinking of a number between 1 and 20')

numOfMe = random.randint(1,20)
count = 0
stop = 0
while True:
    count = count + 1
    if stop == 5:
        print('You lose.')
        break
    stop = stop + 1
    print('Take a guess:')
    numOfUser = pin.inputInt()

    if numOfUser < numOfMe:
        print('Your guess is too low')
    if numOfUser > numOfMe:
        print('Your guess is too high')
    if numOfUser == numOfMe:
        print(f'Good job, you guessed my number in {count} guesses')
        break
