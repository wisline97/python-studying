'''
	[문제]
		아래 a리스트의 값을 자리별로 분리 후,
		그 합을 total 리스트에 추가하시오.
	[예시]
		[1] 1 + 3 + 2  				total = [6]
		[2] 4 + 3 + 5 + 4  			total = [6,16]
		[3] 2 + 3 + 3 				total = [6,16,8]
		[4] 6 + 6 + 7 + 6 + 5  		total = [6,16,8,30]
	[정답]
		total = [6, 16, 8, 30]
'''

a = [132, 4354, 233, 66765]
total = []

for idx in range(len(a)):
    a_str = str(a[idx])
    add = 0
    for nums in range(len(a_str)):
        add += int(a_str[nums])
    total.append(add)
    
print(total)