'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''

count = 0

for i in range(1,201):
	if 200%i == 0:
		if i%2 == 0:
			if (i%100)//10 == 8 or (i%100)//10 == 9 or i//100 == 1:
				print(i)
				break