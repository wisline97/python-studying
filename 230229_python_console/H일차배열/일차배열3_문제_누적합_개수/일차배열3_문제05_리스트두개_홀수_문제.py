'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 홀수의 합을 출력하시오. 
        a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [28, 79, 47, 70, 36]
        b = [63, 4, 45, 54, 87]
        total1 = 126
        total2 = 195
        195    
'''
import random

a = []
b = []

total1 = 0
total2 = 0

a_odd_total = 0

for i in range(5):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    a.append(num1)
    b.append(num2)
    total1 += num1
    if num2 % 2 == 1:
        total2 += num2
    if num1 % 2 == 1:
        a_odd_total += num1

print(a, total1)
print(b, total2)

if total2> a_odd_total:
    print(total2, "b 배열 홀수값들의 합이 더 크다")
elif total2 < a_odd_total:
    print(a_odd_total, "a 배열 홀수값들의 합이 더 크다")
else:
    print(total2, a_odd_total)
