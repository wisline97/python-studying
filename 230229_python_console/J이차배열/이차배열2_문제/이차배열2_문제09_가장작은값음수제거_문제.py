'''
    [문제]
        a리스트를 이차원으로 만들고 랜덤 값(-100~100)을 3개씩 3줄 총 9개를 만들고
        사각형모양 으로 출력한다.
        그 중에 가장 작은 값을 출력하시오.

        단, 음수는 양수로 변경해 비교하시오.
    [예시]
        [6,-12,90]
        [-98,45,18]
        [34,2, 10]
    
        가장 작은 값 = 2
'''
import random

a = []

for nums in range(3):
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    num3 = random.randint(-100,100)
    a.append([num1,num2,num3])

print(a)
print(abs(min(min(a))))

