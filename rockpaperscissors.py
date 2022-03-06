import random
import time

print("Hello, welcome to the Rock Paper Scissors Game.") , time.sleep(0.7)
print("Enter R, P and S to play, or 'q' to quit."), time.sleep(0.7)

user_wins = 0
computer_wins = 0

choices = ["R", "P", "S"]
while True:
    user_input = input("Enter your move: ")
    computer_choice = choices[random.randint(0, 2)]
    if user_input == "R" and computer_choice == "R":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        print("Tie")
    elif user_input == "R" and computer_choice == "P":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        computer_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
    elif user_input == "R" and computer_choice == "S":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        user_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
    if user_input == "P" and computer_choice == "P":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        print("Tie")
    elif user_input == "P" and computer_choice == "R":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        user_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
    elif user_input == "P" and computer_choice == "S":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        computer_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
    if user_input == "S" and computer_choice == "S":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        print("Tie")
    elif user_input == "S" and computer_choice == "P":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        user_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")
    elif user_input == "S" and computer_choice == "R":
        print(f"\nUser: {user_input}")
        print(f"Computer: {computer_choice}\n")
        computer_wins += 1
        print(f"User Wins: {user_wins}")
        print(f"Computer Wins: {computer_wins}")  
    if user_input == 'q':
        print("Succesfuly quitted the game."), time.sleep(0.7)
        if user_wins > computer_wins:
            print("You won")
        elif user_wins == computer_wins:
            print("It's tie")
        else:
            print("You lost")
        break
