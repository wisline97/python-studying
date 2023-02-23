'''
    [문제]
        철수는 게임을 만들고 있다.
        game리스트는 이차원으로 되어있다.
        game리스트 안에 block리스트의 숫자를 채워 넣는 게임이다.

        리스트의 값1은 block이 차 있는 것을 의미한다.
        리스트의 값0은 block이 비어있는 것을 의미한다.
    [조건1] 
        block은 이번에 제시된 모양이다. 
        block의 모양을 game 리스트에 넣을 수 있다면 채워 넣고,
        넣을 수 없다면 "gameover"를 출력하시오.
    [조건2]
        block을 채워 넣었을 때 가로로 1이 연속 5개이거나, 
        세로로 1이 연속 5개이면 그 줄은 전부 숫자 2로 변경하시오.
    [정답]

'''
game = [
    [0,1,0,1,0],
    [1,1,0,1,1],
    [0,1,1,1,1],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

block = [
    [0,1],
    [1,1]
]

for game_y in range(len(game)-1):
    for game_x in range(len(game[game_y])-1):
        if game[game_y][game_x] == 0 or game[game_y][game_x] == 1:
            if game[game_y][game_x+1] == 0 and game[game_y+1][game_x] == 0 and game[game_y+1][game_x+1] == 0:
                game[game_y][game_x+1] = 1
                game[game_y+1][game_x] = 1
                game[game_y+1][game_x+1] = 1
                break

for draw in range(len(game)):
    print(game[draw])

temp = []

for game_y in range(len(game)):
    unit = []
    for game_x in range(len(game[game_y])):
        unit.append(game[game_y][game_x])
    temp.append(unit)

# 가로검사

for game_y in range(len(game)):
    for game_x in range(len(game[game_y]) - (len(game[game_y])-1)):
        if game[game_y][game_x] == 1 and game[game_y][game_x+1] == 1 and game[game_y][game_x+2] == 1 and game[game_y][game_x+3] == 1 and game[game_y][game_x+4] == 1:
            temp[game_y][game_x] = 2
            temp[game_y][game_x+1] = 2
            temp[game_y][game_x+2] = 2
            temp[game_y][game_x+3] = 2
            temp[game_y][game_x+4] = 2

# 세로검사

for game_x in range(len(game[0])):
    for game_y in range(len(game) - (len(game)-1)):
        if game[game_y][game_x] == 1 and game[game_y+1][game_x] == 1 and game[game_y+2][game_x] == 1 and game[game_y+3][game_x] == 1 and game[game_y+4][game_x] == 1:
            temp[game_y][game_x] = 2
            temp[game_y+1][game_x] = 2
            temp[game_y+2][game_x] = 2
            temp[game_y+3][game_x] = 2
            temp[game_y+4][game_x] = 2

print()

for draw in range(len(temp)):
    print(temp[draw])