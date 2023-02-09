'''
	[문제]
	    100~200 사이의 숫자 중에서
        [조건1] 9의 배수 중에서 십의 자리가 7인 수만 출력하고, 
        [조건2] 그 합을 구하시오.
        [조건3] 개수를 구하시오.
    [정답] 
        171 
        total = 171
        count = 1
'''

count = 0
total = 0
for i in range(100,201):
	if i%9 == 0:
		if (i%100)// 10 == 7:
			print(i)
			count += 1
			total += i

print("합",total)
print("수",count)