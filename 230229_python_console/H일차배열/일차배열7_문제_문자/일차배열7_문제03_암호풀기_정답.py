'''
    [문제]
        철수는 비밀번호는 아래와 같다. 
        철수는 비밀번호를 보호하기 위해 비밀번호 글자 사이사이에 
        알파벳을 a부터 순서대로 끼워 넣었다.
        이제 철수는 원래 비밀번호로 다시 변환해야 한다.
        암호화된 비밀번호를 원래대로 복구하시오.
    [정답]
        qwer1234
'''
password = "qawbecrd1e2f3g4h"

temp = ""
for i in range(len(password)):
    if i % 2 == 0:
        temp += password[i]
password = temp
print(password)