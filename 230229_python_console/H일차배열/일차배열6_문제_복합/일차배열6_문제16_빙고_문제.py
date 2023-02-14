'''
    [문제]
        아래 a리스트는 3 x 3의 빙고 판을 표현한 것이다.
        1이 연속으로 3개이면, 빙고이다.
        즉 아래 빙고 판은 빙고가 2개이다.
        판정을 통해 빙고가 2개가 나오도록 식을 작성하시오.
'''
a = [0, 0, 1,
     0, 1, 1,
     1, 0, 1]

bingo = 0

# 가로 검사
i = 0
while i < len(a)-2:
    if a[i] == 1 and a[i+1] == 1 and a[i+2] == 1:
        bingo += 1
    i += 3

# 세로 검사
i = 0
while i < 3:
    if a[i] == 1 and a[i+3] == 1 and a[i+6] == 1:
        bingo += 1
    i += 1

# 대각선 검사
i = 0
while i < 3:
    if i == 0:
        if a[i] == 1 and a[i+4] == 1 and a[i+8] == 1:
            bingo += 1
    if i == 2:
        if a[i] == 1 and a[i+2] == 1 and a[i+4] == 1:
            bingo += 1
    i += 1

print(bingo)