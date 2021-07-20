from player import Player


class Human(Player):

    def __init__(self, name):
        self.human_score = 0
        super().__init__(name)

    def choose_gesture(self):
        print("\nRock\nPaper\nScissors\nLizard\Spock")
        gesture = input("Please enter one of the available gestures: ")

        while gesture != "Rock" or gesture != "Scissors" or gesture != "Lizard" or gesture != "Spock":
            gesture = input(
                "Invalid entry. Please enter one of the available gestures: ")
            self.chosen_gesture = gesture
