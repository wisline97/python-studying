'''
	[문제]
		아래와 같이 출력하시오.
'''
'''
	[문제1]
		11112
		11122
		11222
		12222
'''
print("[문제1]")
max = 5
i = 1
for x in range(4):
    for y in range(max-i):
        print("1",end=" ")
    for z in range(i):
        print("2", end=" ")
    i+=1
    print()
print()


'''
	[문제2]
		12222
		11222
		11122
		11112
'''
print("[문제2]")
max = 5
i = 1
for x in range(4):
    for y in range(i):
        print("1",end=" ")
    for z in range(max-i):
        print("2", end=" ")
    i+=1
    print()

print()

'''
	[문제3]
		11211
		12221	
		22222
'''
print("[문제3]")
max = 5
i = 1
for x in range(3):
    for y in range((max-i)//2):
        print("1",end=" ")
    for z in range(i):
        print("2", end=" ")
    for y in range((max-i)//2):
        print("1",end=" ")
    i+=2
    print()

print()
'''
	[문제4]
		  2
		 222
		22222
'''
print("[문제4]")
max = 5
i = 1
for x in range(3):
    for y in range((max-i)//2):
        print(" ",end=" ")
    for z in range(i):
        print("2", end=" ")
    for y in range((max-i)//2):
        print(" ",end=" ")
    i+=2
    print()
print()

'''
	[문제5]
		22222
		 222
		  2   
'''
print("[문제5]")
max = 5
i = 5
for x in range(3):
    for y in range((max-i)//2):
        print(" ",end=" ")
    for z in range(i):
        print("2", end=" ")
    for y in range((max-i)//2):
        print(" ",end=" ")
    i-=2
    print()