'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든 복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝"을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''
import random

a = [1,7]
lotto = []

svn_cnt = 0
one_cnt = 0

for i in range(7):
	num = random.randint(0,1)

	if num == 0:
		one_cnt += 1
		if one_cnt < 5:
			lotto.append(a[0])
		else:
			lotto.append(a[1])

	else:
		svn_cnt += 1
		if svn_cnt < 4:
			lotto.append(a[1])
		else:
			lotto.append(a[0])

print(lotto)

