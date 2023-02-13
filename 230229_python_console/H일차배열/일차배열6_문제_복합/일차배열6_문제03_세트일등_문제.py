'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		일등 학생의 번호와 점수를 출력하시오.
	[정답]
		번호 = 1002
		점수 = 82
'''
a = [1001, 40, 1002, 82, 1003, 65, 1004, 70]

max = 0
max_num = 0

for i in range(len(a)):
	if a[i] < 101:
		if a[i] > max:
			max = a[i]
			max_num = a[i-1]

print(max_num)
print(max)