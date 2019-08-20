def rev(string):
	lst = string.split(" ")
	lst.reverse()
	print(" ".join(lst))

def rev2(string):
	lst = string.split(" ")
	string2 = ''
	for i in lst:
		string2 = string2 + i[::-1] + " "
	print(string2)

string = input()
rev(string)
rev2(string)