import time
import os, sys


grid1 = [['.','.', '.', '.', '.', '.', '.','.','.'],
         ['.','O', 'O', 'O', '.', 'O', 'O','O','.'],
         ['O','O', 'O', 'O', 'O', 'O', 'O','O','O'],
         ['O','O', 'O', 'O', 'O', 'O', 'O','O','O'],
         ['.','O', 'O', 'O', 'O', 'O', 'O','O','.'],
         ['.','.', 'O', 'O', 'O', 'O', 'O','.','.'],
         ['.','.', '.', 'O', 'O', 'O', '.','.','.'],
         ['.','.', '.', '.', 'O', '.', '.','.','.']]

grid2 = [['.','.', '.', '.', '.', '.', '.','.','.'],
         ['.','.', 'O', 'O', '.', 'O', 'O','.','.'],
         ['.','O', 'O', 'O', 'O', 'O', 'O','O','.'],
         ['.','O', 'O', 'O', 'O', 'O', 'O','O','.'],
         ['.','.', 'O', 'O', 'O', 'O', 'O','.','.'],
         ['.','.', '.', 'O', 'O', 'O', '.','.','.'],
         ['.','.', '.', '.', 'O', '.', '.','.','.'],
         ['.','.', '.', '.', '.', '.', '.','.','.']]



rong = len(grid1)
cao = len(grid1[0])
while True:
    for x in range(rong):
        for y in range(cao):
            print(grid1[x][y],end='')
        print()
    time.sleep(0.5)
    os.system('cls')  # For Windows
    for x in range(rong):
        for y in range(cao):
            print(grid2[x][y],end='')
        print()
    time.sleep(0.5)
    os.system('cls')  # For Windows
    

