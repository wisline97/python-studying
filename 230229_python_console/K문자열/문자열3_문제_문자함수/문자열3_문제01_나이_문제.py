'''
    [문제]
        아래 주민번호를 가진 사람의 
        나이와 성별을 구하시오.
    [정답]
        35세
        남성
'''
jumin = "870612-1012940"
age = 2023 - int("19"+jumin[:2]) - 1
gender = int(jumin[7:8])
if gender == 1:
    gender = "남성"
else:
    gender = "여성"
print(age,gender)