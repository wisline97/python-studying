'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''
count = 0
num1 = 0
num2 = 0

for i in range(1,10001):
	if 100%i == 0:
		count += 1
		if count == 2:
			num1 = i
		elif count == 5:
			num2 = i
			break

print(num2-num1)