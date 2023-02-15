'''
	[문제]		
		[1] com리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[2] me리스트에 0~9사이의 랜덤 숫자 3개를 저장하되 중복 값이 없어야 한다.
		[3] com과 me 를 비교해서 숫자가 같고 자리도 같으면 strike + 1
		[4] com과 me 를 비교해서 숫자가 같고 자리가 틀리면 ball + 1
		[5] 사용자에게 strike와 ball 개수를 출력해 보여준다.
		
		계속 반복하면서 strike가 3이 되면 종료한다.
'''
import random

com = [0, 0, 0]
com_idx = 0

while True:
	check = False
	num = random.randint(0,9)
	for i in range(len(com)):
		if num == com[i]:
			check = True
	if check == False:
		com[com_idx] = num
		com_idx += 1
	
	if com_idx == 3:
		break

while True:
	print()
	print("Game Start")
	print()
	ball = 0
	strike = 0
	me = [0, 0, 0]
	me_idx = 0
	while me_idx < 3:
		check = False
		num = random.randint(0,9)
		for i in range(len(me)):
			if num == me[i]:
				check = True
		if check == False:
			me[me_idx] = num
			me_idx += 1
	print()
	print(com)
	print(me)
	print()
	for i in range(len(me)):
		for y in range(len(me)):
			if i != y and me[i] == com[y]:
				ball += 1
				print(" ball! ",me[i],com[y])
			if i == y and me[i] == com[y]:
				print(" strike! ",me[i],i,com[y],y)
				strike += 1
	if strike == 3:
		print("Strike 3!!!!")
		print("Game Over!!!!")
		break