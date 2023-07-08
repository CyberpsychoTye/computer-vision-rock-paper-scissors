from random import randint

options = ["rock","paper","scissors"]

def get_computer_choice() -> str : 
    random_index = randint(0,len(options))
    computer_choice = options[random_index]
    return computer_choice

def get_user_choice() -> str:
    print(f"Choose one from the following:{options}")
    user_choice = input("Type in your choice: ").lower()
    return user_choice

def get_winner(computer_choice,user_choice):
    who_won = ["Computer","Humanoid Player"]
    if computer_choice == "rock" and user_choice == "scissors":
        print("You lost!")
        return who_won[0]
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
        return who_won[1]
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost!")
        return who_won[0]
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
        return who_won[1]
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost!")
        return who_won[0]
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
        return who_won[1]
    else:
        print(f"Computer picked: {computer_choice}\n Player picked: {user_choice}\n It's a tie!")
        return None
    
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"Player picked: {user_choice}\nComputer picked: {computer_choice}")
    winner = get_winner(computer_choice, user_choice)
    print(f"The {winner} has won this battle. The defeated must now surrender")

play()
    

