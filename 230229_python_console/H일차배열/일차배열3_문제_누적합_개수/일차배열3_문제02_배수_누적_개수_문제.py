'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 짝수만 출력하시오.
        [조건3] 짝수의 누적 합을 저장 후 출력하시오.
        [조건4] 짝수의 개수를 출력하시오.
    
    [예시]
        arr = [68, 81, 84, 72, 81]
        68
        84
        72

        개수 = 3
        합 = 224
'''

import random
a = []
total = 0
cnt = 0

for i in range(5):
    num = random.randint(1,100)
    a.append(num)
    if num % 2 == 0:
        print(num)
        total += num
        cnt += 1

print("합",total)
print("개수",cnt)
