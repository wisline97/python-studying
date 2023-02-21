'''
	[문제]
        철수는 게임을 만들고 있다. 
        (1~6 사이의 랜덤 숫자)주사위를 던져
		해당 숫자만큼 캐릭터를 이동시킨다.
		단, 캐릭터는 외곽으로만 움직일 수 있다.
		두 바퀴를 돌고 게임을 끝내시오.
'''
""" 	[예시]
		옷 □ □ □ □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 2   
		□ □ □ 옷 □ 
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □  
		□ ■ ■ ■ 옷 
		□ ■ ■ ■ □  
		□ □ □ □ □  

		dice = 3   
		□ □ □ □ □  
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ 옷 □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 6
		옷 □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 5
		□ □ □ □ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 1
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ 옷
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ 옷 □ □

		dice = 4
		□ □ □ □ □
		□ ■ ■ ■ □
		옷 ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □

		dice = 4
		□ □ 옷 □ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ ■ ■ ■ □
		□ □ □ □ □ """

import random

game = [
    [ 0,  1,  2,  3, 4],
    [15, 99, 99, 99, 5],
    [14, 99, 99, 99, 6],
    [13, 99, 99, 99, 7],
    [12, 11, 10,  9, 8]
]

move_count = 0
player_y = 0
player_x = 0
circle = 0

for	draw_y in range(len(game)):
	for draw_x in range(len(game[draw_y])):
		if game[draw_y][draw_x] == 99:
			print("■",end=" ")
		elif draw_x != player_x or draw_y != player_y:
			print("□",end=" ")
		elif draw_x == player_x and draw_y == player_y:
			print("★", end=" ")
	print()

while True:
	dice = random.randint(1,6)
	print("=================================")
	print("주사위 굴리기!",dice)
	print("=================================")

	move_count += dice
	if move_count > 15:
		print()
		print("한 바퀴 통과!")
		print()
		circle += 1
	move_count %= 16

	for check_y in range(len(game)):
		for check_x in range(len(game[draw_y])):
			if game[check_y][check_x] == move_count:
				player_y = check_y
				player_x = check_x
				break

	for	draw_y in range(len(game)):
		for draw_x in range(len(game[draw_y])):
			if game[draw_y][draw_x] == 99:
				print("■",end=" ")
			elif draw_x != player_x or draw_y != player_y:
				print("□",end=" ")
			elif draw_x == player_x and draw_y == player_y:
				print("★", end=" ")
		print()

	if circle >= 2:
		break