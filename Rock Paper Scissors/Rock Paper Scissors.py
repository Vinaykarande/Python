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
image = [rock, paper, scissors]
#Write your code below this line 👇
user = int(input("Enter 0 for Rock, 1 for paper and 2 for scissors \n"))

if user >= 3 and user < 0:
    print("You typed wrong input, You Loss!")
else:
    print("you selected \n")
    print(image[user])

    computer = random.randint(0, 2)
    print("computer selected \n")
    print(image[computer])

    if (user == 0 and computer == 2):
        print("You Win!")
    elif (computer == 0 and user == 2):
        print("You Loss")
    elif computer > user:
        print("You Loss")
    elif user > computer:
        print("You Win!")
    elif computer == user:
        print("It's Draw")
