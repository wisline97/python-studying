'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1
			23
			456
			7890
'''

a = [1,2,3,4,5,6,7,8,9,0]

cnt = 0
check = 1
for i in range(len(a)):
	cnt += 1
	print(a[i], end="")
	if cnt == check:
		print()
		cnt = 0
		check += 1
