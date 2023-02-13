'''
	[문제]
		아래 배열은 3명의 학생 데이터이다.		
		각 학생은 3개씩 데이터로 표현한다. 
		맨 앞은 번호, 그다음은 국어점수, 그다음은 수학점수이다.					
		(예) 
			1001번, 국어 100, 수학 20
			1002번, 국어 32,  수학 54
			1003번  국어 34,  수학 65	

		[1] 전체 평균을 출력하시오.
		[2] 국어 1등 학생을 출력하시오.
		[3] 수학 1등 학생을 출력하시오.
		[4] 전체 1등 학생을 출력하시오.
'''

a = [1001, 100, 20, 1002, 32, 54, 1003, 34, 65]

i = 0
total = 0

while i<len(a):
	if i%3 != 0:
		total += a[i]
	i += 1

print("[1] 평균", total//6,"점")

lang_max = 0
lang_idx = 0
math_max = 0
math_idx = 0

total_first_std = 0
total_first_idx = 0
total = 0

for i in range(len(a)):
	total = 0
	if i%3 == 1:
		if a[i] > lang_max:
			lang_max = a[i]
			lang_idx = i
			total += a[i]
			total += a[i+1]
			if total_first_std < total:
				total_first_std = total
				total_first_idx = i
	if i%3 == 2:
		if a[i] > math_max:
			math_max = a[i]
			math_idx = i

print("[2]",a[lang_idx-1],"번 학생 국어",a[lang_idx],"점")
print("[3]",a[math_idx-2],"번 학생 수학",a[math_idx],"점")
print("[4]",a[total_first_idx-1],"번")