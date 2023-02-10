'''
[문제] 
	45와 60, 75의 최소공배수를 구하시오.
[정답]
	900
'''

for i in range(1,45*60*75):
	if i%45 == 0 and i%60 == 0 and i%75 == 0:
		print(i)
		break