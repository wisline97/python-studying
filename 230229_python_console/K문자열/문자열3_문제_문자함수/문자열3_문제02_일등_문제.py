'''
   [문제]
        text는 학생점수를 기록한 데이터이다.
        전체 평균과 일등의 점수를 출력하시오.
    [정답]
        평균 = 30.2
        일등 점수 = 80
'''
text = "13,32,80,3,23"
score = text.split(",")
print(score)

max = 0
total = 0
for idx in range(len(score)):
    if int(score[idx]) > max:
        max = int(score[idx])
    total += int(score[idx])

print("평균=",total/len(score))
print("일등점수=",max)