'''
    [문제]
        [1] 빈리스트를 만들고, 랜덤으로 숫자(1~5)를 저장하고, 그 숫자만큼 연속으로 추가하시오.
        [2] 위 규칙을 다섯 번 반복하여 이차원 리스트로 만들어보시오.
    [예시]
        [3, 3, 3]
        [4, 4, 4, 4]
        [2, 2]
        [4, 4, 4, 4]
        [4, 4, 4, 4]
'''
import random
a = []

for turns in range(5):
    num = random.randint(1,5)
    print(num)
    b = []
    for idx in range(num):
        b.append(num)
    a.append(b)
    print(a[turns])