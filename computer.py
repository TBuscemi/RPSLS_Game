from player import Player
import random


class Computer(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

# maybe, not sure about using to random the gestures for the AI
    # def rpsls_gesture(self):
        #self.choice = self.gestures[random.randint(0, 4)]
