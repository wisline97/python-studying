'''
    [문제]
        arr리스트의 값을 체크하여
        짝수의 개수를 출력하는 함수를 만드시오.
    [정답]
        2
'''
arr = [2, 45, 1, 12]

def check_even(arr):
    count = 0
    for idx in range(len(arr)):
        if arr[idx] % 2 == 0:
            count += 1
    print(count,"개")

check_even(arr)