'''
	[문제] 
		9의 배수 중 일의 자리가 6인 
		첫 번째 배수를 출력하시오.
	[정답]
 		36
'''

count = 0

for i in range(1,1000):
	if i%9 == 0:
		if i%10 == 6:
			count += 1

	if count == 1:
		print(i)
		break