#Parent Class
class Player:
    def __init__(self, name,):
        self.name = self.validate_name(name)
        self.win = 0
        self.list_of_gestures = ["Rock","Paper"]
        self.selected_gesture = ""

    def validate_name(self,name):
        if name == (""):
            name = input(f"Player {player_number}, What is your name?: ")
            return name
    
    def method_of_play(self, gestures):
        pass