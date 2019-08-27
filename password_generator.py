import string, random
str = string.printable
for i in range(0,6):
	print(str[random.randint(0,100)], end = '')
print()

