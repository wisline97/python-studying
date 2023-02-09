'''
	[문제]
		철수는 13살 철수의 아버지는 45살이다. 
		몇 년 후 철수의 아버지는 철수 나이의 3배가 될지 구하시오.
	[정답]
		3
'''

chulsu = 13
father = 45
year = 0

while True:
	if (father+year) == (chulsu+year)*3:
		break
	year += 1

print(year,"년 후")