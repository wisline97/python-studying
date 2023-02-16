'''
	[문제]
		철수는 게임을 개발하고 있다.
		game리스트를 아래와 같이 사각형으로 출력한다.

		숫자8 은 현재 플레이어가 있는 자리이다.
		숫자0 은 플레이어가 이동할 수 있는 자리이다.
		숫자1 은 플레이어가 이동할 수 없는 벽이다.

		order리스트는 플레이어를 움직이기 위한 명령어들이다.
		숫자 1~4로 표현하고 북(1)동(2)남(3)서(4)를 뜻한다.

		order의 내용대로 플레이어가 이동하는 경로를 전부 출력하시오.
		벽 때문에 이동할 수 없을 때는 "이동 불가"를 출력하시오.
'''
game = [1,1,1,1,1,
	    1,0,0,0,1,
	    1,0,8,0,1,
	    1,0,0,0,1,
	    1,1,1,1,1]

order = [1,2,3,3,3,1,4,1]
player_location = 0

# 플레이어의 첫 위치 찾기
for location_of_player in range(len(game)):
    if game[location_of_player] == 8:
        player_location = location_of_player

print("현재 플레이어의 인덱스는",player_location,"입니다.")
print()

for i in range(len(order)):
    print(i+1,"번째 턴")
    direction = order[i]
    
    if direction == 1:
        print("북으로 1칸 이동")
        if game[player_location - 5] == 1:
            print("이동 불가")
        else:
            game[player_location] = 0
            player_location -= 5
            game[player_location] = 8

    if direction == 2:
        print("동으로 1칸 이동")
        if game[player_location + 1] == 1:
            print("이동 불가")
        else:
            game[player_location] = 0
            player_location += 1
            game[player_location] = 8

    if direction == 3:
        print("남으로 1칸 이동")
        if game[player_location + 5] == 1:
            print("이동 불가")
        else:
            game[player_location] = 0
            player_location += 5
            game[player_location] = 8

    if direction == 4:
        print("서로 1칸 이동")
        if game[player_location - 1] == 1:
            print("이동 불가")
        else:
            game[player_location] = 0
            player_location -= 1
            game[player_location] = 8

	# 이동경로 출력용
    game_idx = 0
    for rows in range(5):
        for columns in range(5):
            print(game[game_idx], end=" ")
            game_idx += 1
        print()        
    print()