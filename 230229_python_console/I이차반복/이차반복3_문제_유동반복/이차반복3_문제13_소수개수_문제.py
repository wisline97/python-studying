'''
	[문제]
		2~100 사이의 랜덤 숫자 하나를 저장하고, 
		2부터 그 숫자 사이의 모든 소수의 개수를 출력하시오.

	[예시]
		r = 20
	 	소수 = 2, 3, 5, 7, 11, 13, 17, 19
		개수 = 8
'''
import random

num = random.randint(2,100)

prime = []

for i in range(1,num+1):
	count = 0
	for y in range(1,i+1):
		if i % y == 0:
			count += 1
	if count > 1 and count < 3:
		prime.append(i)

print("랜덤숫자 =",num)
print("소수 =",prime)
print("개수 =",len(prime))