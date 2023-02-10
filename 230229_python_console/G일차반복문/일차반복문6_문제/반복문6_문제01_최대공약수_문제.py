'''
	[문제] 
		45와 60, 75의 최대공약수를 구하시오.
	[정답]
		15
'''

for i in reversed(range(1,76)):
	if 45%i == 0 and 60%i == 0 and 75%i == 0:
		print(i)
		break
