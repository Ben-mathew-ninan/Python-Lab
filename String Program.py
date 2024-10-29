'''
Author:Ben Mathew Ninan
Date:29/10/2024
Program:The number of prime numbers between a given number'''
string_input=input("enter a String")
vowels = "aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
print(f"no of vowels in given string{string_input}={vowels_count}")
