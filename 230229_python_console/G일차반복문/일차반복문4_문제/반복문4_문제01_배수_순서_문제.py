'''
	[문제] 
		[1] 100 이상의 숫자 중에서  
			7의 배수를 순차적으로 검색하고,
		[2] 그중 3번째 7의 배수를 출력하시오.
	[정답] 
		119
'''

count = 0

for i in range(100,1000):
	if i%7 == 0:
		count += 1
	if count == 3:
		print(i)
		break
