'''
    [문제]
        [1] a이차리스트에 랜덤 값(1~100)을 9개 저장 후 출력하시오.
        [2] 랜덤으로 값 두 개를 선택 후 두 개의 위치를 교환 후 출력하시오.
    [예시]
    값 교체 전 >>>
    [46, 62, 75]
    [36, 18, 100]
    [26, 11, 39]

    r1 = 11
    r2 = 36
    
    값 교체 후 >>>
    [46, 62, 75]
    [11, 18, 100]
    [26, 36, 39]
'''
import random

a = [[0,0,0], [0,0,0], [0,0,0]]

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a[first_idx_of_a])):
        num = random.randint(1,100)
        a[first_idx_of_a][second_idx_of_a] = num

print(a)

first_random_idx_of_a_1 = random.randint(0,2)
second_random_idx_of_a_1 = random.randint(0,2)

first_random_idx_of_a_2 = random.randint(0,2)
second_random_idx_of_a_2 = random.randint(0,2)

temp = a[first_random_idx_of_a_1][second_random_idx_of_a_1]
a[first_random_idx_of_a_1][second_random_idx_of_a_1] = a[first_random_idx_of_a_2][second_random_idx_of_a_2]
a[first_random_idx_of_a_2][second_random_idx_of_a_2] = temp

print(a)