'''
	[문제]
		철수는 도서관에서 책을 한 권 빌렸다. 
		빌린 날짜는 작년 10월 10일이고, 대여 일수는 20일이다. 
		도서가 연체되면 연체 비용은 하루에 100원이다.
		오늘은 2월 25일 이라고 할 때, 지급해야 하는 비용은 얼마인지 구하시오.
		또한 작년 1월1일이 월요일이라고하면, 오늘은 무슨 요일인지 구하시오.
		단, 윤년은 계산하지 않는다.
	[정답]
		11800
'''
monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 			 1월 2월 3월 4월 5월 6월 7월 8월 9월 10월 11월 12월

rentdate = [10,10]
today = [2,25]

last_year = 2022
this_year = 2023 

rule = 20

money = 100

# 총 연체날짜 구하기
total_date = 0

if this_year - last_year >= 2:
	total_date += (this_year - last_year - 1)*365
	total_date += monthList[rentdate[0]-1] - rentdate[1]

	for i in range(rentdate[0], len(monthList)):
		total_date += monthList[i]

else:
	total_date += monthList[rentdate[0]-1] - rentdate[1]

	for i in range(rentdate[0], len(monthList)):
		total_date += monthList[i]

for i in range(today[0]-1):
	total_date += monthList[i]

total_date += today[1]

print("총 연체날짜는",total_date, "일")
print("총 연체비용은",(total_date - rule)*money, "원")

# 요일 구하기

day = 365 + 31 + 25 

if day%7 == 0:
	요일 = "일요일"
if day%7 == 1:
	요일 = "월요일"
if day%7 == 2:
	요일 = "화요일"
if day%7 == 3:
	요일 = "수요일"
if day%7 == 4:
	요일 = "목요일"
if day%7 == 5:
	요일 = "금요일"
if day%7 == 6:
	요일 = "토요일"

print(요일)