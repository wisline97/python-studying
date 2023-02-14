'''
	[문제]
		item리스트는 쇼핑몰 아이템 번호들이다.
		count리스트는 오늘 판매된 아이템 개수를 적는 장부이다. 
		purchase리스트는 오늘 판매된 아이템 번호이다.
  
		오늘 판매된 개수만큼 count리스트의 값을 증가시키시오.
  
	[예시]
		1002 : count = [   0,    1,    0,    0,    0,    0]
  		1003 : count = [   0,    1,    1,    0,    0,    0]
		1004 : count = [   0,    1,    1,    1,    0,    0]
		1001 : count = [   1,    1,    1,    1,    0,    0]
		1001 : count = [   2,    1,    1,    1,    0,    0]
	[정답]
		[2, 1, 1, 1, 0, 0]
'''

item =  [1001, 1002, 1003, 1004, 1005, 1006]
count = [   0,    0,    0,    0,    0,    0]

purchase = [1002, 1003, 1004, 1001, 1001]

for i in range(len(purchase)):
	sold_item = purchase[i]
	for y in range(len(item)):
		if item[y] == sold_item:
			idx = y
			count[y] += 1
	print(item[idx],":",count[idx])

print(count)