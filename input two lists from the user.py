
'''author=Ben Mathew Ninan
Date=19/11/2024
Python program
lists
'''
list1=[]
list2=[]
list1_size=int(input("Enter the size of list1:"))
print("Enter the elements of list1:")
for i in range(list1_size):
    list1.append(int(input()))


list2_size=int(input("Enter numbers for the second list"))
print("Enter the elements of list2:")
for i in range (list2_size):
    list2.append(int(input()))
print(list1,list2)


