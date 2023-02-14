'''
    [문제]
        문자열 hello를 olleh로 출력하시오.
'''
text = "hello"

for i in reversed(range(len(text))):
    print(text[i],end="")