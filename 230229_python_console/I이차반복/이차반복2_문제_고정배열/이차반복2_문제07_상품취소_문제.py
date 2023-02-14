'''
	[문제]
		item리스트는 쇼핑몰 아이템 번호이다.
		count리스트는 오늘 판매된 아이템 개수를 적는 장부이다. 
		cancle리스트는 오늘 취소된 아이템 번호이다.

		오늘 취소된 개수만큼 count리스트의 값을 감소시키시오.
	[예시]
		1002: count = [   3,    1,    1,    4,    2,    1]
		1003: count = [   3,    1,    0,    4,    2,    1]
		1004: count = [   3,    1,    0,    3,    2,    1]
		1001: count = [   2,    1,    0,    3,    2,    1]
		1001: count = [   1,    1,    0,    3,    2,    1]
	[정답]
		[1, 1, 0, 3, 2, 1]
'''
item =  [1001, 1002, 1003, 1004, 1005, 1006]
count = [   3,    2,    1,    4,    2,    1]

cancle = [1002, 1003, 1004, 1001, 1001]

for i in range(len(cancle)):
	cancle_item = cancle[i]
	for y in range(len(item)):
		if item[y] == cancle_item:
			idx = y
			count[y] -= 1
	print(item[idx],":",count[idx])

print(count)