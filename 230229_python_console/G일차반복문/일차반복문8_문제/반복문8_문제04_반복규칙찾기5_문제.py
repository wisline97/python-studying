'''
	[문제]
	  	반복문을 10회 반복해서 아래와 같이 출력하시오.
		[예시]
			0 0
			1 0
			2 1
			3 1
			4 2
			5 2
			6 3
			7 3
			8 4
			9 4
'''
y = 0
for x in range(0,10):
	print(x, round(y//1))
	y += 5/10