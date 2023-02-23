student = [
			["번호",  "이름",  "성별"],
			[1001,  "이만수",  "남" ],
			[1002,  "이영희",  "여" ],
			[1003,  "김민정",  "여" ],
			[1004,  "이철민",  "남" ],
			[1005,  "오만석",  "남" ],
			[1006,  "최이슬",  "여" ]
		]
		
score = [
			["번호", "국어", "수학"],
			[1001,      10,     20],
			[1002,      70,     30],
			[1003,      64,     65],
			[1004,      13,     87],
			[1005,      49,     80],
			[1006,      14,     90]
		]
'''
	[문제1] 
		여학생들 점수 총합과 남학생들의 점수 총합을 비교하고
		점수가 더 큰쪽을 출력하시오.
	[정답1]
		333
'''
girls_score_total = 0
boys_score_total = 0

for student_idx in range(1,len(student)):
	total = 0
	if student[student_idx][2] == "여":
		total = score[student_idx][1] + score[student_idx][2]
		girls_score_total += total
	else:
		total = score[student_idx][1] + score[student_idx][2]
		boys_score_total += total

if girls_score_total > boys_score_total:
    print("여학생들의 점수 총합이 더 큽니다.")
    print(girls_score_total)
else:
    print("남학생들의 점수 총합이 더 큽니다.")
    print(boys_score_total)

'''
	[문제2]
		평균이 60점이상이면 합격이다.
		합격생들 번호, 이름, 평균을 출력하시오.
	[정답2]
		1003 김민정 64.5
		1005 오만석 64.5
'''
print()
for student_idx in range(1,len(student)):
	total = score[student_idx][1] + score[student_idx][2]
	avg = round(total/2,2)
	if avg >= 60:
		print(student[student_idx][0],student[student_idx][1],avg)
print()
'''
	[문제3]
		국어점수가 수학점수 보다 큰 학생들 
		번호, 이름을 출력하시오.
	[정답3]
		1002 이영희
'''
for student_idx in range(1,len(student)):
	if score[student_idx][1] > score[student_idx][2]:
		print(student[student_idx][0],student[student_idx][1])
print()

'''
	[문제4]
		총점이 1등인 학생의 번호, 이름을 출력하시오.
		만약 여러명이면 전부 출력하시오.
	[정답4]
		1003 김민정
		1005 오만석
'''
max = 0
for student_idx in range(1,len(student)):
	total = score[student_idx][1] + score[student_idx][2]
	if max <= total:
		max = total

for student_idx in range(1,len(student)):
	total = score[student_idx][1] + score[student_idx][2]
	if max == total:
		print(student[student_idx][0],student[student_idx][1])