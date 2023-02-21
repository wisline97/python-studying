'''
    [문제]
        랜덤으로 dir 리스트의 값을 d에 저장한다. 
        랜덤으로 count 에 2~4를 저장한다.
        d값의 방향으로 a리스트의 모든값이 count 숫자만큼 이동한다. 
        밀린값은 반대편으로 저장된다.
        
    [예시1]
        d = "북" 
        count = 2
        
    [결과1]          
        [1008,1009,1010,1011],
        [1000,1001,1002,1003],
        [1004,1005,1006,1007],
        
    [예시2]
        d = "서"
        count = 3
    [결과2]
        [1003,1000,1001,1002],
        [1007,1004,1005,1006],
        [1011,1008,1009,1010],
    
'''
import random
dir = ["북" , "동" , "남" , "서"]
d = dir[random.randint(0,3)]
print("방향 :",d)
count = random.randint(2,4)
print("횟수 :",count)

a = [
    [1000,1001,1002,1003],
    [1004,1005,1006,1007],
    [1008,1009,1010,1011],
]

if d == "북":
    for turns in range(count):
        temp = a[0]

        for a_y_idx in range(len(a)-1):
            a[a_y_idx] = a[a_y_idx+1]

        a[len(a)-1] = temp

        for repeat in range(len(a)):
            print(a[repeat])
        print()

if d == "남":
    for turns in range(count):
        temp = a[len(a)-1]

        for a_y_idx in reversed(range(1,len(a))):
            a[a_y_idx] = a[a_y_idx-1]
            
        a[0] = temp

        for repeat in range(len(a)):
            print(a[repeat])
        print()

if d == "서":
    for turns in range(count):
        for a_y_idx in range(len(a)):
            temp = a[a_y_idx][0]

            for a_x_idx in range(len(a[a_y_idx])-1):
                a[a_y_idx][a_x_idx] = a[a_y_idx][a_x_idx+1]

            a[a_y_idx][len(a[a_y_idx])-1] = temp

        for repeat in range(len(a)):
            print(a[repeat])
        print()

if d == "동":
    for turns in range(count):
        for a_y_idx in range(len(a)):
            temp = a[a_y_idx][len(a[a_y_idx])-1]

            for a_x_idx in reversed(range(1, len(a[a_y_idx]))):
                a[a_y_idx][a_x_idx] = a[a_y_idx][a_x_idx-1]

            a[a_y_idx][0] = temp

        for repeat in range(len(a)):
            print(a[repeat])
        print()