import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_chose = [rock, paper, scissors]
player_chose = int(input(f"Chose 0 for Rock, 1 for paper, 2 for scissors\n"))
if player_chose >= 0 and player_chose <= 2:
    print(list_chose[player_chose])

computer_chose = random.randint(0, 2)
print("Computer Chose:")
print(list_chose[computer_chose])

if player_chose >= 3 or player_chose < 0:
    print("You Chose Wrong Number : You Lose!")
elif player_chose == 0 and computer_chose == 2:
    print("You Win Bro!")
elif computer_chose == 0 and player_chose == 2:
    print("You Lose!")
elif computer_chose > player_chose:
    print("You Lose!")
elif player_chose > computer_chose:
    print("You Win Bro!")
elif player_chose == computer_chose:
    print("Game Draw!")
