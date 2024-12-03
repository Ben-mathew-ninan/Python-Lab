'''Author=Ben Mathew Ninan
   program=Monty Hall
   date=03/12/2024'''


import random
print("Welcome to the show")
doors=[1,2,3]
host=random.choice(doors)
participate=int (input("please choose any door"))
if participate==host:
    print("you won")
else:
    print("you have choose wrong option")
    replay=input("do you want to change the option")
    if replay=="yes":
        received=int(input("select another option"))
        if received==host:
            print("you won")
        else:
            print("you have got goat again,you loose")
    if replay=="no":
        print("you have got a goat,so you loose")
