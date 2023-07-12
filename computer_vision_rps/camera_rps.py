from random import randint
import time
import cv2
from keras.models import load_model
import numpy as np

class CVRockPaperScissors:
    cap = cv2.VideoCapture(0)
    model = load_model('keras_model.h5')
    computer_score = 0
    player_score = 0
    options = ["rock","paper","scissors"]
    user_choosing_duration = 30

    def __init__(self,player_name = "Humanoid Player",countdown_timer = 3):
        self.player_name = player_name
        self.players = ["Computer",self.player_name]
        self.countdown_timer = countdown_timer
        self.user_choice = ''
        self.computer_choice = ''

    def loading_bar(self):
        print("""
                    \n********************LOADING GAME********************\n""")
        
    def get_highest_probability(self) -> int:
        data_collection_period = CVRockPaperScissors.user_choosing_duration
        while data_collection_period != 0:    
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            ret, frame = CVRockPaperScissors.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = CVRockPaperScissors.model.predict(data)
            cv2.imshow('frame', frame)
            cv2.waitKey(50)
            data_collection_period -= 1
        cv2.destroyAllWindows()
        return (np.argmax(prediction[0]))
    
    def get_prediction(self, index) -> str:
        if index == 3:
            raise ValueError("You did not pick anything!")
        elif index == 0:
            return 'rock'
        elif index == 1:
            return 'paper'
        elif index == 2:
            return 'scissors'
        
    def get_computer_choice(self) -> str : 
        random_index = randint(0,2)
        computer_choice = CVRockPaperScissors.options[random_index]
        return computer_choice
    
    def get_user_choice(self) -> str:
        user_choice = self.get_prediction(self.get_highest_probability())
        return user_choice
    
    def get_winner(self) -> str:
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        if computer_choice == "rock" and user_choice == "scissors":
            print("You lost!")
            return self.players[0],computer_choice,user_choice
        elif computer_choice == "rock" and user_choice == "paper":
            print("You won!")
            return self.players[1],computer_choice,user_choice
        elif computer_choice == "scissors" and user_choice == "paper":
            print("You lost!")
            return self.players[0],computer_choice,user_choice
        elif computer_choice == "scissors" and user_choice == "rock":
            print("You won!")
            return self.players[1],computer_choice,user_choice
        elif computer_choice == "paper" and user_choice == "rock":
            print("You lost!")
            return self.players[0],computer_choice,user_choice
        elif computer_choice == "paper" and user_choice == "scissors":
            print("You won!")
            return self.players[1],computer_choice,user_choice
        else:
            print("It's a tie!")
            return None, computer_choice, user_choice

    def winner_validater(self) -> str:
        winner, computer_choice, user_choice = self.get_winner()
        if winner == None:
            print("No one won this round.")
        elif winner == self.players[0]:
            print(f"The {self.players[0]} has won this round.")
            CVRockPaperScissors.computer_score += 1
        else:
            print(f"{self.players[1]} has won this round.")
            CVRockPaperScissors.player_score += 1
        return computer_choice, user_choice
    
    def countdown(self):
        timer = self.countdown_timer
        while True:
            if timer > 0:
                ret, frame = CVRockPaperScissors.cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(timer), (250, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
                cv2.imshow("Shaka",frame)
                cv2.waitKey(2000)
                timer -= 1

            else:
                ret, frame = CVRockPaperScissors.cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str("GO!!"), (150, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
                cv2.imshow("Shaka",frame)
                cv2.waitKey(2000)
                cv2.destroyAllWindows()
                break

    def display_scoreboard(self):
        print(f"""\n
                            Player: {CVRockPaperScissors.player_score}    Computer: {CVRockPaperScissors.computer_score}""")
        
    def play_one_round(self):
        self.countdown()
        computer_choice, user_choice = self.winner_validater()
        print(f"Player picked: {user_choice}\nComputer picked: {computer_choice}")
        time.sleep(2)
        self.display_scoreboard()

    def play_game(self):
        while True:
            if CVRockPaperScissors.computer_score == 3 or CVRockPaperScissors.player_score == 3:
                if CVRockPaperScissors.computer_score == 3: 
                    print(f"Computer is superior.\n{self.player_name} has been defeated.\nThe defeated must surrender :(")
                    break
                else:
                    print(f"The computer has been defeated.\n{self.player_name} is superior, as humans always have been.")
                    break
            else:
                self.play_one_round()
            


        
        

# print("""
# \n*******************LOADING GAME********************\n
# """)
# model = load_model('keras_model.h5')
# cap = cv2.VideoCapture(0)
# options = ["rock","paper","scissors"]
# players = ["Computer","Humanoid Player"]
# countdown_timer = 3
# user_choosing_duration = 30
# computer_score = 0
# player_score = 0


# def get_highest_probability(duration:int) -> int: 
#     data_collection_period = duration
#     while data_collection_period != 0:    
#         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#         ret, frame = cap.read()
#         resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
#         image_np = np.array(resized_frame)
#         normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
#         data[0] = normalized_image
#         prediction = model.predict(data)
#         cv2.imshow('frame', frame)
#         cv2.waitKey(50)
#         data_collection_period -= 1
#     cv2.destroyAllWindows()
#     return (np.argmax(prediction[0]))

# def get_prediction(index) -> str:
#     if index == 3:
#         raise ValueError("You did not pick anything!")
#     elif index == 0:
#         return 'rock'
#     elif index == 1:
#         return 'paper'
#     elif index == 2:
#         return 'scissors'
    

# def get_computer_choice() -> str : 
#     random_index = randint(0,2)
#     computer_choice = options[random_index]
#     return computer_choice

# def get_user_choice() -> str:
#     user_choice = get_prediction(get_highest_probability(user_choosing_duration))
#     return user_choice

# def get_winner(computer_choice,user_choice):
    
#     if computer_choice == "rock" and user_choice == "scissors":
#         print("You lost!")
#         return players[0]
#     elif computer_choice == "rock" and user_choice == "paper":
#         print("You won!")
#         return players[1]
#     elif computer_choice == "scissors" and user_choice == "paper":
#         print("You lost!")
#         return players[0]
#     elif computer_choice == "scissors" and user_choice == "rock":
#         print("You won!")
#         return players[1]
#     elif computer_choice == "paper" and user_choice == "rock":
#         print("You lost!")
#         return players[0]
#     elif computer_choice == "paper" and user_choice == "scissors":
#         print("You won!")
#         return players[1]
#     else:
#         print("It's a tie!")
#         return None

# def winner_validater(winner):
#     if winner == None:
#         print("No one won this round.")
#     elif winner == "Computer":
#         print(f"The {winner} has won this round.")
#         global computer_score
#         computer_score += 1
#     else:
#         print(f"The {winner} has won this round.")
#         global player_score
#         player_score += 1
    
# def countdown(time):
#     timer = time
#     while True:
#             if timer > 0:
#                 ret, frame = cap.read()
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 cv2.putText(frame, str(timer), (200, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
#                 cv2.imshow("Shaka",frame)
#                 cv2.waitKey(2000)
#                 timer -= 1

#             else:
#                 ret, frame = cap.read()
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 cv2.putText(frame, str("GO!!"), (200, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
#                 cv2.imshow("Shaka",frame)
#                 cv2.waitKey(2000)
#                 cv2.destroyAllWindows()
#                 break


# def display_scoreboard():
#     print(f"""\n
#                             Player: {player_score}    Computer: {computer_score}
# """)



# def play_one_round():
#     computer_choice = get_computer_choice()
#     print(f"\nChoose one from the following:{options}")
#     countdown(countdown_timer)
#     user_choice = get_user_choice()
#     print(f"Player picked: {user_choice}\nComputer picked: {computer_choice}")
#     winner = get_winner(computer_choice, user_choice)
#     time.sleep(1)
#     winner_validater(winner)
#     time.sleep(2)
#     display_scoreboard()
    
# def play_game():
#     while True:
#         if computer_score == 3 or player_score == 3:
#             if computer_score == 3:
#                 print("Computer is superior.\nThe humanoid player has been defeated.\nThe defeated must surrender :(")
#                 break
#             else:
#                 print("The computer has been defeated.\nHumanoid players are superior, as it always has been.")
#                 break
#         else:
#             play_one_round()
            

# play_game()



hello = CVRockPaperScissors()

hello.play_game()


    