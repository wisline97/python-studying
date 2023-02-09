'''
	[문제]
		아래 candy 리스트는 각 병에 들어있는 사탕의 양이다. 
		사탕의 종류는 전부 다르고, 한 사람 당 한 병에서 25개씩 나눠주려 한다.
		나눠 줄 수 있는 사람 수를 count 리스트에 저장하고, 나머지는 뒤로 넘겨준다.
		나눠주고 남은 사탕은 뒤로 넘겨서 합쳐서 나눠주시오.
		전부 나눠주고 난 candy와 count를 출력하시오. 
	
	[예시]
		(1) 80 : 75 개를 3명에게 나눠주고 5개 남는다. 뒤로 넘겨서 53은 58이 된다.
		(2) 58 : 50 개를 2명에게 나눠주고 8개 남는다. 뒤로 넘겨서 46은 54가 된다.
		(3) 54 : 50 개를 2명에게 나눠주고 4개 남는다. 뒤로 넘겨서 23는 27이 된다.
		(4) 27 : 25 개를 1명에게 나눠주고 2이 남는다. 
  
	[정답]
		candy = [0, 0, 0, 2]
		count = [3, 2, 2, 1]
'''

candy = [80,53,46,23]
count =[]
print("candy : " , candy)
print("count : " , count)

for i in range(len(candy)):
	person = candy[i] // 25
	count.append(person)
	if i < len(candy) - 1:
		candy[i + 1] += candy[i] % 25
		candy[i] = 0
	else:
		candy[i] = candy[i] % 25
print(candy)
print(count)





