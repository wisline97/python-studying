'''
    [문제]
        철수는 영어단어 타자 게임을 만들고 있다.
        한 단어씩 출력하는데 그냥 출력하면 재미없기 때문에 
        랜덤 위치에 글자 대신 * 을 한 개 출력한다.
        타자 게임을 구현을 위한 화면을 출력하시오.
    [예시]
        ja*a
        pytho*
        c+*
        n*de
        *avascript
'''
import random
wordList = ["java", "python", "c++", "node", "javascript"]

for idx in range(len(wordList)):
    num = random.randint(0,len(wordList[idx])-1)
    print("랜덤숫자는", num)
    temp = ""
    for str_idx in range(len(wordList[idx])):
        if str_idx == num:
            temp += "*"
        else:
            temp += wordList[idx][str_idx]
    print(temp)