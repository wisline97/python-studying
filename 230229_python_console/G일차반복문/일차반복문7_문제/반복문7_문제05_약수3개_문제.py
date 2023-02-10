'''
	[문제]
		어떤 수를 1부터 자기 숫자까지 나눠서 나눠지는 수를 약수라고 한다. 
		랜덤으로 1~100을 저장 후, 
		약수가 3개이면 "정답"을 
		아니면 "오답"을 출력하시오.
'''

for i in range(1,101):
	count = 0

	for divisor in range(1,i+1):
		if i%divisor == 0:
			count += 1
	if count == 3:
		print(i, count, "정답")
	else:
		print(i, count, "오답")
