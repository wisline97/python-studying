'''
	[문제]
		[1] a리스트의 값들을 순차적으로 검사한다. 
		[2] 연속으로 같은 값이 두 개가 있다면, 
		[3] 두 수를 삭제하고 그 합을 다시 그 자리에 저장한다.
		[4] 연속으로 같은 값이 없을 때까지 (1~3)을 반복한다.

		b = [8,4,2,2,8,4,4] 세번째 자리 2, 2가 연속이다.
		b = [8,4,4,8,4,4] , 두번째 자리 4, 4가 연속이다.
		b = [8,8,8,4,4] , 첫번째자리 8, 8 이 연속이다.
		b = [16,8,4,4] , 세번째자리 4, 4 이 연속이다.
		b = [16,8,8] , 두번째자리 8, 8 이 연속이다.
		b = [16,16] , 첫번째자리 16, 16 이 연속이다.
		b = [32] , 연속된 수가 없다. 
	[정답]
		b = [32, 0, 0, 0, 0, 0, 0]
'''
b = [8,4,2,2,4,4,8]
print(b)   


while True:
	is_consecutive = False
	# b[i] 와 b[i+1] 값을 항상 비교해야하니까 len(b)에서 1을 빼는 것 
	for i in range(len(b)-1):
		if b[i] == b[i+1]:
			is_consecutive = True
			total = b[i] + b[i+1]
			b[i:i+2] = [total]
			break

	if not is_consecutive:
		break

print(b)



""" while True:
    is_consecutive = False
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            is_consecutive = True
            total = b[i] + b[i+1]
            b[i:i+2] = [total]
            break
    print(b)
    if not is_consecutive:
        break
 """