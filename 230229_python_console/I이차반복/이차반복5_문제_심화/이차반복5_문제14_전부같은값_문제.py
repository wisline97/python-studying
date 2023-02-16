'''
	[문제]
		a리스트와 b리스트의 값들이 각각 값과 개수가 똑같은지 확인한다.
		똑같으면 "같음", 아니면 "다름"을 출력하시오.
		위치는 상관없이 각각의 숫자의 개수가 일치하면 "같음"이다. 
	[정답]
'''
a = [10, 20, 30, 10, 20, 30]
b = [30, 20, 10, 20, 30, 10]


for a_idx1 in range(len(a)):
	count_a = 0
	count_b = 0
	for a_idx2 in range(len(a)):
		if a[a_idx1] == a[a_idx2]:
			count_a += 1
	for b_idx in range(len(b)):
		if b[b_idx] == a[a_idx1]:
			count_b += 1
	if count_a == count_b:
		print("같음")
		print(count_a, count_b)
	else:
		print("다름")
		print(count_a, count_b)