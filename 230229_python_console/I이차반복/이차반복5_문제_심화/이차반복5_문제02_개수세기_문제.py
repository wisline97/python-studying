'''
	[문제]
		a리스트의 값을 중복없이 value에 저장한다.
		그리고 중복되는 개수를 count에 저장한다.
	[정답]
		value = [10,20,30,100]
		count = [2,3,5,1]
'''

a = [10, 20, 30, 30, 100, 10, 30, 30, 20, 30, 20]

value = []
count = []

for idx in range(len(a)):
	check = False
	for i in range(len(value)):
		if a[idx] == value[i]:
			check = True

	if not check:
		value.append(a[idx])

for idx in range(len(value)):
	cnt = 0
	for i in range(len(a)):
		if value[idx] == a[i]:
			cnt += 1
	count.append(cnt)

print(value)
print(count)