import random

def roll_dice():
    return random.randint(1, 6)

MAX = 50

while True:
   try:
      num_players= int(input("How many players for this PIG match: (between 2 and 5) "))
      break
   except ValueError:
      print("Invalid input")

while num_players <2 or num_players>5:
   print("Invalid number")
   num_players= int(input("How many players for this PIG match: (between 2 and 5) "))

player_points=[]
for _ in range(num_players):
   player_points.append(0)
print(player_points)

while True:
    for i in range(num_players):
       score=0
       print()
       print(f"Player number {i+1}, your turn to roll the dice!\n")
       current=roll_dice()
       while True:
          print(f"You rolled the number {current}")
          if current == 1:
             print("You lose the points and now it's the next player's turn!")
             break
          score+= current
          print(f"Your score for this turn is {score}")
          playing = input("Do you want to continue rolling the dice? ('yes' if you want, anything else to stop):  ")
          if playing != "yes":
             player_points[i]+=score
             if player_points[i]>=MAX:
                print(f"\nPlayer number {i+1} has won with {player_points[i]} points")
                exit()
             break
          else:
             current = roll_dice()
    print(player_points)