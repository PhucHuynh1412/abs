import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message2 = 'phuclovenhu'

count_chars = {}
count_chars2 = {}

for char in message:
    count_chars.setdefault(char,0)
    count_chars[char] += 1

pprint.pprint(count_chars)

for char in message2:
	count_chars2.setdefault(char, 0)
	count_chars2[char] += 1

pprint.pprint(count_chars2)
