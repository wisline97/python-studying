'''
   [문제]
      a 리스트에 있는 값들을 b에 저장하려고 한다. 
      a 리스트의 값을 뒤에서부터 두 개씩 저장하시오.
   [정답]
      b = [7,7,3,3,1,1]
'''

a = [1 ,3, 7]
b = [0, 0, 0, 0, 0, 0]

a_idx = len(a) - 1

cnt = 0

for i in range(len(b)):

   b[i] = a[a_idx]
   cnt += 1

   print(cnt)

   if cnt >= 2:
      cnt = 0
      a_idx -= 1
   

print(b)



