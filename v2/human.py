from player import Player


class Human(Player):

    def __init__(self):
        self.human_score = 0
        super().__init__()

    # Use 1-5 input to select which gesture the player is using. Not sure if I want to keep numbers or change the numbers to the actual names
    def human_move(self):
        user_input = input(
            "Throw down! \nRock: '1' \nPaper: '2' \nScissors: '3' \nLizard: '4' \nSpock: '5' \nPlease pick a number 1-5: ")
        if user_input == '1':
            user_input = "Rock"
        if user_input == '2':
            user_input = "Paper"
        if user_input == '3':
            user_input = "Scissors"
        if user_input == '4':
            user_input = "Lizard"
        if user_input == '5':
            user_input = "Spock"
        else:
            # this should validate the input for the human/player gesture
            print(
                "Enter a valid option: \nRock: '1' \nPaper: '2' \nScissors: '3' \nLizard: '4' \nSpock: '5'")
            user_input = False
        return user_input
