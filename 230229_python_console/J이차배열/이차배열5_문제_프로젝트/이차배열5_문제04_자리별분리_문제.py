'''
	[문제]
		랜덤으로 10000 ~ 99999 사이의 랜덤숫자를 저장하고 
		다음 규칙에 따라 결과를 출력하시오.
		랜덤숫자를 두 개로 분리하는데
		한 자리씩 늘리면서 분리한다. 
		각 분리한 숫자의 합을 출력한다.
	[예시]
		r = 34567
	[결과]
		3 + 4567
		34 + 567
		345 + 67
		3456 + 7
'''
import random

random_number = str(random.randint(10000,99999))
print("랜덤숫자는 :",random_number)
front_nums = ""
total = []
for turns1 in range(len(random_number)-1):
	back_nums = ""
	front_nums += random_number[turns1]
	
	for turns2 in range(turns1+1, len(random_number)):
		back_nums += random_number[turns2]

	total_unit = int(front_nums) + int(back_nums)
	print(front_nums,"+", back_nums,"=",total_unit)
	total.append(total_unit)

print(total)