# This program says hello and asks for my name

import numpy as np
import pyinputplus as pin
import random
import matplotlib.pyplot as plt

arr = np.arange(5)
for num in arr:
    print(random.randint(1,10))


print('What is your name?')
myName = input()

print('It is nice to meet you ' + myName)
print('The length of your name is ' + str(len(myName)))

print('What is your age?')
myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')

