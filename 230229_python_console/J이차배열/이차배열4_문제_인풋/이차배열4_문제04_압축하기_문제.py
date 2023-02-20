'''
    [문제]
        a리스트는 압축하기 전 데이터이다.
        다음데이터를 압축 하시오.
        
        압축 기준은 데이터와 개수로 저장한다.
        예를 들어 3이 연속으로 5개이므로
        b = [[3,5]]
        다시 5가 6개이므로
        b = [[3,5],[5,6]]
        위와 같이 마지막까지 반복하시오.  
    [정답]     
        [3, 5]
        [5, 6]
        [2, 1]
        [4, 1]
        [2, 2]
'''
a = [3,3,3,3,3,5,5,5,5,5,5,2,4,2,2,2,3,3,5]
b = []
cnt = 1
for a_idx in range(len(a)-1):
    if a[a_idx] == a[a_idx+1]:
        if a_idx == len(a)-2:
            cnt += 1
            b.append([a[a_idx], cnt])
        else:
            cnt += 1
    else:
        b.append([a[a_idx], cnt])
        cnt = 1

last = len(a) - 1
if a[last] != a[last-1]:
    b.append([a[last], cnt])

print(b)