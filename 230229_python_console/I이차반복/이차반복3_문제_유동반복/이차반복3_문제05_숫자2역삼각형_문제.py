'''
	[문제]
		아래와 같이 삼각형을 출력하시오.
	[예시]
		123123
		12312
		1231
		123
		12
		1
'''

for i in reversed(range(1,7)):
	write = 1
	for y in range(i):
		if write == 4:
			write = 1
		print(write,end="")
		write += 1

	print()