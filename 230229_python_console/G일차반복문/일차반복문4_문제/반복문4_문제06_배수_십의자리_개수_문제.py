'''
	[문제] 
	   	1000보다 큰 수중에서 8의 배수를 검색하고, 
     	십의자리가 5인 배수를
		가장 작은 수부터 차례대로 4개를 출력하시오.
	[정답]
		1056 1152 1256 1352 
'''

count = 0
for i in range(1000,10001):
	if i%8 == 0:
		if (i%100) // 10 == 5:
			print(i)
			count += 1
	if count == 4:
		break