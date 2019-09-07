fgh=int(input())
ad=map(int,input().split())
unique_list = [] 
for x in ad:
  if x not in unique_list: 
	  unique_list.append(x)
for x in unique_list: 
	print(x)
