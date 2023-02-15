'''
	[문제]
		아래 리스트 두 개를 합치고 오름차순으로 정렬하시오. 
	[정답]
		[1, 2, 3, 5, 7, 8, 9, 10, 12, 15, 19, 20]
'''
a =[9,10,3,2,20,19]
b = [15,12,1,5,7,8]
c = []

for i in range(len(a)):
    c.append(a[i])

for i in range(len(b)):
    c.append(b[i])
    
print(c)

for min_i in range(len(c)):
    for max_i in range(len(c)):
        if min_i!=max_i and	c[min_i] < c[max_i]:
            temp = c[max_i]
            c[max_i] = c[min_i]
            c[min_i] = temp
            print(min_i,"번째 턴",c)
    print()
            
print(c)