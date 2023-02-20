'''
	[문제]
		랜덤으로 (1~4)를 저장하고
		아래와 같은 경우로 리스트에 저장하시오.
	[예]
		[1 번 선택시] 
		123
		654
		789
		
		[2 번 선택시]
		761
		852
		943
		
		[3번 선택시]		
		987
		456
		321
		
		[4번 선택시]	
		349
		258
		167
'''
import random

# num = random.randint(1,4)
num = 4
snake = []

for i in range(3):
    snake.append([0,0,0])

if num == 1:
    number = 1
    for y in range(len(snake)):
        if y % 2 == 0:
            for x in range(len(snake[y])):
                snake[y][x] = number
                number += 1
        else:
            for x in reversed(range(len(snake[y]))):
                snake[y][x] = number
                number += 1

elif num == 2:
    number = 1
    for x in reversed(range(len(snake))):
        if x % 2 == 0:
            for y in range(len(snake)):
                snake[y][x] = number
                number += 1
        else:
            for y in reversed(range(len(snake))):
                snake[y][x] = number
                number += 1

elif num == 3:
    number = 1
    for y in reversed(range(len(snake))):
        if y % 2 == 0:
            for x in reversed(range(len(snake[y]))):
                snake[y][x] = number
                number += 1
        else:
            for x in range(len(snake[y])):
                snake[y][x] = number
                number += 1

elif num == 4:
    number = 1
    for x in range(len(snake)):
        if x % 2 == 0:
            for y in reversed(range(len(snake))):
                snake[y][x] = number
                number += 1
        else:
            for y in range(len(snake)):
                snake[y][x] = number
                number += 1

for i in range(len(snake)):
    print(snake[i])