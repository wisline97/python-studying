'''
     [문제]
      1. 같은 숫자가 적혀있는 카드 2장씩 5세트가 있다. (총10장)
      2. front는 카드를 엎어놓은 상태를 뜻한다. 
      3. 먼저 front를 셔플한다. 
      4. front에 있는 카드 2개를 랜덤으로 선택한다. (마우스가 없으므로 인덱스로 선택)
      5. 선택한 카드 2장의 내용이 같으면 back에 복사해서 맞춘 걸 표시한다. 
         back에 모든 글자가 채워지면 게임은 종료된다.
         
      6. 같은 인덱스 선택할 수 없다. 
      7. 이미 선택한 자리를 또 선택할 수 없다. 
'''
import random

front = [10,10,20,20,30,30,40,40,50,50]
back = [0,0,0,0,0,0,0,0,0,0]
cnt = 0

for i in range(10000):
   num1 = random.randint(0,9)
   num2 = random.randint(0,9)

   temp = front[num1]
   front[num1] = front[num2]
   front[num2] = temp

print(front)

temp1 = 10000
temp2 = 10000

while True:
   print("0부터 9까지의 숫자 중 하나만 입력해주세요.")
   select1 = int(input())
   print("0부터 9까지의 숫자 중 하나만 입력해주세요.")
   select2 = int(input())

   if temp1 != 10000 and temp2 != 10000 and select1 == temp1 or select1 == temp2 or select2 == temp1 or select2 == temp2:
      print()
      print("방금 선택하신 카드와 동일한 카드입니다.")
      print("다시 선택해주세요")
      print()

   elif select1 == select2:
      print()
      print("같은 자리의 카드는 두 번 선택할 수 없습니다.")
      print("다시 선택해주세요")
      print()

   else:
      if front[select1] == front[select2]:
         print()
         print(front[select1],front[select2],"서로 같은 카드입니다.")
         back[select1] = front[select1]
         back[select2] = front[select2]
         print(back)
         print()
         cnt += 1
         print(cnt)

      else:
         print()
         print(front[select1],front[select2],"서로 다른 카드입니다.")
         print("다시 선택해주세요")
         print()

   if cnt == 5:
      print()
      print("모든 카드를 뒤집었습니다.")
      print("게임을 종료합니다.")
      print(back)
      print()
      break
   temp1 = select1
   temp2 = select2
   continue