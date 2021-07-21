class Player:

    def __init__(self, name):
        self.name = name
        self.player_score = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.gesture_choice = None
        self.gesture_beats = []

    def score(self):  # each time this is called it increases the score by one
        self.player_score += 1

    def generate_beats(self, gesture):
        if gesture == 1:
            self.gesture_beats.append(3)
            self.gesture_beats.append(4)
        if gesture == 2:
            self.gesture_beats.append(1)
            self.gesture_beats.append(5)
        if gesture == 3:
            self.gesture_beats.append(2)
            self.gesture_beats.append(4)
        if gesture == 4:
            self.gesture_beats.append(2)
            self.gesture_beats.append(5)
        if gesture == 5:
            self.gesture_beats.append(1)
            self.gesture_beats.append(3)
