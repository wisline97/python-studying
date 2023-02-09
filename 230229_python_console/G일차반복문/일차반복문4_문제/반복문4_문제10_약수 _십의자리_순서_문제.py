'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때, 
        십의자리가 3인 두 번째 약수를 출력하시오.
	[정답]
		33
'''
count = 0
for i in range(1,10001):
	if 1980%i == 0:
		if (i%100)//10 == 3:
			count += 1
	if count == 2:
		print(i)
		break