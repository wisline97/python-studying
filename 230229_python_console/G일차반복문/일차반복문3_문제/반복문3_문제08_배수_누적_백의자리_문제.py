'''
	[문제]
	    1000~2000 사이의 숫자 중에서 
     	[1] 16의 배수 중에서 백의 자리가 7인 수만 출력하고, 
		[2] 그 합을 구하시오.
		[3] 개수를 구하시오.
    [정답]
		1712 1728 1744 1760 1776 1792 
		total = 10512
		count = 6
'''

count = 0
total = 0
for i in range(1000,2001):
	if i%16 == 0:
		if (i%1000)// 100 == 7:
			print(i)
			count += 1
			total += i

print("합",total)
print("수",count)