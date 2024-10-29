'''
Author= Ben Mathew Ninan
Date=22/10/2024
Python program To Find Largest number
'''
Temp=float(input("Temperature in celsius Fahrenheit:"))
Unit=input("Is this in (C)elsius or (F)ahrenheit")
if Unit=="C":
    f=(9/5*Temp)+32
    print(Temp,"Celsius is",f,"Fahrenheit")
elif Unit=="F":
    c=5/9*(Temp-32)
    print(Temp,"Fahrenheit is",c,"celsius")
else:
    print("invalid input")















