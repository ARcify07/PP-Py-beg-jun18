## file handling

file = open('simpleText.txt', 'r+')

file.read()
for line in file.readlines():
    print(line,end='')
mystory = "This story is about files"
file.seek(file.tell() + 27)
file.write(mystory)

print(file.read())

for line in file.read():
	print(line, end='')

print(file.closed)

## better method

with open('filename', 'mode'):
    pass

