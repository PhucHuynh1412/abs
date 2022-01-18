import sys
import time

while True:
    print('Type to exit to exit')
    response = input()
    if response == 'exit':
        time.sleep(2)
        sys.exit()
    print(f'You typed {response}.')


