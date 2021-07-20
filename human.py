from player import Player


class Human(Player):

    def __init__(self):
        self.name = "name"
        self.gesture = ""
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
    def choose_gesture(self):
        print('\n'.join(self.gesture_list))
        gesture = input(
            "Please enter one of the available gestures: ").lower()
        return gesture
        # while gesture != "Rock" or gesture != "Scissors" or gesture != "Lizard" or gesture != "Spock":
        #     gesture = input(
        #         "Invalid entry. Please enter one of the available gestures: ")
        #     self.chosen_gesture = gesture
