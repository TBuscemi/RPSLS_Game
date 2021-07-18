from human import Human
from computer import Computer


class Play:
    def __init__(self):
        self.player_one = Human(input("Enter your name: "))
        self.player_two = Computer()
        self.round = 1

    def start_game(self):
        # display_rules the welcoming message and rules would need to go here
        # maybe "hit enter to continue" to play
        pass

    # def display_welcome(self): #add this later, it's extra.
    #     print("GREETINGS PROFESSOR FALKEN")
    #     print()
    #     print("A STRANGE GAME.")
    #     print("THE ONLY WINNING MOVE IS")
    #     print("NOT TO PLAY.")
    #     print()
    #     print("HOW ABOUT A NICE GAME OF ROCK PAPER SCISSORS LIZARD SPOCK?")
    #     pass

    def display_rules(self):
        print()
        print("Instructions for Rock-Paper-Scissors-Lizard-Spock: ")
        print()
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")
        print()
        pass

    def comp_turn(self):
        pass

    def player_choice(self, player_turn):
        pass

    def results(self):
        pass

    def compare_results(self):
        pass

    def display_results(self):
        pass

    def show_winner(self):
        pass
