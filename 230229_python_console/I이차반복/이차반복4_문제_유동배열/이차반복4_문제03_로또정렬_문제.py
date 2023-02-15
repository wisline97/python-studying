'''
	[문제] 
		1~45사이의 랜덤값 6개를 lotto에 저장하려 한다.
		단, 중복되는 숫자는 없어야 하며,
		내림차순 정렬 후 출력하시오.
	[예시]
        [40, 38, 27, 26, 18, 5]
'''
import random

lotto = []
count = 0


while True:
	check = False
	if count == 6:
		break

	num = random.randint(1,45)

	for i in range(len(lotto)):
		if lotto[i] == num:
			check = True

	if check == False:
		lotto.append(num)
		count += 1
	else:
		continue

print(lotto)