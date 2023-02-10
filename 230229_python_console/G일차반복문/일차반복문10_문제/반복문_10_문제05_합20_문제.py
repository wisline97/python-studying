'''
    [문제]
        1~10 사이의 랜덤 숫자 3개 저장하고
        그 숫자의 합이 무조건 20이 되도록 출력해보자.
'''
import random

run = 1

while run == 1:
    print("==============================")
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    num3 = random.randint(1,10)

    print(num1, num2, num3)

    if num1 + num2 + num3 == 20:
        run = 0
        print("세 숫자의 합이 20입니다.")
        print("==============================")
        print(num1, num2, num3)
    else:
        print(num1, num2, num3, "의 합이 20이 아님")
        print("==============================")
        print("다시 랜덤 숫자 뽑기")
