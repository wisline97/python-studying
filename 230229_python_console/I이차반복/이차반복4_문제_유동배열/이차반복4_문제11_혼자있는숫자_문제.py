'''
	[문제]
		a리스트에서 혼자있는 숫자만 출력하시오.
	[정답]
		20 50
'''

a = [10,20,30,40,40,10,30,10,50]

for i in range(len(a)):
	count = 0
	for y in range(len(a)):
		if a[i] == a[y]:
			count += 1
	if count < 2:
		print(a[i], end=" ")