'''
    [문제]
        [조건1] a, b 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] base 변수에 랜덤으로 1~100 사이의 숫자를 저장한다. 
        base 변수값보다 큰 값들을 전부 출력하시오.
    [예시]
        base = 54

        a = [7, 99, 40, 14, 45]
        b = [46, 56, 87, 7, 80]

        99
        56
        87
        80    
'''

import random

a = []
b = []

base = random.randint(1,100)
print("base -> ", base)

for i in range(20):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    a.append(num1)
    b.append(num2)
    if num1 > base:
        print(num1)
    if num2 > base:
        print(num2)

print(a)
print(b)