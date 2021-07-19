from human import Human
from computer import Computer
from player import Player


class Run_game:

    def __init__(self):

        pass

        # welcome + basic rules
    def display_welcome(self):
        print("GREETINGS PROFESSOR FALKEN "
              "\nSHALL WE PLAY A GAME? "
              "\n"
              "\nInstructions for the game: "
              "\nScissors cuts Paper "
              "\nPaper covers Rock "
              "\nRock crushes Lizard"
              "\nLizard poisons Spock"
              "\nSpock smashes Scissors"
              "\nScissors decapitate Lizard"
              "\nLizard eats Paper"
              "\nPaper disproves Spock"
              "\nSpock vaporizes Rock"
              "\nRock crushes Scissors"
              "\n"
              "\nEach gesture thrown beats two other gestures, and in turn can be beat by two. \n")

    def single_or_two_player(self):
        pass

        # instantiating human and computer objects:
    def single_player_round(self):
        player = Human()
        computer = Computer()

        # is a tie?
        if player.human_move == computer.computer_move:
            print("One of us should play better")
            return "It's a tie."

        # if player picks rocks
        elif player.human_move == "Rock" and computer.computer_move == "Paper":
            print("Paper covers Rock")
            return False  # Paper beats rock
        elif player.human_move == "Rock" and computer.computer_move == "Scissors":
            print("Rock crushes Scissors")
            return True  # Rock beats scissors
        elif player.human_move == "Rock" and computer.computer_move == "Lizard":
            print("Rock crushes Lizard")
            return True  # Rock beats lizard
        elif player.human_move == "Rock" and computer.computer_move == "Spock":
            print("Spock vaporizes Rock")
            return False  # Spock beats rock

        # if player picks paper
        elif player.human_move == "Paper" and computer.computer_move == "Rock":
            print("Paper covers Rock")
            return True  # Paper beats rock
        elif player.human_move == "Paper" and computer.computer_move == "Scissors":
            print("Scissors cuts Paper")
            return False  # Scissors beats paper
        elif player.human_move == "Paper" and computer.computer_move == "Lizard":
            print("Lizard eats Paper")
            return False  # Lizard beats paper
        elif player.human_move == "Paper" and computer.computer_move == "Spock":
            print("Paper disproves Spock")
            return True  # Paper beats Spock

        # if player picks Scissors
        elif player.human_move == "Scissors" and computer.computer_move == "Rock":
            print("Rock crushes Scissors")
            return False  # Rock beats scissors
        elif player.human_move == "Scissors" and computer.computer_move == "Paper":
            print("Scissors cuts Paper")
            return True  # Scissors beats paper
        elif player.human_move == "Scissors" and computer.computer_move == "Lizard":
            print("Scissors decapitates Lizard")
            return True  # Scissors beats lizard
        elif player.human_move == "Scissors" and computer.computer_move == "Spock":
            print("Spock smashes Scissors")
            return False  # Spock beats scissors

        # if player picks lizard
        elif player.human_move == "Lizard" and computer.computer_move == "Rock":
            print("Rock crushes Lizard")
            return False  # Rock beats lizard
        elif player.human_move == "Lizard" and computer.computer_move == "Paper":
            print("Lizard eats Paper")
            return True  # Lizard beats paper
        elif player.human_move == "Lizard" and computer.computer_move == "Scissors":
            print("Scissors decapitates Lizard")
            return False  # Scissors beats lizard
        elif player.human_move == "Lizard" and computer.computer_move == "Spock":
            print("Lizard poisons Spock")
            return True  # Lizard beats Spock

        # if player picks Spock
        elif player.human_move == "Spock" and computer.computer_move == "Rock":
            print("Spock vaporizes Rock")
            return True  # Spock beats rock
        elif player.human_move == "Spock" and computer.computer_move == "Paper":
            print("Paper disproves Spock")
            return False  # Paper beats Spock
        elif player.human_move == "Spock" and computer.computer_move == "Scissors":
            print("Spock smashes Scissors")
            return True  # Spock beats scissors
        elif player.human_move == "Spock" and computer.computer_move == "Lizard":
            print("Lizard poisons Spock")
            return False  # Lizard beats Spock


Run_game()
