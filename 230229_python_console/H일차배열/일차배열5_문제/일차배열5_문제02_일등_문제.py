'''
	[문제]
		다음은 학생 번호와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]

max = 0
max_idx = 0


for i in range(len(numberList)):
	if scoreList[i] > max:
		max = scoreList[i]
		max_idx = i

min = max
min_idx = 0

for i in range(len(numberList)):
	if scoreList[i] < min:
		min = scoreList[i]
		min_idx = i

print(max, numberList[max_idx])
print(min, numberList[min_idx])