'''
    [문제]
        랜덤(1~4)를 저장한다. 랜덤숫자는 회전 횟수이다. 
        회전 횟수만큼 block의 숫자들을 90도로 우회전시키시오.
        
    [예시]
        rNum = 4
        1 2 3 
        4 5 6 
        7 8 9 

        7 4 1 
        8 5 2 
        9 6 3 

        9 8 7 
        6 5 4 
        3 2 1 

        3 6 9 
        2 5 8 
        1 4 7
'''
import random

block = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

random_number = random.randint(1,4)
print(random_number)

for turns in range(random_number):
    for x in range(3):
        print(block[x])
    print()

    temp = []

    for block_x in range(3):
        temp_element = []
        for block_y in reversed(range(3)):
            temp_element.append(block[block_y][block_x])
        temp.append(temp_element)

    for block_y in range(3):
        for block_x in range(3):
            block[block_y][block_x] = temp[block_y][block_x]