'''
	[문제]
		반복문을 사용해서 아래와 같이 출력해보세요.
		[예시]
				0 30
				1 29
				2 27
				3 24
				4 20
				5 15
				6 9
				7 2
				8 -6
				9 -15
'''
x = 0
y = 30
i = 0
while i < 10:
	print(x, y)
	x += 1
	y = y - x
	i += 1
