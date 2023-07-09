from random import randint
import time
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
options = ["rock","paper","scissors"]

def get_highest_probability() -> int: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    global prediction
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
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
    random_index = randint(0,len(options))
    computer_choice = options[random_index]
    return computer_choice

def get_user_choice() -> str:
    print(f"Choose one from the following:{options}")
    user_choice = get_prediction(get_highest_probability())
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
    