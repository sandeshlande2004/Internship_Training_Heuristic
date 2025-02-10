# import random

# possible_action = ['rock', 'paper', 'scissor']

# def get_user_choice():
#     user_choice = input("Enter a choice (rock, paper, scissor): ")
#     return user_choice

# def computer_choice():
#     return random.choice(possible_action)

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif user_choice == 'rock':
#         if computer_choice == 'scissor':
#             return "Rock smashes scissor! You win!"
#         else:
#             return "Paper covers rock! You lose."
#     elif user_choice == 'paper':
#         if computer_choice == 'rock':
#             return "Paper covers rock! You win!"
#         else:
#             return "Scissor cuts paper! You lose."
#     elif user_choice == 'scissor':
#         if computer_choice == 'paper':
#             return "Scissor cuts paper! You win!"
#         else:
#             return "Rock smashes scissor! You lose."
#     else:
#         return "Invalid input! You have not entered rock, paper or scissor, try again."

# def play_game():
#     user_choice = get_user_choice()
#     computer = computer_choice()
#     print(f"\nYou chose {user_choice}, computer chose {computer}.\n")
#     print(determine_winner(user_choice, computer))

# play_game()

#------------------------------------------------------------------------------------------------------------------------------------------------#

import random  #used to generate random results

title = 'Rock Paper Scissor Game'
print(title.center(50, '*'))
print('\n')

welcome = 'Welcome to the Rock Paper Scissor Game !'
print(welcome.center(50))
print('\n')

possible_action = ['rock', 'paper', 'scissor']

while True:
    
    user_choice = input("1.Rock\n2.Paper\n3.Scissor\nEnter your choice: ").lower() #user choice #lower() used to convert string to lower case because we have used lower case in possible_action and we want to match user choice with possible_action also it is case insensitive ie it maintain input format from user to lowercase so that there will be no error
    print('----------------------------------------------------------------------------------------')
    if user_choice not in possible_action:
        print('Invalid input! You have not entered rock, paper or scissor, try again.')
        continue
    
    computer_choice = random.choice(possible_action)  #computer choice random
    print(f'Your action is {user_choice} and computer action is {computer_choice}')
    
    if(user_choice == 'rock'):
        
        if(computer_choice == 'rock'):
            print("It's a tie!\nBoom!!")
        elif(computer_choice == 'paper'):
            print("Paper covers rock!\nYou lose.\nBetter luck next time!")
        elif(computer_choice == 'scissor'):
            print("Rock smashes scissor!\nYou win!\nCongratulations!\nNailed it!!")
            
    elif(user_choice == 'paper'):
        
        if(computer_choice == 'rock'):
            print("Paper covers rock!\nYou win!\nCongratulations!\nNailed it!!")
        elif(computer_choice == 'paper'):
            print("It's a tie!")
        elif(computer_choice == 'scissor'):
            print("Scissor cuts paper!\nYou lose.\nBetter luck next time!")
    
    elif(user_choice == 'scissor'):
        
        if(computer_choice == 'rock'):
            print("Rock smashes scissor!\nYou lose.\nBetter luck next time!")
        elif(computer_choice == 'paper'):
            print("Scissor cuts paper!\nYou win!\nCongratulations!\nNailed it!!")
        elif(computer_choice == 'scissor'):
            print("It's a tie!")
    print('\n')       
    play_again = input('Do you want to play again? (y/n): ') #play again
    
    if play_again.lower() != 'y':
        break

