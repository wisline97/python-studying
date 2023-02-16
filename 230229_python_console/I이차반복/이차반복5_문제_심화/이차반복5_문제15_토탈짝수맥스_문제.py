'''
    [문제]
        [1] 1~50 사이의 랜덤 숫자 중 3의 배수 3개의 합을 total에 추가한다. 
        [2] 위 내용을 총 다섯 번 반복한다. 
        [3] 합이 가장 큰 수를 변수 max에 저장하시오.
    [예시]
        27 27 18 = 72
        30 24 15 = 69 
        6 12 45 = 63  
        45 27 48 = 120
        30 18 27 = 75 
        
        max = 120
'''
import random
max = 0
total = []

for turn in range(5):
    add = 0
    print(turn+1,"번째 턴")
    for pick_multiple in range(3):
        print("랜덤 3의 배수 뽑기")
        while True:
            num = random.randint(1,50)
            if num % 3 == 0:
                print(pick_multiple+1,"번째 3의 배수",num)
                break

        add += num
    print()
    if add > max:
        max = add
    total.append(add)
    print(total)

print("max =",max)