'''
	[문제]
		2~1000 사이의 랜덤 숫자 하나를 저장한다.
		위 숫자 바로 다음 소수를 출력하시오.
	
	[예시1]
		r = 1000
		소수 = 1009	 
	[예시2]
		r = 500
	    소수 = 503
'''
import random

num = random.randint(2,1000)
print(num)
min = num
check = False

while True:
	min += 1
	count = 0
	for i in range(1, min):
		if min%i == 0:
			print(min, i)
			count += 1
	if count < 2:
		break