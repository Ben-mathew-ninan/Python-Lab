from itertools import filterfalse
'''
Python Lab
Author:Ben Mathew Ninan
Date:29/10/2024
Program:The number of prime numbers between a given number'''

limit = int(input("enter a number"))
for number in range (2,limit+1):
    isPrime="True"
    for i in range (2,(number//2)+1):
        if number %i ==0:
            isPrime="False"
    if isPrime=="True":
        print(number)










