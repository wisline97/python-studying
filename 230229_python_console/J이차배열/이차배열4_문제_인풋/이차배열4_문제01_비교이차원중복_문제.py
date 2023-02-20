'''
    [문제]
        a리스트와 b리스트를 비교해서 
        서로 겹치는 값을 0으로 변경하시오.
        중복되는 값은 전부 0으로 변경한다.
    [정답]
    a = [
            [0, 4, 0],
            [0, 0, 0],
            [0, 4, 0]
        ]
    b = [
            [0, 0, 0],
            [0, 0, 8],
            [6, 0, 0]
        ]
'''

a = [[1,4,3],[5,7,2],[5,4,1]]
b = [[5,3,2],[1,7,8],[6,5,1]]

for a_y_idx in range(len(a)):
    for a_x_idx in range(len(a)):
        for b_y_idx in range(len(b)):
            for b_x_idx in range(len(b)):
                if a[a_y_idx][a_x_idx] == b[b_y_idx][b_x_idx]:
                    a[a_y_idx][a_x_idx] = 0
                    b[b_y_idx][b_x_idx] = 0

print(a)
print(b)