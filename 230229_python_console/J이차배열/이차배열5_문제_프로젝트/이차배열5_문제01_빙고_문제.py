'''
    [문제]
        철수는 빙고 게임을 만들고 있다.
        빙고 조건은 가로 1이 3개 또는 세로 1이 3개 또는 대각선으로 1이 3개이면 빙고이다.
        빙고는 중첩될 수 있다.
        반복적으로 랜덤 위치에 1을 저장한다. 
        단, 한번 1이 저장된 곳은 또 다시 저장할 수 없다.
        3빙고가 성립되면 종료한다. 
'''
import random

bingo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# bingo_cnt를 반복문안에 집어넣으면 카운트가 중복으로 더해지는 오류 체크를 안해줘도 된다.

while True:
    bingo_cnt = 0

    random_y_idx = random.randint(0,2)
    random_x_idx = random.randint(0,2)

    if bingo[random_y_idx][random_x_idx] == 1:
        continue

    bingo[random_y_idx][random_x_idx] = 1

    # 빙고 가로 체크
    for bingo_y_idx in range(len(bingo)):
        x_bingo_check = True

        for bingo_x_idx in range(len(bingo[bingo_y_idx])):
            if bingo[bingo_y_idx][bingo_x_idx] != 1:
                x_bingo_check = False

        if x_bingo_check:
            bingo_cnt += 1

    # 빙고 세로 체크
    for bingo_x_idx in range(len(bingo)):
        y_bingo_check = True

        for bingo_y_idx in range(len(bingo[bingo_x_idx])):
            if bingo[bingo_y_idx][bingo_x_idx] != 1:
                y_bingo_check = False

        if y_bingo_check:
            bingo_cnt += 1

    # 빙고 대각선 체크
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
            bingo_cnt += 1

    if bingo[0][2] and bingo[1][1] and bingo[2][0]:
            bingo_cnt += 1

    print(bingo_cnt)
    for i in range(len(bingo)):
        print(bingo[i])
    print()

    if bingo_cnt > 3:
        break