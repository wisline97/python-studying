'''
    [문제]
        1. 1~100까지 반복한다.
        2. 각 수에 3이나 6이나 9의 개수를 누적해서 출력하시오. 

        [예시]
            3 1
            6 1
            9 1
            13 1
            16 1
            ...
            98 1
            99 2
'''

for i in range(1,101):
    num_to_str = str(i)
    count = 0
    for y in range(len(num_to_str)):
        if int(num_to_str[y]) % 3 == 0 and int(num_to_str[y])!=0:
            count += 1
    print(i, count)