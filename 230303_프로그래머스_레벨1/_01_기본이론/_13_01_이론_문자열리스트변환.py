"""
    sorted() 함수 는 문자열을 정렬해서 리스트로 반환해준다. 

"""
"""
     ''.join() 함수는 리스트를 다시 문자열로 변환해준다. 
"""

"""
[문제]
    118372 을 큰 숫자순서대로 내림차순으로 정렬하시오.
[정답]
    873211
"""

n = 118372

s1 = str(n) # 숫자를 문자로 변환
print(s1) # "118372"

s2 = sorted(s1)	#  soerted를 이용해서 각각을 잘라서 리스트로변환후 오름차순정렬 
print(s2) # ['1', '1', '2', '3', '7', '8']

s2.reverse() # 리스트를 반전시킨다. 

s3 = ''.join(s2) # 리스트를 문자열로 변환 

a = int(s3) # 정수로 변환
print(a) # 873211

