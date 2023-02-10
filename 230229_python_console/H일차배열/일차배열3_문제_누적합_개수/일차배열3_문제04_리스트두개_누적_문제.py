'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 전체 합 중 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [93, 100, 41, 74, 45]
        b = [84, 80, 25, 19, 27]
        total1 = 353
        total2 = 235
        353
'''
import random

a = []
b = []

total1 = 0
total2 = 0
for i in range(5):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    a.append(num1)
    b.append(num2)
    total1 += num1
    total2 += num2

print(a)
print(b)

if total1 > total2:
    print(total1, a)
elif total1 < total2:
    print(total2, b)
else:
    print(total1,total2, a, b)