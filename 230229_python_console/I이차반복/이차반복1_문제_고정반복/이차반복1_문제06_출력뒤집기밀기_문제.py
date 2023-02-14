'''
	[문제]
		3~6 사이의 랜덤 숫자 하나를 저장하고 그 숫자만큼 아래와 같은 규칙으로 출력하시오.
		단, 일차 반복문과 이차 반복문으로 출력하시오.
 	[예시]
		r = 6
	[출력]
		6 5 4
		5 4 3
		4 3 2
		3 2 1
'''
import random

num = random.randint(3,6)
print(num)
max = num

while True:
	if max-2 < 1:
		break

	print(max, max-1, max-2)
	max -= 1

print()


# 이차반복문
print(num)
max = num

while True:
	if max-2 < 1:
		break
	for y in range(3):
		print(max-y,end=" ")
	print()
	max -= 1