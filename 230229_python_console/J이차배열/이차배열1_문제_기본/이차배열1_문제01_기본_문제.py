import random

'''
    [문제1]
        a리스트를 한 줄당 3개씩 3줄 총 9개로 이차원으로 만들고, 
        랜덤값(1~100)을 9개 저장하시오.
    [예시1]
        [56, 64, 10] 
        [100, 40, 12]
        [9, 70, 29] 
'''

print("[문제1]")
a = []

for turn in range(3):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    num3 = random.randint(1,100)
    a.append([num1, num2, num3])

print(a)

'''         
    [문제2]
        a리스트값들 중 50이상을 전부 출력하시오.
    [예시2] 
        56 64 100 70
'''

print("[문제2]")

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a[first_idx_of_a])):
        if a[first_idx_of_a][second_idx_of_a] >= 50:
            print(a[first_idx_of_a][second_idx_of_a], end=" ")

print()

'''
    [문제3]
        a리스트값들 중 4의 배수만 출력하시오.
    [예시3]
        56 64 100 40 12
'''
print("[문제3]")

check = False

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a[first_idx_of_a])):
        if a[first_idx_of_a][second_idx_of_a] % 4 == 0:
            check = True
            print(a[first_idx_of_a][second_idx_of_a], end=" ")

if not check:
    print("4의 배수 없음")

print()

'''        
    [문제4]
         a리스트값들 중 50이상인 수의 합을 출력하시오.
    [예시4]
        total = 290
'''
print("[문제4]")

total = 0

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a[first_idx_of_a])):
        if a[first_idx_of_a][second_idx_of_a] >= 50:
            total += a[first_idx_of_a][second_idx_of_a]

print(total)

'''
    [문제5]
         a리스트값들 중 50이상인 수의 개수를 출력하시오.
    [예시5]
        count = 4
'''
print("[문제5]")

count = 0

for first_idx_of_a in range(len(a)):
    for second_idx_of_a in range(len(a[first_idx_of_a])):
        if a[first_idx_of_a][second_idx_of_a] >= 50:
            count += 1

print(count)








