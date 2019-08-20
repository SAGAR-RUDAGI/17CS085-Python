def search(arr,key):
	if key in arr:
		return True
	else:
		return False

arr = []
arr.extend(map(int,input().split()))
key = int(input())
res =  search(arr,key)
if res:	
	print("Exists")
else:
	print("Not exists")