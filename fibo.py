def fibo(n):
	lst = []
	a=0
	b=1
	if n==0:
		lst.append("None")
	elif n==1:
		lst.append("0")
	elif n==2:
		lst.extend([0,1])
	else:
		lst.extend([0,1])
		for i in range(n-2):
			c=a+b
			lst.append(c)
			a=b
			b=c
	print(lst)


n = int(input())
fibo(n)