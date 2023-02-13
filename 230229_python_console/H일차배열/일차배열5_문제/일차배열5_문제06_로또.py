'''
	[로또]	
		아래 lotto 리스트에 1~45숫자를 순차적으로 저장한다. 
		셔플후 그중 가장앞에서 6개를 출력한다. 
'''
import random

lotto = []

for i in range(1,46):
	lotto.append(i)

print(lotto)

for i in range(1000):
	num1 = random.randint(0,len(lotto)-1)
	num2 = random.randint(0,len(lotto)-1)

	temp = lotto[num1]
	lotto[num1] = lotto[num2]
	lotto[num2] = temp
print(lotto)

answer = []

for i in range(6):
	answer.append(lotto[i])

print(answer)