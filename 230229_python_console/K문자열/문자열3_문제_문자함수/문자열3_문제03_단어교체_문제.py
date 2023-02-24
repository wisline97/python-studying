'''     
    [문제]
        text변수의 내용을 변경하려 한다.
        change변수의 앞부분은 교체할 단어이고, 뒷부분은 삽입할 단어이다.
        text변수의 내용을 변경하시오.
    [정답]
        text = "Life is too short." (변경 전)          
        text = "Life is too long."  (변경 후)
'''
text = "Life is too short."
change = "short,long"

changeList = change.split(",")
print("교체할 단어 =", changeList[0])
print("삽입할 단어 =", changeList[1])

교체단어 = changeList[0]

check = -1

turns = len(text) - len(changeList[0]) + 1

for text_idx in range(turns):
    count = 0
    for change_idx in range(len(교체단어)):
        if text[text_idx+change_idx] == 교체단어[change_idx]:
            count += 1
    if count == 5:
        check = text_idx
        break

if check != -1:
    front = text[:check]
    end = text[check+len(교체단어):]
    answer = front + changeList[1] + end
    print(answer)
else:
    print("교체 가능한 단어가 없습니다.")