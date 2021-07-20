from player import Player
import random

class Computer(Player):

    def __init__(self):
        self.name = "ai"
        self.gesture = ""
        self.gesture_list = [""]
  
    def choose_gesture(self):
        
        i = random.randrange(len(self.gesture_list))
        gesture = self.gesture_list[i]
        return gesture   
