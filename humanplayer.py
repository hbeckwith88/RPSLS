from ast import While
from player import Player

class HumanPlayer(Player):
    def __init__(self, name="", player_number=1):
        super().__init__(name, player_number)
        pass 

    def method_of_play(self, gestures):
         gesture_choice = ""
         valid_entry = False
         print(f"These are the gestures: {self.list_of_gestures}")
         while not valid_entry:
            try:
                gestures.index(gesture_choice)
                valid_entry = True
            except ValueError:
                print("That's not a valid option.  Please try again.")

         else:
            print(f"{self.name} your selection was {gesture_choice}.")
            return gesture_choice



        #if user_choice = "Rock" 
            #self.selected_gesture = "Rock"

        

