'''
    [문제]
        a 와 b 의 각 자리의 합을 total에 저장하시오.
    [정답]
        [64, 49, 27, 24, 103]
'''

a = [10,43,23,12,53]
b = [54,6,4,12,50]

total = [0,0,0,0,0]

arr_length = len(total)

for i in range(arr_length):
    total[i] = a[i]+b[i]

print(total)
