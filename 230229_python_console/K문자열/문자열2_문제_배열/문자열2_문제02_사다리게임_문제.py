'''
	[문제]
		1. 랜덤(0~4)를 하나를 선택한다. 
		2. 숫자0 을 만나면 그냥 아래로 내려간다.
		3. 숫자1 을 만나면 오른쪽으로 이동 후 내려간다.
		4. 숫자2 를 만나면 완쪽으로 이동 후 내려간다.
		5. 오늘의 메뉴를 출력하시오.
	[정답]
		r = 0, 된장찌개	
		r = 1, 돈까스
		r = 2, 떡라면
		r = 3, 짜장면
		r = 4, 쫄면
'''
import random
menu = ["떡라면", "돈까스","짜장면", "쫄면", "된장찌개"]
r = random.randint(0,4)
ladder= [
		[0,0,0,0,0],
		[1,2,0,1,2],
		[0,1,2,0,0],
		[0,0,1,2,0],
		[1,2,0,1,2],
		[0,1,2,0,0],
		[0,1,2,0,0],
		[0,0,1,2,0],
		[0,0,0,0,0]
	]
print(r)
ladder_x = r
ladder_y = 0
while ladder_y < len(ladder)-1:
	if ladder[ladder_y][ladder_x] == 1:
		ladder_x += 1
	elif ladder[ladder_y][ladder_x] == 2:
		ladder_x -= 1
	ladder_y += 1
answer = menu[ladder_x]
print(answer)