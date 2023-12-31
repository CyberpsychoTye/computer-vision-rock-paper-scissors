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
    countdown_duration = 8
    countdown_from = 3

    def __init__(self,player_name = "Humanoid Player"):
        self.player_name = player_name
        self.players = ["Computer",self.player_name]
        self.user_choice = ''
        self.computer_choice = ''

        
    def landing_screen(self):
        while True:
            ret, frame = CVRockPaperScissors.cap.read()
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.rectangle(frame,(26,87),(616,360),(0,0,0),-1)
            cv2.putText(frame,f"Welcome {self.player_name}",(85,120),font,1,(250,250,250),1,cv2.LINE_4)
            cv2.putText(frame,"To Play:",(30,210),font,0.7,(255,102,51),1,cv2.LINE_8)
            cv2.putText(frame,"1) Choose either Rock, Paper, or Scissors.",(32,250),font,0.6,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,"2) Show the camera your choice after the countdown.",(32,275),font,0.6,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,"3) Good luck :)",(32,300),font,0.6,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,"3) Good luck :)",(32,300),font,0.6,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,"Press 'c' to continue.....",(30,345),font,0.6,(255,250,250),1,cv2.LINE_8)
            cv2.imshow('Landing Screen',frame)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.destroyAllWindows()
                break
            

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
        self.computer_choice = self.get_computer_choice()
        self.user_choice = self.get_user_choice()
        if self.computer_choice == "rock" and self.user_choice == "scissors":
            print("You lost!")
            return self.players[0]
        elif self.computer_choice == "rock" and self.user_choice == "paper":
            print("You won!")
            return self.players[1]
        elif self.computer_choice == "scissors" and self.user_choice == "paper":
            print("You lost!")
            return self.players[0]
        elif self.computer_choice == "scissors" and self.user_choice == "rock":
            print("You won!")
            return self.players[1]
        elif self.computer_choice == "paper" and self.user_choice == "rock":
            print("You lost!")
            return self.players[0]
        elif self.computer_choice == "paper" and self.user_choice == "scissors":
            print("You won!")
            return self.players[1]
        else:
            print("It's a tie!")
            return None

    def winner_validater(self) -> str:
        winner = self.get_winner()
        if winner == None:
            print("No one won this round.")
        elif winner == self.players[0]:
            print(f"The {self.players[0]} has won this round.")
            CVRockPaperScissors.computer_score += 1
        else:
            print(f"{self.players[1]} has won this round.")
            CVRockPaperScissors.player_score += 1
        

    def countdown_wrapper(self,func):
        def wrapper (character:int):
            target = (time.time()) + CVRockPaperScissors.countdown_duration
            while True:
                current = time.time()
                if target - current >= 6:
                    func(character)
                elif target - current >= 4:
                    func(character - 1)
                elif target - current >= 2:
                    func(character - 2)
                elif target - current > 0:
                    func('GO!!',x_alignment = 100, shape_starting = (104,94),shape_ending = (522,264))
                else:
                    cv2.destroyAllWindows()
                    break
        return wrapper

   
    def character_display(self,character, x_alignment:int= 250, shape_starting = (251,94),shape_ending = (390,264)):
        target = time.time() + (CVRockPaperScissors.countdown_duration/4)
        while True:
            current = time.time()
            if current >= target:
                break
            else:    
                ret, frame = CVRockPaperScissors.cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.rectangle(frame,shape_starting,shape_ending,(0,0,0),-1)
                cv2.putText(frame, str(character), (x_alignment, 250), font, 7, (255, 255, 255),4, cv2.LINE_AA)
                cv2.imshow("Shaka",frame)
                cv2.waitKey(50)
            

    def display_scoreboard(self):
        font = cv2.FONT_HERSHEY_COMPLEX
        while True:
            ret, frame = CVRockPaperScissors.cap.read()
            cv2.rectangle(frame,(26,87),(616,360),(0,0,0),-1)
            cv2.putText(frame,"Scoreboard",(130,150),font,2,(250,250,250),1,cv2.LINE_4)
            cv2.putText(frame,f"Computer: {CVRockPaperScissors.computer_score}",(97,220),font,0.7,(0,0,255),1,cv2.LINE_4)
            cv2.putText(frame,f"{self.player_name}: {CVRockPaperScissors.player_score}",(313,220),font,0.7,(255,102,51),1,cv2.LINE_4)
            cv2.putText(frame,f"Computer picked: {self.computer_choice}",(45,307),font,0.5,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,f"{self.player_name} picked: {self.user_choice}",(45,335),font,0.5,(255,250,250),1,cv2.LINE_8)
            cv2.putText(frame,"press 'c' to continue.....",(405,335),font,0.5,(255,250,250),1,cv2.LINE_8)
            cv2.imshow("Scoreboard",frame)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.destroyAllWindows()
                break

    
    def play_one_round(self):
        self.countdown_wrapper(self.character_display)(self.countdown_from)
        self.winner_validater()
        print(f"Player picked: {self.user_choice}\nComputer picked: {self.computer_choice}")
        time.sleep(2)
        self.display_scoreboard()

    def play_game(self):
        self.landing_screen()
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

hello = CVRockPaperScissors()
hello.character_display(3)






            






    