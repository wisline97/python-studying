'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		12345
		1234
		123
		12
		1
'''

for i in reversed(range(1,6)):
	for y in range(i):
		print(y+1, end=" ")
	print()