'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        숫자8은 플레이어 위치를 뜻한다.
        숫자0은 플레이어가 움직일 수 있는 위치이다.
        
        order리스트는 플레이어가 움직이게 하는 명령어이다.
        1,2,3,4는 차례대로 북, 동, 남, 서를 뜻한다. 

        order의 이동대로 플레이어를 이동시키고 출력하시오.
        플레이어가 벽에 붙어서,
        더 이상 원하는 방향으로 이동할 수 없을 때는 "이동 불가"를 출력한다.
    [정답]        
        캐릭터의 현재 위치 = 2 , 2
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0 

        북
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0
        0 0 0 0 0

        남
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 8 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        남
        이동 불가
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0

        서
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        8 0 0 0 0

        동
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 8 0 0 0
'''

game = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,8,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

player_location = [2,2]

order = [1,3,3,3,4,3,3,4,2]

player_location_y = player_location[0]
player_location_x = player_location[1]

y_limit = len(game) - 1
x_limit = len(game[0]) - 1

# 1,2,3,4는 차례대로 북, 동, 남, 서
for turns in range(len(order)):
    print(player_location_y, player_location_x)
    game[player_location_y][player_location_x] = 0

    if order[turns] == 1:
        if player_location_y - 1 >= 0:
            player_location_y -= 1
        else:
            print("이동불가")
            continue
    elif order[turns] == 2:
        if player_location_x + 1 <= x_limit:
            player_location_x += 1
        else:
            print("이동불가")
            continue
    elif order[turns] == 3:
        if player_location_y + 1 <= y_limit:
            player_location_y += 1
        else:
            print("이동불가")
            continue
    else:
        if player_location_x - 1 >= 0:
            player_location_x -= 1
        else:
            print("이동불가")
            continue

    game[player_location_y][player_location_x] = 8
    print(player_location_y, player_location_x)
    for i in range(len(game)):
        print(game[i])
    print()

player_location[0] = player_location_y
player_location[1] = player_location_x