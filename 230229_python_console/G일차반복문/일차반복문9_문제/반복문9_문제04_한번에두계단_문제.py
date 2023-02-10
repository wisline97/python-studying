'''
	[문제]
		계단이 50 계단이 있다. 철수는 제일 위 계단에 서 있다. 
		철수는 한 번에 두 계단씩 내려간다. 
		철수가 왼발로 디딘 계단을 출력하시오.
		아래 조건을 참고하시오.
		[1] 철수는 한 번에 두 계단씩 내려간다.
		[2] 철수는 왼발부터 내려간다.
		[3] 5번 출력할 때마다 다른 발을 출력하시오.
		
		(좌) 48 (좌) 44 (좌) 40 (좌) 36 (좌) 32 
		(우) 30 (우) 26 (우) 22 (우) 18 (우) 14
		(좌) 12 (좌) 8 (좌) 4 (좌) 0
'''
철수위치 = 50
turn = True
count = 0
switch = False
while 철수위치 > 0:
	철수위치 -= 2

	if count > 4:
		switch = not switch
		count = 0
		print()

	#왼발
	if switch == False:
		if turn == True:
			count += 1
			print("(왼)",철수위치, end=" ")

	if switch == True:
		if turn == False:
			count += 1
			print("(오)",철수위치, end=" ")

	turn = not turn
