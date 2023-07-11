from random import randint
import time
import cv2
from keras.models import load_model
import numpy as np
print("""
\n*******************LOADING GAME********************\n
""")
model = load_model('keras_model.h5')
# cap = cv2.VideoCapture(0)
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ["rock","paper","scissors"]
players = ["Computer","Humanoid Player"]
computer_score = 0
player_score = 0
count_three = """
                                3333
                                   3
                                3333   
                                   3
                                3333
"""
count_two = """
                                222222
                                2    2
                                    2
                                   2
                                 22  
                                2222222 
"""

count_one = """
                                   1
                                 1 1
                                1  1
                                   1
                                   1
                                1111111   
"""

count_go = """
                                GGGG    OO   ||
                                G      O  O  ||
                                G  GG  O  O  ||
                                G   G  O  O  
                                GGGGG   OO   !!
"""

def get_highest_probability() -> int: 
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    cap.release()
    cv2.destroyAllWindows()
    return (np.argmax(prediction[0]))

def get_prediction(index) -> str:
    if index == 3:
        raise ValueError("You did not pick anything!")
    elif index == 0:
        return 'rock'
    elif index == 1:
        return 'paper'
    elif index == 2:
        return 'scissors'
    

def get_computer_choice() -> str : 
    random_index = randint(0,2)
    computer_choice = options[random_index]
    return computer_choice

def get_user_choice() -> str:
    user_choice = get_prediction(get_highest_probability())
    return user_choice

def get_winner(computer_choice,user_choice):
    
    if computer_choice == "rock" and user_choice == "scissors":
        print("You lost!")
        return players[0]
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
        return players[1]
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost!")
        return players[0]
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
        return players[1]
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost!")
        return players[0]
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
        return players[1]
    else:
        print("It's a tie!")
        return None

def winner_validater(winner):
    if winner == None:
        print("No one won this round.")
    elif winner == "Computer":
        print(f"The {winner} has won this round.")
        global computer_score
        computer_score += 1
    else:
        print(f"The {winner} has won this round.")
        global player_score
        player_score += 1
    
def choosing_countdown():
    time.sleep(4)
    print("\nShow your choice to the camera at the end of this countdown!")
    time.sleep(1)
    print(count_three)
    time.sleep(1)
    print(count_two)
    time.sleep(1)
    print(count_one)
    time.sleep(1)
    print(count_go)
    time.sleep(1)

def display_scoreboard():
    print(f"""\n
                            Player: {player_score}    Computer: {computer_score}
""")



def play_one_round():
    computer_choice = get_computer_choice()
    print(f"\nChoose one from the following:{options}")
    choosing_countdown()
    user_choice = get_user_choice()
    print(f"Player picked: {user_choice}\nComputer picked: {computer_choice}")
    winner = get_winner(computer_choice, user_choice)
    time.sleep(1)
    winner_validater(winner)
    time.sleep(2)
    display_scoreboard()
    # time.sleep(1)
    # print("Next round commencing soon. Prepare yourself.....")
    time.sleep(3)
    


def play_game():
    while True:
        if computer_score == 3 or player_score == 3:
            if computer_score == 3:
                print("Computer is superior.\nThe humanoid player has been defeated.\nThe defeated must surrender :(")
                break
            else:
                print("The computer has been defeated.\nHumanoid players are superior, as it always has been.")
                break
        else:
            play_one_round()
            

play_game()





    