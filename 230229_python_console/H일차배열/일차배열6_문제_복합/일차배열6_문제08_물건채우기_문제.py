'''
	[문제] 
		철수는 편의점에서 아르바이트를 하고 있다. 
		오늘 장사가 잘돼서 라면이 많이 판매되었다.
		라면 진열장에 라면들이 전부 채워질 수 있도록 라면을 채워보자.
		
		라면 진열장은 한 칸에 최대 5개씩 진열할 수 있으며,
		재고는 6개 밖에 없고 앞에서부터 순차적으로 채워 넣는다. 
		재고를 다 채웠을 때 라면 진열장의 모습을 출력하시오.
	[정답] 
		list = [3,5,2,1,2]
		count = 6
  
		1번은 3이므로 2개를 추가해 ==> -2
		2번은 5이므로 0개를 추가해 ==> -0
		3번은 2이므로 3개를 추가해 ==> -3
		4번은 1이므로 4개를 추가해야되지만 재고가 1개밖에없어서 -1	
		최종으론 [5,5,5,2,2] 가된다. 
'''

list = [3, 5, 2, 1, 2]
count = 6

for i in range(len(list)):
	fill = 5 - list[i]
	if fill == 0:
		continue
	
	if count - fill > 0:
		list[i] += fill
		count -= fill
	elif count - fill <= 0:
		list[i] += count
		count -= count
	print(fill)

print(list)
