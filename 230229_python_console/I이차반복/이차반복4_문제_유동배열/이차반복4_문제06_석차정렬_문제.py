'''
	[문제]
		석차를 출력하시오.
	[정답]
		2 3 4 1 
'''

numList = [1001, 1002, 1003, 1004]
scoreList = [87, 42,  11, 98]

for i in range(len(scoreList)):
	count = 1
	for y in range(len(scoreList)):
		if scoreList[i] < scoreList[y]:
			count += 1
	print(count, end=" ")
