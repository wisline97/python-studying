'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        cancel은 주문취소 목록이다. 취소한회원아이디와 아이템이름 그리고, 주무개수가 기록되어있다.
        오늘의 매출을 출력하시오.
    [정답]
        7700
'''

member = "qwer1234,pythongood,testid"
item   = "사과,1100/바나나,2000/딸기,4300"
order  = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"
cancel = "qwer1234,딸기,5/phthongood,바나나,2"

item = item.split("/")
order = order.split("/")
cancel = cancel.split("/")

for idx in range(len(item)):
    item[idx] = item[idx].split(",")

for idx in range(len(order)):
    order[idx] = order[idx].split(",")

for idx in range(len(cancel)):
    cancel[idx] = cancel[idx].split(",")

print(item)
print(order)
print(cancel)

today_total = 0

for order_cnt in range(len(order)):
    if order[order_cnt][1] == "사과":
        today_total += int(item[0][1]) * int(order[order_cnt][2])
    if order[order_cnt][1] == "바나나":
        today_total += int(item[1][1]) * int(order[order_cnt][2])
    if order[order_cnt][1] == "딸기":
        today_total += int(item[2][1]) * int(order[order_cnt][2])

for cancel_cnt in range(len(cancel)):
    if cancel[cancel_cnt][1] == "사과":
        today_total -= int(item[0][1]) * int(cancel[cancel_cnt][2])
    if cancel[cancel_cnt][1] == "바나나":
        today_total -= int(item[1][1]) * int(cancel[cancel_cnt][2])
    if cancel[cancel_cnt][1] == "딸기":
        today_total -= int(item[2][1]) * int(cancel[cancel_cnt][2])


print(today_total)