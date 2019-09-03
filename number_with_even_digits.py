for i in range(100,401):
	lst = [int(j) for j in str(i) if int(j)%2==0]
	if("".join(str(digit) for digit in lst)==str(i)):
		print(int(i),",",end=" ")
