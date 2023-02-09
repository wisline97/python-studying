'''
	[문제]
        80의 약수 중에서 순서대로 약수를 출력했을 때, 
        [조건1] 일의자리가 4인 약수들만 출력하고,
        [조건2] 그 전체 합을 출력하시오.
        [조건3] 위 수의 개수도 출력하시오.
    [정답]
        4 
        total = 4
        count = 1    
'''
count = 0
total = 0
for i in range(1,81):
	if 80%i == 0:
		if (i%10) == 4:
			count += 1
			total += i

print(total)
print(count)