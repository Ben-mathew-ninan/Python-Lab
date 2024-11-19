my_list=[12,10,12,34,56,10]
unique_list=[]
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print("The original list is:",my_list)
print(unique_list)

