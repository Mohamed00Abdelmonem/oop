# import random
# r = ['rock', 'paper','scissors' ]
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# play = input("Please Enter Your played :")

# class Game:
#     def __init__(self):
#         pass
   
#     def game(self, your_play, ):
#         while True:
#             choose = random.choice(r)

#             #Rock

#             if your_play == 'rock' and choose == 'scissors':
#                 print(scissors)
#                 print('you winer')  
               
#             elif your_play == 'rock' and choose == 'paper':
#                 print(paper)
#                 print('you lose')
#             elif your_play == 'rock' and choose == 'rock':
#                 print(rock)
#                 print('agin')
            
#             # Paper

#             if your_play == 'paper' and choose == 'scissors':
#                 print(scissors)
#                 print('you lose')
#             elif your_play == 'paper' and choose == 'rock':
#                 print(rock)
#                 print('you winer')
#             elif your_play == 'paper' and choose == 'paper':
#                 print(paper)
#                 print('agin')

#             # Scissors
            

#             if your_play == 'scissors' and choose == 'paper':
#                 return('you winer')
#             elif your_play == 'scissors' and choose == 'rock':
#                 return('you lose')
#             elif your_play == 'scissors' and choose == 'scissors':
#                 return('agin')

# result = Game() 
# print(result.game(play))




import random

r = ['rock', 'paper', 'scissors']

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

class Game:
    def game(self):
        while True:
            play = input("Please Enter Your play ('rock', 'paper', 'scissors') or 'exit' to quit: ")
            if play.lower() == 'exit':
                print("Thanks for playing! Exiting the game.")
                break

            if play not in r:
                print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
                continue

            choose = random.choice(r)
            
            if choose == 'rock':
                print(rock)
            elif choose == 'paper':
                print(paper)
            else:
                print(scissors)

            # Game logic
            if play == choose:
                print("It's a tie!")
            elif (play == 'rock' and choose == 'scissors') or (play == 'paper' and choose == 'rock') or (play == 'scissors' and choose == 'paper'):
                print("You win!")
            else:
                print("You lose!")

if __name__ == "__main__":
    result = Game() 
    result.game()









# # perfect code 

# import random

# class Game:
#     def __init__(self):
#         # Initialize the game with available choices and ASCII art for each choice
#         self.choices = ['rock', 'paper', 'scissors']
#         self.rock = '''
#         _______
#     ---'   ____)
#           (_____)
#           (_____)
#           (____)
#     ---.__(___)
#     '''
#         self.paper = '''
#         _______
#     ---'   ____)____
#               ______)
#               _______)
#              _______)
#     ---.__________)
#     '''
#         self.scissors = '''
#         _______
#     ---'   ____)____
#               ______)
#            __________)
#           (____)
#     ---.__(___)
#     '''
#         self.round_count = 0

#     def display_computer_choice(self, choice):
#         # Display the ASCII art for the computer's choice
#         if choice == 'rock':
#             print(self.rock)
#         elif choice == 'paper':
#             print(self.paper)
#         else:
#             print(self.scissors)

#     def play_round(self, player_choice):
#         # Game loop for playing rounds until the player chooses to exit
#         while True:
#             if player_choice.lower() == 'exit':
#                 print("Thanks for playing! Exiting the game.")
#                 break

#             if player_choice not in self.choices:
#                 print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")
#                 continue

#             # Computer randomly selects a choice
#             computer_choice = random.choice(self.choices)
#             print("Computer's choice:")
#             self.display_computer_choice(computer_choice)

#             # Game logic to determine the winner
#             if player_choice == computer_choice:
#                 print("It's a tie!")
#             elif (player_choice == 'rock' and computer_choice == 'scissors') or \
#                  (player_choice == 'paper' and computer_choice == 'rock') or \
#                  (player_choice == 'scissors' and computer_choice == 'paper'):
#                 print("You win!")
#             else:
#                 print("You lose!")

#             # Increment the round count and prompt the player for the next round
#             self.round_count += 1
#             player_choice = input("Please Enter Your play ('rock', 'paper', 'scissors') or 'exit' to quit: ")

# if __name__ == "__main__":
#     # Create a Game object and start playing the rounds
#     game = Game() 
#     game.play_round(input("Please Enter Your play ('rock', 'paper', 'scissors') or 'exit' to quit: "))
