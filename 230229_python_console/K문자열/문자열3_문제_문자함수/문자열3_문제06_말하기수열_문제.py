'''
    [문제]
    	다음은 읽고, 말하기 수열의 규칙이다.
  
  		1, 11, 12, 1121, 122111, 112213
  
	 	첫번째 수열 : 1
	 	두번째 수열 : 1이 1개 = 11
	 	세번째 수열 : 1이 2개 = 12
	 	네번째 수열 : 1이 1개, 2가 1개 = 1121
	 	다섯번째 수열 : 1이 2개, 2가 1개, 1이 1개 = 122111
	 	여섯번재 수열 : 1이 1개, 2가 2개, 1이 3개 = 112213
'''

a = "1"

for turns in range(5):
	temp = a
	a = ""
	count = 1

	for idx in range(len(temp)-1):
		if temp[idx] == temp[idx+1]:
			count += 1
		else:
			a += temp[idx]
			a += str(count)
			count = 1
	a += temp[len(temp) - 1]
	a += str(count)
	print("temp:",temp)
	print("a:",a)