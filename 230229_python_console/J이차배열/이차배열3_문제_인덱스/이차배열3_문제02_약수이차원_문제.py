'''
    [문제]
        랜덤(2~100) 숫자를 저장해 그 수의 약수를 모두 리스트에 저장한다.
        위 규칙을 다섯 번 반복하여 이차원리스트를 만드시오.
    [정답]
        27 [1, 3, 9, 27]
        72 [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]
        76 [1, 2, 4, 19, 38, 76]
        94 [1, 2, 47, 94]
        91 [1, 7, 13, 91]  
'''
import random

a = []

for turns in range(5):
    num = random.randint(2,100)
    print(num)
    temp = []
    for nums in range(1,num+1):
        if num % nums == 0:
            temp.append(nums)
    print(temp)
    a.append(temp)

print(a)