'''
    [문제]
        lotto리스트가 당첨인지 꽝인지 체크하는 함수를 만드시오.
        단, 7이 연속으로 3개이면 당첨이다.
    [정답]
        당첨
'''

lotto = [1, 7, 1, 7, 7, 7, 7]

def lotto_win_check(lotto):
    for idx in range(len(lotto)-2):
        cnt = 0
        for count in range(3):
            if lotto[idx+count] == 7:
                cnt += 1
        if cnt == 3:
            print("당첨입니다.")
            break
    if cnt != 3:
        print("꽝!")

lotto_win_check(lotto)