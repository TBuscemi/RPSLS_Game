from player import Player


class Human(Player):

    def __init__(self):
        self.human_score = 0
        super().__init__()
