'''
    [문제]
        regist 리스트는 수강신청을 신청한 학생명단이다.
        cancle 리스트는 수강철회를 신청한 학생명단이다.
        수강신청을 한 학생들을 last_regist 에 저장후 출력하시오.
'''

regist = ["김철민" ,"이민정" , "오사랑" , "최면술" , "김밥집" , "박대한" ,"조정민"]
cancle = ["이민정" , "최면술" , "조정민"]

last_regist = []

for regist_idx in range(len(regist)):
    check = False
    for cancle_idx in range(len(cancle)):
        if regist[regist_idx] == cancle[cancle_idx]:
            check = True
    if not check:
        last_regist.append(regist[regist_idx])

print(last_regist)