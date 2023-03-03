'''
    [문제]
        member는 회원목록이다.
        item은 쇼핑몰 판매상품이다.
        order는 오늘 주문목록이다.
        회원별 아이템 주문개수를 출력하시오.
    [정답]
        이만수: 고래밥 3
        김철민: 고래밥 1 칸쵸 1
        이영희: 새우깡 2 칸쵸 1
'''

member  = "3001/이만수,3002/김철민,3003/이영희"
item    = "1001/고래밥,1002/새우깡,1003/칸쵸"
order   = "3001,1001/3001,1001/3003,1002/3002,1003/3001,1001/3003,1002/3003,1003/3002,1001"

member = member.split(",")
item = item.split(",")
order = order.split("/")

for idx in range(len(item)):
    item[idx] = item[idx].split("/")

for idx in range(len(order)):
    order[idx] = order[idx].split(",")

for idx in range(len(member)):
    member[idx] = member[idx].split("/")

order_cnt = []

for idx in range(len(member)):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for order_idx in range(len(order)):
        if member[idx][0] == order[order_idx][0]:
            if order[order_idx][1] == "1001":
                cnt1 += 1
            if order[order_idx][1] == "1002":
                cnt2 += 1
            if order[order_idx][1] == "1003":
                cnt3 += 1
    order_cnt.append([member[idx][1],"고래밥",cnt1,"새우깡",cnt2,"칸쵸",cnt3])

for idx in range(len(order_cnt)):
    print(order_cnt[idx])