'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~100)숫자 하나를 저장 후,
        랜덤 값보다 작은 값은 전부 a리스트에서 삭제하시오.
    [정답]

'''
import random

a = [10, 20, 30, 40, 50, 60]
num = random.randint(1,100)
print(num)
a_idx = 0
for i in range(len(a)):
    if a[a_idx] < num:
        a.remove(a[a_idx])
        a_idx -= 1
    a_idx += 1

print(a)