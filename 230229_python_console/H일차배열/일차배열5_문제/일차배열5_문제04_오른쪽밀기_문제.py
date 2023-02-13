'''
	[문제]
		a리스트의 값중 0을 제외하고 모든값을 오른쪽으로 모으시오.
 	[결과]
 		a = [0,0,0,0,0,0,2,3,4,5];
'''


a = [0,0,2,0,3,0,4,0,0,5]
b = []

"""
for i in range(len(a)):
	if a[i] != 0:
		b.append(a[i])
		a[i] = 0

print(b)

a_idx = len(a)-1

for i in reversed(range(len(b))):
	a[a_idx] = b[i]
	a_idx -= 1

print(a)
"""

zero_idx = len(a) - 1
not_zero_idx = len(a) - 1

for i in range(len(a)):
	if a[not_zero_idx] != 0:
		temp = a[zero_idx]
		a[zero_idx] = a[not_zero_idx]
		a[not_zero_idx] = temp
		zero_idx -= 1

	not_zero_idx -= 1

print(a)