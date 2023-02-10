'''
   [문제]
      1 ~ 9 사이의 랜덤 값을 4개 출력한다. 
      랜덤 값이 모두 홀수이면 "당첨"을 출력,
      하나라도 홀수가 아니면 "꽝" 출력한다.
      
      [예시] 
         3 1 5 1 : "당첨"
         5 2 1 4 : "꽝"
'''

import random


num1 = random.randint(1,9)
num2 = random.randint(1,9)
num3 = random.randint(1,9)
num4 = random.randint(1,9)

if num1%2 == 1 and num2%2 == 1 and num3%2 == 1 and num4%2 == 1 :
   print(num1, num2, num3, num4, "당첨")
else:
   print(num1, num2, num3, num4, "꽝")
