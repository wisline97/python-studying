'''
	[문제] 	
		현재 택시는 5, 5 위치에 있다.
		배열의 왼쪽 세로줄은 속도를 뜻한다.
		배열의 오른쪽 세로줄은 방향을 뜻하고 (북, 동, 남, 서)를 뜻한다. 
		
		속도와 방향은 택시가 매번 이동한 내용을 기록한 것이다. 
		
		예) 속도는 4이고 방향은 북쪽을 뜻한다. 
			y가 4감소해  x : 5 , y : 9 가 된다.  
			
		6번 모두 이동한 후 택시의 위치를 출력하시오. 
	[정답]
		x : -1 y : 2
'''
arr = [
		[4,"북"],
		[2,"동"],
		[1,"남"],
		[5,"서"],
		[4,"서"],
		[1,"동"]
	]
x = 5
y = 5

for arr_idx in range(len(arr)):
	if arr[arr_idx][1] == "북":
		y -= arr[arr_idx][0]
	if arr[arr_idx][1] == "동":
		x += arr[arr_idx][0]
	if arr[arr_idx][1] == "남":
		y += arr[arr_idx][0]
	if arr[arr_idx][1] == "서":
		x -= arr[arr_idx][0]
	print(arr_idx+1,"번째", x,y)

print(x,y)