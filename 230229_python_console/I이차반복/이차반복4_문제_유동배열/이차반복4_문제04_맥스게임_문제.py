'''
  [문제]
    0~4 사이의 랜덤 숫자를 저장해 a리스트에서 그 위치의 값이
    최대값인지 검사한다.
    만약 최대값이면 그 위치의 값을 0으로 바꾸고,
    전부 0이되면 종료한다. 

    과정을 전부 출력하시오.
  [예]
      랜덤 : 3
      [11, 87, 42, 0, 24]

      랜덤 : 0
      [11, 87, 42, 0, 24]   <- 최대값이 아니므로 그대로 유지

      랜덤 : 1
      [11, 0, 42, 100, 24]

      ...
      
  '''

import random

a = [11, 87, 42, 100, 24]


while True:
    check = True
    num = random.randint(0,4)
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        if a[i] != 0:
            check = False
    if a[num] == max:
        print(max, a[num])
        print(a)
        a[num] = 0
    
    if check == True:
        break