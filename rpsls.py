import random
from humanplayer import HumanPlayer
from computer_player import ComputerPlayer

class RPSLS:
    def __init__(self):
        self.player_one = HumanPlayer()
        self.player_two = ""
        


    def display_welcome():
        print("")
        print("Welcome to Rock, Paper, Scissor, Lizard, Spock!!!")
        print("")

win_loss_combos =[("Rock"   , "Scissors")
                  ("Scissor", "Paper")
                  ("Paper"  , "Rock")
                  ("Rock"   , "Lizard")
                  ("Lizard" , "Spock")
                  ("Spock"  , "Scissor")
                  ("Scissor", "Lizard")
                  ("Lizard" , "Paper")
                  ("Paper"  , "Spock")
                  ("Spock"  , "Rock")]

choices = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]

computer_choice = random.choice(choices)

print(computer_choice)
        

        #Assign self.player_two is going to equal either HumanPlayer() or ComputerPlayer()
    def choose_player(self):
        self.player_two = ComputerPlayer()

        #Create winning logic ex. If self.player_one.selected_gesture = "rock" and self.player_two.selected_gesture scissors.self.player_one.wins += 1
        #While loop to keep the game running.
    def rounds():
        