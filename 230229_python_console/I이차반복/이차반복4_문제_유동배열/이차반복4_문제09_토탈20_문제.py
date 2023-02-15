'''
	[문제]
		[1] a리스트에 1~10까지의 랜덤 숫자 3개를 저장 후 출력하시오.
		[2] 단, 숫자 3개는 서로 중복되면 안 된다. 
		[3] 숫자 3개의 합은 반드시 20이어야 한다. 
	[예시]
		[3, 10, 7] o 
		[5, 10, 5] x 
'''
import random

while True:
	a = [0,0,0]
	a_idx = 0
	total = 0

	while a_idx < 3:
		check = False
		num = random.randint(1,10)

		for i in range(len(a)):
			if a[i] == num:
				check = True

		if check == False:
			a[a_idx] = num
			a_idx += 1

	print()
	print(a)
	print()

	for i in range(len(a)):
		total += a[i]

	print(total)

	if total == 20:
		print("total값이 20입니다. 게임을 종료합니다.")
		break