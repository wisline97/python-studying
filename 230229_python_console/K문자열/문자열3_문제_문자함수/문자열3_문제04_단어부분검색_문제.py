'''
    [문제]
        a리스트는 단어들이 모여있는 리스트이다.
        search는 검색하고 싶은 단어이다.
        a리스트에서 해당 단어를 검색해서 출력하시오.
        단, 부분 검색도 되어야한다.
        
    [예시] 
        school, teacher, child
'''


a =["school", "teacher", "child","father", "love"]
answer = []
search = "ch"
for a_idx in range(len(a)):
    check = False
    for word_idx in range(len(a[a_idx])-1):
        count = 0
        for search_idx in range(len(search)):
            if a[a_idx][word_idx+search_idx] == search[search_idx]:
                count += 1
            else:
                count = 0
        if count == 2:
            answer.append(a[a_idx])

print(answer)