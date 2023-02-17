'''
    apt 리스트는 아파트 1동의 각 세대를 의미한다.
    pay 는 이번달 관리비를 뜻한다.
'''
import random

apt = [
		[101, 102, 103],	
		[201, 202, 203],	
		[301, 302, 303]		
	]		
pay = [
		[1000, 2100, 1300],	 
		[4100, 2000, 1000],	 
		[3000, 1600,  800]  
	]
rank = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

'''
    [문제 1] 
        각 층별 관리비 합을 출력하시오.
    [정답 1] 
        4400 7100 5400
'''
print("[문제1]")
for first_idx_of_pay in range(len(pay)):
    total = 0
    for second_idx_of_pay in range(len(pay[first_idx_of_pay])):
        total += pay[first_idx_of_pay][second_idx_of_pay]
    print(total, end=" ")
print()

''' 
    [문제 2] 
        랜덤으로 호수와 관리비 한개 출력하시오.
    [예시 2]
        0 2
        103 1300 원 
'''
print("[문제2]")
random_first_idx_of_apt = random.randint(0,2)
random_second_idx_of_apt = random.randint(0,2)
print(apt[random_first_idx_of_apt][random_second_idx_of_apt],"호",end=" ")
print(pay[random_first_idx_of_apt][random_second_idx_of_apt],"원")


'''
    [문제 3] 
        관리비가 가장 많이 나온 집, 가장 적게 나온 집을 출력하시오.
    [정답 3]
        가장 많이 나온 집 = 201
        가장 적게 나온 집 = 303    
'''
print("[문제3]")
max = 0
for first_idx_of_pay in range(len(pay)):
    for second_idx_of_pay in range(len(pay[first_idx_of_pay])):
        if pay[first_idx_of_pay][second_idx_of_pay] > max:
            max = pay[first_idx_of_pay][second_idx_of_pay]
            max_idx = [first_idx_of_pay,second_idx_of_pay]

min = max
for first_idx_of_pay in range(len(pay)):
    for second_idx_of_pay in range(len(pay[first_idx_of_pay])):
        if pay[first_idx_of_pay][second_idx_of_pay] < min:
            min = pay[first_idx_of_pay][second_idx_of_pay]
            min_idx = [first_idx_of_pay,second_idx_of_pay]

print("가장 적게 나온 집")
print(apt[min_idx[0]][min_idx[1]], "호", end=" ")
print(min,"원")
print()
print("가장 많이 나온 집")
print(apt[max_idx[0]][max_idx[1]], "호", end=" ")
print(max,"원")
print()

'''     
    [문제 4] 
        관리비 많이나온 순서대로 rank리스트에 등수를 저장하시오.
    [정답 4]
        [7, 3, 6]
        [1, 4, 7]
        [2, 5, 9]
'''
print("[문제4]")

temp = []
rank_temp = []

for y in range(len(pay)):
    for x in range(len(pay[y])):
        temp.append(pay[y][x])

for i in range(len(temp)):
    count = 1
    for y in range(len(temp)):
        if temp[i] < temp[y]:
            count += 1
    rank_temp.append(count)

idx = 0
for y in range(len(rank)):
    for x in range(len(rank[y])):
        rank[y][x] = rank_temp[idx]
        idx+=1

print(rank)