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

#Write your code below this line 👇
play = [rock, paper, scissors]
# user choice input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))

# based on user choice print
if user_choice < 0 or user_choice > 2:
    print("Invalid input")    
else: 
    print(play[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(play[computer_choice])
    # Win OR loose logic
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice >  computer_choice:
        print("You win!")
    else:
        print("Draw, try again")