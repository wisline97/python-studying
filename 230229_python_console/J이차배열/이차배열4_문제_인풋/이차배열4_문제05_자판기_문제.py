'''
    [문제]
        철수는 편의점에서 아르바이트하고 있다. 
        vending은 음료수 냉장고 물품 개수 상태이다.
        숫자는 아이템 번호이고 
        0은 비어있는 것을 뜻한다.

        냉장고는 최대 10개까지 저장할 수 있다.
        그리고 같은 종류의 아이템으로만 저장하며, 세로로 저장한다.
        box리스트는 현재 아이템 창고 재고를 표시한다.

        왼쪽숫자는 아이템번호이고 오른쪽 숫자는 개수이다.
        예를 들어 [1,4]는 1번 아이템을 뜻하고, 남은개수는 4개를 뜻한다.
        box에 있는 상품들로 채울 수 있을 만큼 채우고 최종상태를 출력하시오.
    [예시]
        1번 아이템은 4개 밖에 재고가 없다.
               
        [vending]
        [0,0,0,0,5,0],
        [0,0,0,0,5,0],
        [1,0,0,0,5,0],
        [1,0,0,0,5,6],
        [1,2,0,0,5,6],
        [1,2,3,0,5,6],
        [1,2,3,0,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
    
        [box]
        [1,0],
        [2,8],
        [3,3],
        [4,4],
        [5,8],
        [6,9]
        
        남은 아이템도 채워보자. 
    [정답]     
        [0, 2, 0, 0, 5, 6]
        [0, 2, 0, 0, 5, 6]
        [1, 2, 3, 0, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]

        [1, 0]
        [2, 4]
        [3, 0]
        [4, 0]
        [5, 8]
        [6, 6]
'''
vending = [
    [0,0,0,0,5,0],
    [0,0,0,0,5,0],
    [0,0,0,0,5,0],
    [0,0,0,0,5,6],
    [0,2,0,0,5,6],
    [0,2,3,0,5,6],
    [1,2,3,0,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],   
    [1,2,3,4,5,6],
]
box = [
    [1,4],
    [2,8],
    [3,3],
    [4,4],
    [5,8],
    [6,9],
]

vending_full_ivnt = len(vending) - 1
for turns in range(len(box)):
    box_item_no = box[turns][0]
    box_item_cnt = box[turns][1]
    print(turns+1,"횟수")
    print(box_item_cnt,"재고개수")

    # 아이템을 어디서부터 채울건지 확인하기 위해 현재 위치를 구함
    full_check = True

    for y_idx_vending in reversed(range(len(vending))):
        if vending[y_idx_vending][turns] == 0:
            location = y_idx_vending
            full_check = False
            print(location,"여기서부터 채워야함")
            break

    for draw in range(len(vending)):
        print(vending[draw])
    print()

    # 이미 꽉 채워져있으면 바로 다음 턴으로 넘어감
    if full_check:
        continue

    if (vending_full_ivnt-location)+box_item_cnt <= 10:
        for fill_ivnt in range(box_item_cnt):
            vending[location][turns] = box_item_no
            box[turns][1] -= 1
            location -= 1

    else:
        for fill_ivnt in range(10-(vending_full_ivnt-location)):
            vending[location][turns] = box_item_no
            box[turns][1] -= 1
            location -= 1

for draw in range(len(vending)):
    print(vending[draw])
print(box)