'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 9는 몬스터의 체력을 의미한다.
        철수의 공격력은 5이다.     
        랜덤으로 몬스터 중 하나를 선택해서 공격하고,
        이를 총 다섯 번 반복한다. 
        모든 몬스터를 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다. 
        또한 공격한 몬스터의 양쪽에게는 1의 대미지를 가하게 된다. 
        
'''
import random

monster = [9,7,8,6]
power = 5

for i in range(5):
    random_mnstr_idx = random.randint(0,3)

    if monster[random_mnstr_idx] - power > 0:
        monster[random_mnstr_idx] -= power
    else:
        monster[random_mnstr_idx] = 0
        
    if random_mnstr_idx - 1 > 0 and random_mnstr_idx + 1 < len(monster):
        monster[random_mnstr_idx-1] -= 1
        monster[random_mnstr_idx+1] -= 1

    elif random_mnstr_idx - 1 <= 0:
        monster[random_mnstr_idx+1] -= 1
    
    elif random_mnstr_idx + 1 >= len(monster):
        monster[random_mnstr_idx-1] -= 1 

    print(random_mnstr_idx,"번째 몬스터 공격")

for i in range(len(monster)):
    if monster[i] < 0:
        monster[i] = 0

print(monster)
