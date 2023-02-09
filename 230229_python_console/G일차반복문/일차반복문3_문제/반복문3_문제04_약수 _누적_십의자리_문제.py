'''
	[문제]
	  	200의 약수 중에서 순서대로 약수를 출력했을 때, 
        [조건1] 십의자리가 4인 약수들만 출력하고, 
        [조건2] 그 전체 합을 구하시오.
        [조건3] 위 수의 개수를 출력하시오.
    [정답]
        40 
        total = 40
        count = 1
'''
count = 0
total = 0
for i in range(1,201):
	if 200%i == 0:
		if (i%100)//10 == 4:
			count += 1
			total += i

print(total)
print(count)