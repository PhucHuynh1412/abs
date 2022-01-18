while True:
    print('Who are you?')
    username = input()
    if username != 'Phuc':
        continue
    print('Hello Phuc')
    print('What is the password?')
    password = input()
    if password != 'swordfish':
        continue
    else:
        break
print('Access granted')
