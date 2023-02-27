'''
    [문제]
        아래 리스트는 시험 점수와 학생 이름이다.
        일등의 학생 이름을 출력해주는 함수를 만드시오.
    [정답]
        1등 학생 = 박민지
'''

name = ["이만수", "김철수", "박민지"]  
score = [54, 32, 92]

def get_first_score(score):
    max = 0
    max_idx = 0
    for idx in range(len(score)):
        if max < score[idx]:
            max = score[idx]
            max_idx = idx
    print("1등학생",name[max_idx])

get_first_score(score)