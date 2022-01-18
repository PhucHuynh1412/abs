import random , time, copy
import numpy as np 
import pyinputplus as pin 

rong = 20 # số hàng
cao = 15  # số cột

nextCells = []

for x in range(rong):
    cot = []
    for y in range(cao):
        if random.randint(0,1) == 1:
            cot.append('o')
        else:
            cot.append(' ')
    nextCells.append(cot)

while True:
    print('\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(cao):
        for x in range(rong):
            print(currentCells[x][y], end = '')
        print()
    
    for x in range(rong):
        for y in range (cao):
            benTrai = (x-1)%rong
            benPhai = (x+1)%rong 
            benTren = (y-1)%cao 
            benDuoi = (y+1)%cao
            
            hangXom = 0
            if currentCells[benTrai][benTren] == 'o':
                hangXom += 1
            if currentCells[benTrai][y] == 'o':
                hangXom += 1
            if currentCells[benTrai][benDuoi] == 'o':
                hangXom += 1
            if currentCells[x][benTren] == 'o':
                hangXom += 1
            if currentCells[x][benDuoi] == 'o':
                hangXom += 1
            if currentCells[benPhai][benTren] == 'o':
                hangXom += 1
            if currentCells[benPhai][y] == 'o':
                hangXom += 1
            if currentCells[benPhai][benDuoi] == 'o':
                hangXom += 1
            
            if currentCells [x][y] =='o' and (hangXom == 2 or hangXom == 3):
                nextCells[x][y] == 'o'
            elif currentCells [x][y] == ' ' and hangXom == 3:
                nextCells [x][y] = 'o'
            else:
                nextCells [x][y] = ' '
            
    time.sleep(3)











