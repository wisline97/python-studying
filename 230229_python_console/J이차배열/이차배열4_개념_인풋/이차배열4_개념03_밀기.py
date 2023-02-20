'''
    [문제]
        랜덤으로 dir 리스트의 값을 d에 저장한다.
        d값의 방향으로 a리스트의 모든값이 한칸씩 이동한다.
        밀린값은 반대편으로 저장된다.

    [예시1]
        d = "북"
    [결과1]    
        [1004,1005,1006,1007],
        [1008,1009,1010,1011],
        [1000,1001,1002,1003],

    [예시2]
        d = "서"
    [결과2]
        [1001,1002,1003,1000],
        [1005,1006,1007,1004],
        [1009,1010,1011,1008],

'''
import random

dir = ["북" , "동" , "남" , "서"]
d = ""
a = [
    [1000,1001,1002,1003],
    [1004,1005,1006,1007],
    [1008,1009,1010,1011],
]

r = random.randint(0, len(dir)-1)
d = dir[r]
d = "동"

print(d)

if d == "북":
    temp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i + 1]
    a[-1] = temp

elif d == "동":
    for i in range(len(a)):
        temp = a[i][-1]   #[-1] => [len(a[i])-1] a[i]의 제일 마지막 값
        last = len(a[i])-1 # a[i]의 제일 마지막 값 == 3
        for j in range(len(a[i])-1): # a[i] 길이에서 1을 뺀 횟수만큼 반복 즉 3번 반복
            a[i][last] = a[i][last-1] # j가 0이고 last가 3일 때 a[i][3] = a[i][2], j가 1이고 last가 2일 때 a[i][2] = a[i][1], j가 2이고 last가 1일 때 a[i][1] = a[i][0]
            last -= 1   # last에서 3회에 걸쳐 1씩 뺌 즉 last가 1이 될 때까지 뺌                                                                                                                                               
        a[i][0] = temp

elif d == "남":
    temp = a[-1]
    last = len(a)-1
    for i in range(len(a)-1):
        a[last] = a[last -1]
        last -= 1
    a[0] = temp

elif d == "서":
    for i in range(len(a)):
        temp = a[i][0]
        for j in range(len(a[i])-1):
            a[i][j] = a[i][j + 1]           
        a[i][-1] = temp

for i in range(len(a)):
    print(a[i])

