"""
[문제]
	[가위 바위 보 게임]
		1. player1 은 가위 바위 보중 하나를 입력받는다. 
		2. com 은 랜덤으로 가위 바위 보를 고른다. 
		3. 결과를 출력한다.
"""
import random

def get_player1():
    player1 = int(input())
    return player1

def get_com():
	com = random.randint(0,2)
	return com

# 0 가위 1 바위 2 보

def game():
    player1 = get_player1()
    com = get_com()
    print(player1, com)

    if player1 == com:
        print("비겼습니다.")

    elif player1 == 0 and com == 1:
        print("컴퓨터가 이겼습니다.")
    elif player1 == 0 and com == 2:
        print("당신이 이겼습니다.")

    elif player1 == 1 and com == 0:
        print("당신이 이겼습니다.")
    elif player1 == 1 and com == 2:
        print("컴퓨터가 이겼습니다.")

    elif player1 == 2 and com == 0:
        print("컴퓨터가 이겼습니다.")
    elif player1 == 2 and com == 1:
        print("당신이 이겼습니다.")
         

game()