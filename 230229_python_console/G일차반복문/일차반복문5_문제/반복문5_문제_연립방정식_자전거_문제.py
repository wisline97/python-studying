'''
	[문제]
		학교에서 집까지 갈 때 시속 15km로 자전거를 타고 가면, 
		시속 6km로 걸어가는 것보다 18분 일찍 도착한다고 한다.
		학교에서 집까지의 거리를 구하시오.
	[정답]
		3.0
'''

walk = 60/6
ride = 60/15

x = 0

while True:
	if (walk*x)-18 == ride*x:
		break
	else:
		x += 1

print(x,"km")