from player import Player
import random

class ComputerPlayer(Player):
    def __init__(self, name="", player_number=2):
        super().__init__(name, player_number)

    def validate_name(name, player_number):
         if name == (""):
            name = input(f"Player {player_number}/Computer, What is your name?: ")
            return name

    def method_of_play(self, gestures):
        index = random.randint(0,4)
        gesture_of_choice = (gestures[index])
        print(f"The computer {self.name} has selected {gesture_of_choice}! ")
        return gesture_of_choice


    