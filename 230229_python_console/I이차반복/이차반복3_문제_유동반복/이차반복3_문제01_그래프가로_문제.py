'''
	[문제] 
		0~10 사이의 랜덤 숫자를 다섯 번 반복해서 저장하고
		그 랜덤 숫자만큼 * 을 출력하시오.
  
	[예]
		3   : ***
		10  : **********
		5   : *****
		6   : ******
		0   : 
		1   : *	
'''
import random

for i in range(5):
	num = random.randint(0,10)
	print(num," : ", end="")
	for y in range(num):
		print("*", end="")
	print()
