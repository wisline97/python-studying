'''
    [문제]
        1~10 사이의 숫자를 랜덤으로 2개 저장하고,
        작은 숫자부터 큰 숫자까지의 합을 출력하는 함수를 만드시오.
    [예시]
        5, 3 ==> 3 + 4 + 5 = 12
        2, 6 ==> 2 + 3 + 4 + 5 + 6 = 20
'''
import random

min = random.randint(1,9)
max = random.randint(min+1,10)

def get_min_to_max_total(min, max):
    print(min, max)
    total = 0
    for num in range(min,max+1):
        total += num
    print(total)

get_min_to_max_total(min,max)