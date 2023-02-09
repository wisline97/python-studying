'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.  
        [조건1] 20 ~ 1까지 거꾸로 반복문을 실행한다.
        [조건2] 5 ~ 15 사이의 3의 배수일 때는 "안녕"을 출력한다.
        [조건3] 위의 조건을 제외하곤 전부 숫자를 출력한다. 
    [정답]
    20
    19
    18
    17
    16
    안녕
    14
    13
    안녕
    11
    10
    안녕
    8
    7
    안녕
    5
    4
    3
    2
    1
'''

for i in reversed(range(1,21)):
    if i>=5 and i<=15:
        if i%3==0:
            print("안녕")
        else:
            print(i)
    else:
        print(i)