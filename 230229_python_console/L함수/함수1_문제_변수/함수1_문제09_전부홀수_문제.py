'''
    [문제]
        리스트에 랜덤으로 -100 ~ 100 사이의 홀수 4개를 저장 후,
        전부 홀수인지 검사하는 함수를 만드시오.
    [예시]
        [-5, 99, -71, 27] 전부 홀수이다.
        [0, 22, -41, 21] 전부 홀수가 아니다.
'''
import random
a = []

def odd(a):
    even_check = False
    for turns in range(4):
        num = random.randint(-100,100)
        if num%2 == 0:
            even_check = True
        a.append(num)

    if even_check:
        print(a)
        print("전부 홀수가 아니다.")
    else:
        print(a)
        print("전부 홀수이다.")

odd(a)