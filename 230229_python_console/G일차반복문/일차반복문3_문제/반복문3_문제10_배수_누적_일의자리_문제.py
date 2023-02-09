'''
	[문제]
	    100~200 사이의 숫자 중에서 
        [조건1] 6의 배수 중에서 일의 자리가 2인 수만 출력하고, 
        [조건2] 그 합을 구하시오.
        [조건3] 그 개수를 구하시오.
    [정답]
        102 132 162 192 
        total = 588
        count = 4
'''
count = 0
total = 0
for i in range(100,201):
	if i%6 == 0:
		if (i%10) == 2:
			print(i)
			count += 1
			total += i

print("합",total)
print("수",count)