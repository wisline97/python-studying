'''
    [문제]
         
        [5,9,0] : 은 5 + 9 이다 total = [14]
        [3,7,1] : 은 3 - 7 이다 total = [14, -4]
        [8,4,2] : 는 8 * 4 이다 total = [14, -4, 32]
        ...
        ...
    [정답]
        [14, -4, 32, 18, -2]
'''
game = [
    [5,9,0],
    [3,7,1],
    [8,4,2],
    [9,2,2],
    [4,6,1],
]
total = []

for idx in range(len(game)):
    answer = 0
    for nums in range(len(game[idx])):
        if game[idx][2] == 0:
            answer = game[idx][0] + game[idx][1]
        elif game[idx][2] == 1:
            answer = game[idx][0] - game[idx][1]
        elif game[idx][2] == 2:
            answer = game[idx][0] * game[idx][1]
    total.append(answer)

print(total)