'''
    [문제]
        아래 리스트는 철수가 소지한 현금 개수이다.
        money는 돈 단위를 뜻하고,
        count는 단위별 개수를 뜻한다. 

        거스름돈은 7800일 때, 
        단위별로 나눠주고, 
        count리스트 값을 조정 후 출력하시오. 
    [정답]
        count = [1, 1, 0, 0, 2, 7]
'''
money = [50000, 10000, 5000, 1000, 500, 100]
count = [    1,     1,    1,    1,   5,  10]

charge = 7800
idx = 0

# charge = charge % money[idx]를 먼저 작성하고
# count[idx] 값을 조정해서 오류났던거 ^^....
while charge >= 0:
    if charge > money[idx]:
        if count[idx] - (charge//money[idx]) >= 0:
            print("charge =",charge)
            print("charge//money[",idx,"] =",charge//money[idx])
            print("count[",idx,"] =",count[idx])
            diff = count[idx] - (charge//money[idx])
            charge = charge % money[idx]
            count[idx] = diff
            print("count[",idx,"] =",count[idx])
            print("charge =",charge)
        else:
            print("charge =",charge)
            print("charge//money[",idx,"] =",charge//money[idx])
            print("count[",idx,"] =",count[idx])
            charge -= money[idx] * count[idx]
            count[idx] = 0
            idx += 1
            print("charge =",charge)
    else:
        idx += 1
    print()
    if charge == 0:
        break

    
print(count)