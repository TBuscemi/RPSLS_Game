from player import Player
import random


class Computer(Player):

    def __init__(self):
        self.computer_score = 0
        super().__init__()

    def computer_move(self):
        computer_choice = random.choice(
            self.gesture_choices)  # will come back to this if it isn't working
        print(computer_choice)


ai = Computer()
ai.computer_move()
