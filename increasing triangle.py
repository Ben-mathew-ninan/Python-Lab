'''Author=Ben Mathew Ninan
Date=19/11/2024
Python program
triangle
'''

limit=int(input("enter the range"))
'''for i in range(1,6):
    for i in range(i):
        print("*",end=" ")
    print()'''



'''for i in range (limit,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''



'''for i in range(1, limit+1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(2 * i-1):
        print("*",end="")
    print()'''


for i in range (limit,0,-1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(2 * i-1):
        print("*",end="")
    print()