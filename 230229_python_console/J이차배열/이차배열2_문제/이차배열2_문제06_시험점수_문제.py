'''
    student리스트는 이번 학기 중간고사 성적이다.
    가로 한 줄을 기준으로 맨 앞은 번호이고, 뒤에 숫자 3개는
    각각 국어, 수학, 영어 점수이다. 
'''
student = [
    [1001, 100, 20, 32],        # 152
    [1002, 40, 43, 12],         # 95
    [1003, 60, 21, 42],         # 123
    [1004, 76, 54, 55],         # 185
    [1005, 23, 11, 76],         # 110
]
rank = [0,0,0,0,0]

all_score = []

'''
    [문제1] 
        모든 점수의 총합을 출력하시오.
    [정답1] 
        665
'''
print("[문제1]")

for y in range(len(student)):
    total = 0
    for x in range(len(student[y])):
        if x != 0:
            total += student[y][x]
    print(student[y][0],"번 학생 점수 총합",total)
    all_score.append(total)

'''
    [문제2] 
        국어 1등 번호를 출력하시오.
    [정답2]         	
        1001
'''
print("[문제2]")

max_lang = 0
max_lang_idx = 0
for y in range(len(student)):
    if max_lang < student[y][1]:
        max_lang = student[y][1]
        max_lang_idx = y

print(student[max_lang_idx][0])

'''
    [문제3] 
        수학 1등 번호를 출력하시오.
    [정답3]    
        1004    
'''
print("[문제3]")
max_math = 0
max_math_idx = 0
for y in range(len(student)):
    if max_math < student[y][2]:
        max_math = student[y][2]
        max_math_idx = y

print(student[max_math_idx][0])

'''        	
    [문제4] 
        영어 1등 번호를 출력하시오.
    [정답4]
        1005
'''
print("[문제4]")
max_eng = 0
max_eng_idx = 0
for y in range(len(student)):
    if max_eng < student[y][3]:
        max_eng = student[y][3]
        max_eng_idx = y

print(student[max_eng_idx][0])


'''
    [문제5] 
        전체 1등 번호를 출력하시오.
    [정답5]
'''
print("[문제5]")

max_score = 0
max_score_idx = 0

for idx in range(len(all_score)):
    if max_score < all_score[idx]:
        max_score = all_score[idx]
        max_score_idx = idx

print(student[max_score_idx][0],"번 학생 점수 총합 =",max_score)

'''
    [문제6] 
        수학점수가 국어점수 보다 높은 번호를 출력하시오.
    [정답6]
        1001 1003 1004 1005
'''
print("[문제6]")

for i in range(len(student)):
    if student[i][2] > student[i][1]:
        print(student[i][0])

'''
    [문제7]
        세 과목의 총합의 등수를 rank리스트에 저장하시오.
    [정답7]
        [2, 5, 3, 1, 4]
'''
print("[문제7]")

for idx in range(len(all_score)):
    count = 0
    for i in range(len(all_score)):
        if all_score[idx] <= all_score[i]:
            count += 1
    rank[idx] = count

print(rank)

