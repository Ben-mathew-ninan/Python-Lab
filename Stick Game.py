'''Author=Ben Mathew Ninan
   Program=Stick Game
   Date=03/12/2024'''

print("welcome to stick_game")
print("Two players  take turns to play the game.Each player take one sets of stick during his turn.\n RULES \n"
      "A set contains 1,2,or3 sticks.Two player who takes the last stick is the loser.\n"
      "The number of sticks in the set is to be input.")
player1=input("enter name of player1:")
player2=input("enter name of player2")
sticks=16
print(f"number of sticks remaining ={sticks}")
while sticks>0:
    score1=int(input(f"{player1},choose 1,2,3 sticks"))
    sticks=sticks-score1
    print(f"number of sticks remaining={sticks}")
    if sticks<=0:
        print(f"{player1} lost.better luck next time")
        break
    score2=int(input(f"{player2},choose 1,2,3 sticks"))
    sticks=sticks-score2
    print(f"number of sticks remaining={sticks}")
    if sticks<=0:
        print(f"{player2} lost.better luck next time")
        break


