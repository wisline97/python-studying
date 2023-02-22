'''
	[문제]
		복권 1개당 7칸으로, 총 5개의 복권을 제작하려 한다.
		복권 1줄은 1 또는 7의 랜덤 숫자로 구성되어 있다.
		7이 연속으로 3개 이상이면 "당첨"이고, 그 미만은 "꽝"이다.
		5개 중에 딱 1개만 당첨 복권이고 나머지 4개는 꽝인 복권을
		랜덤으로 생성해서 출력하시오.
		
		예)
			1177117 (꽝)
			1117771 (당첨)
			7171117 (꽝)
			7711771 (꽝)
			7171717 (꽝)
'''
import random
lotto = [0, 0, 0, 0, 0]
random_num = [0,1]

check = False
lotto_check = False
direct_stop_trigger = False

for lotto_cnt in range(5):

	if lotto_cnt == 4 and check == False:
		# 만약 마지막 로또인데도 아직 당첨번호가 나오지 않았을 때 실행되는 반복문
		while True:
			temp = []
			for turns in range(7):
				one_or_seven = random.randint(0,1)
				if one_or_seven == 0:
					lotto_num = 1
				if one_or_seven == 1:
					lotto_num = 7
				temp.append(lotto_num)

			for idx_temp in range(len(temp)-2):
				if temp[idx_temp] == 7 and temp[idx_temp+1] == 7 and temp[idx_temp+2] == 7:
					lotto_check = True
				else:
					lotto_check = False

			if lotto_check:
				print(temp,"당첨!")
				direct_stop_trigger = True
				break
			else:
				continue

	if direct_stop_trigger:
		break

	if check:
	# 당첨 번호가 나왔을 때부터 작동하는 반복문
		while True:
			temp = []
			lotto_check = False
			for turns in range(7):
				one_or_seven = random.randint(0,1)
				if one_or_seven == 0:
					lotto_num = 1
				if one_or_seven == 1:
					lotto_num = 7
				temp.append(lotto_num)

			for idx_temp in range(len(temp)-2):
				if temp[idx_temp] == 7 and temp[idx_temp+1] == 7 and temp[idx_temp+2] == 7:
					lotto_check = True

			if lotto_check:
				continue
			else:
				print(temp,"꽝!")
				break

	if not check:
		temp = []
		# 당첨 번호가 나오지 않을 때까지만 작동하는 반복문
		for turns in range(7):
			one_or_seven = random.randint(0,1)
			if one_or_seven == 0:
				lotto_num = 1
			if one_or_seven == 1:
				lotto_num = 7
			temp.append(lotto_num)

		for idx_temp in range(len(temp)-2):
			if temp[idx_temp] == 7 and temp[idx_temp+1] == 7 and temp[idx_temp+2] == 7:
				check = True

		if check:
			print(temp,"당첨!")
		else:
			print(temp,"꽝!")

	lotto[lotto_cnt] = temp