n = int(input())
list1 = []
list1.extend(map(int,input().split(" ")))
print(list1)
list2  = [i for i in list1 if i%2==0]
print(list2)