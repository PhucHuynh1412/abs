import time

n = 0
while True:
    print(' '*n + '********')
    if n == 10:
        reverse = False
    if n == 0:
        reverse = True
    if reverse == True:
        n += 1
    else:
        n -= 1
    time.sleep(0.1)


    
