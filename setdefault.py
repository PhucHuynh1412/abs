import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count_chars = {}

for char in message:
    count_chars.setdefault(char,0)
    count_chars[char] += 1

print(count_chars)

print('-'*20)

pprint.pprint(count_chars)
