'''
    [문제]
        철수네 반은 체육대회를 준비하고 있다. 
		달리기 리스트는 달리기 대회에 참가하는 학생들이다. 
		배구 리스트는 배구 대회에 참가하는 학생들이다.
		둘 중 하나만 참가하는 학생들을 c리스트에 저장하시오.
	[정답]
		c = ['김철수', '신민아', '최재식', '이진상', '소지석', '유재석', '이민자', '박명수', '유명새', '킬리만자로']
		
'''
달리기 = [
            ["김철수","이서영","최민식"],
            ["조춘자","김말숙","이진상"],
            ["유재석","박명수","킬리만자로"]
        ]
배구 = [
			["신민아","김말숙","최재식"],
			["최민식","이서영","소지석"],
			["이민자","유명새","조춘자"]
	    ]

c = []

for y_idx in range(len(달리기)):
	for x_idx in range(len(달리기[y_idx])):

		check = False
		for 배구_y_idx in range(len(배구)):
			for 배구_x_idx in range(len(배구[배구_y_idx])):
				if 달리기[y_idx][x_idx] == 배구[배구_y_idx][배구_x_idx]:
					check = True

		if not check:
			c.append(달리기[y_idx][x_idx])

		check = False
		for 달리기_y_idx in range(len(달리기)):
			for 달리기_x_idx in range(len(달리기[달리기_y_idx])):
				if 배구[y_idx][x_idx] == 달리기[달리기_y_idx][달리기_x_idx]:
					check = True

		if not check:
			c.append(배구[y_idx][x_idx])


print(c)