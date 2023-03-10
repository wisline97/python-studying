'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		3 2 1
		6 5 4
		9 8 7
		12 11 10
		15 14 13
		18 17 16
'''
import random

num = random.randint(3,6)
print(num)


# 1차반복문
for i in range(1, num+1):
	max = 3*i
	print(max,max-1,max-2)

print()


# 2차반복문
for i in range(1, num+1):
	max = 3*i
	for y in range(3):
		print(max, end=" ")
		max-=1
	print()
