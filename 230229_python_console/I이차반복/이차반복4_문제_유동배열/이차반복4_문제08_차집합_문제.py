'''
	[문제]
		a와 b 두 리스트를 비교해서 서로 겹치지 않는 값을 
		temp에 저장하고 출력하시오.
	[정답]
		temp = [6, 4, 20, 3, 17, 13, 7]
'''
a = [16,  5, 11, 6, 19, 12, 18,  4, 20, 3]
b = [17, 11, 19, 5, 13, 18, 16, 12, 11, 7]
temp = []

for i in range(len(a)):
	check = False
	for y in range(len(b)):
		if a[i] == b[y]:
			check = True
	if check == False:
		temp.append(a[i])

	check = False
	for y in range(len(b)):
		if b[i] == a[y]:
			check = True
	if check == False:
		temp.append(b[i])

print(temp)	