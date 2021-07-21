from player import Player


class Human(Player):

    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        print("\nPick a gesture: \n1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock\n")

        gesture = int(input(
            "Please enter 1-5 for the available gestures: "))
        while gesture < 1 or gesture > 5:
            gesture = int(input(
                "Invalid entry. Please enter 1-5 for the available gestures: "))
        self.gesture_choice = gesture
        self.generate_beats(gesture)
