'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~70)숫자 하나를 저장 후,
        a리스트의 값들 사이에 저장하려고 한다. 
        저장조건은 a리스트의 바로 앞의 값 보다는 크고 
        바로 뒤의 값 보다는 이하인 위치에 삽입 후 출력하시오.
    [예시]
        r = 54
        a = [10,20,30,40,50,54,60]

'''
import random

a = [10, 20, 30, 40, 50, 60]

num = random.randint(1,70)
print("랜덤숫자는",num)

a.append(num)
print(a)

index = 0

check = False
for i in range(len(a)-1):
    if num > 60:
        index = len(a)
        print("num의 위치는",index)
        check = True
        break
    if a[i] < num and num < a[i+1] or a[i] == num :
        index = i+1
        print("num의 위치는",index)
        check = False

if check == False:
    a_last_idx = len(a) - 1
    while a_last_idx > index: 
        a[a_last_idx] = a[a_last_idx-1] 
        a_last_idx -= 1
    check = True

a[index] = num

if check == True:
    print(a)