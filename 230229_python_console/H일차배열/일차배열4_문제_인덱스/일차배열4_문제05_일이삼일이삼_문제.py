'''
	[문제]
		랜덤(2~10)의 숫자를 저장하고 
		랜덤 개수만큼 반복하면서 반복적으로 숫자를 저장한다.
		반복 숫자란? 1 2 3 1 2 3 1 2 3 을 반복해서 저장하는 것이다.
	[예1] 
		r = 8
		arr = [1,2,3,1,2,3,1,2]
	[예2] 
		r = 4
		arr = [1,2,3,1]
'''
import random

num = random.randint(2,10)
arr = []
cnt = 1
for i in range(num):
	if cnt > 3:
		cnt = 1
	arr.append(cnt)
	cnt += 1

print(num)
print(arr)
