'''
    [문제]
        omr 리스트의 값들은 이번 시험 정답이다.
        a는 철수의 답안지이다. 랜덤숫자(1~5) 열 개를 a에 추가 후,
        정답과 비교해서 철수의 점수를 출력. 
        한 문제당 10점이다. 
    [예시]
        omr  = [4, 3, 1, 5, 3, 2, 1, 4, 5, 3]
        철수 = [5, 2, 5, 5, 2, 1, 4, 4, 4, 1]
        성적 = 20
'''
import random

omr = [4,3,1,5,3,2,1,4,5,3]
a =[]
total = 0 
for i in range(10):
    num = random.randint(1,5)
    a.append(num)
    if num == omr[i]:
        total += 10

print("정답",omr)
print("내 답",a)
print("점수",total)
