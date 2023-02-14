'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
  
	[예시]
		********
		******
		****
		**
'''

for i in reversed(range(1,5)):
	mult = i*2
	for y in range(mult):
		print("*",end="")
	print()