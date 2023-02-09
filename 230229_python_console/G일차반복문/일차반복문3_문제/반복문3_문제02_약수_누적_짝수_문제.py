'''
	[문제]
		[조건1] 18의 약수 중 짝수들만 출력하고, 
     	[조건2] 총합을 출력하시오.
		[조건3] 개수를 구하시오.
	[정답]
		2 6 18 
		total = 26
		count = 3
'''
count = 0
total = 0
for i in range(1,19):
	if 18%i == 0:
		if i%2 == 0:
			count += 1
			total += i

print(total)
print(count)