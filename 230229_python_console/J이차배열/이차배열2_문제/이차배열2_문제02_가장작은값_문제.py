'''
    [문제]
        a리스트를 이차원으로 만들고 랜덤 값(-100~100)을 3개씩 3줄 총 9개를 만들고
        사각형모양 으로 출력한다.
        그 중에 가장 작은 값을 출력하시오.
    [예시]
        [6,-12,90]
        [-98,45,18]
        [34,2,0]
    
        가장 작은 값 = -98
'''
import random

a = []

for turns in range(3):
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    num3 = random.randint(-100,100)
    a.append([num1, num2, num3])

print(a)

min = 100

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a)):
        if a[first_idx_of_a][second_idx_of_a] < min:
            min = a[first_idx_of_a][second_idx_of_a]

print(min)