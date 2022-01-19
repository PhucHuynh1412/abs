message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message2 = 'Hello world, I like coding python'

count = {}
count2 = {}

for chr in message:
    count.setdefault(chr,0)
    count[chr] += 1

for ch in message2:
	count2.setdefault(ch,0)
	count2[ch] += 1

print(count)
print()
print(count2)

