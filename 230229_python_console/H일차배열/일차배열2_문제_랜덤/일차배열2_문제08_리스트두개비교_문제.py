'''
    [문제]
        [조건1] 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] 둘 다 짝수이거나 "짝수" 출력, 둘 다 홀수이면 "홀수" 출력 , 
                한쪽은 홀수이고 다른 한쪽은 짝수이면 "다르다"를 출력하시오.
    [예시]
        a = [48, 71, 66, 85, 65]
        b = [99, 81, 75, 24, 40]
        다르다
        홀수
        다르다
        다르다
        다르다    
'''

import random

a = []
b = []

for i in range(5):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    a.append(num1)
    b.append(num2)
    if num1%2 == 0 and num2%2 == 0:
        print("짝수")
    elif num1%2 == 1 and num2%2 == 1:
        print("홀수")
    else:
        print("다르다")

print(a)
print(b)