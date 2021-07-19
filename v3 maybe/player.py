class Player:
    def __init__(self, name):
        self.gesture_choices = [
            ("Rock"), ("Paper"), ("Scissors"), ("Lizard"), ("Spock")]
        self.chosen_gesture = None
        self.name = name
        self.wins = 0

    # def earned_win(self):
    #     self.earned_wins += 1

    # def gesture_choices(self, gesture):
    #     self.gesture = gesture
    #     self.wins = []
    #     self.who_wins()

    # def who_wins(self):
    #     if self.gesture == "Rock":
    #         self.wins.append("Scissors")
    #         self.wins.append("Lizard")
    #     if self.gesture == ("Paper"):
    #         self.wins.append("Rock")
    #         self.wins.append("Spock")
    #     if self.gesture == ("Scissors"):
    #         self.wins.append("Paper")
    #         self.wins.append("Lizard")
    #     if self.gesture == ("Lizard"):
    #         self.wins.append("Paper")
    #         self.wins.append("Spock")
    #     if self.gesture == ("Spock"):
    #         self.wins.append("Scissors")
    #         self.wins.append("Rock")
