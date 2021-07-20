import random
from player import Player
from human import Human
from computer import Computer


class Run_Game:

    def __init__(self):
        self.player = Player("Player 1")
        self.player2 = Player("Player 2")  # fix this maybe
        self.best_of = 3
        pass

    def start(self):
        print("GREETINGS PROFESSOR FALKEN "
              "\nSHALL WE PLAY A GAME?* "
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
              "\nEach gesture thrown beats two other gestures, and in turn can be beat by two. \n"
              "\n"
              "\n* game is limited to Rock Paper Scissors Lizard Spock."
              "\nGlobal Thermonuclear War is currently out of order.")  # just for the laughs from old people
        self.menu()

    def menu(self):
        game_type = input(
            "Enter 1 to play against the computer; Enter 2 to play against a friend: ")
        while game_type != "1" and game_type != "2":
            game_type = input(
                "Invalid. Enter 1 to play against the computer; Enter 2 to play against a friend: ")

        if game_type == "1":
            self.player = Human("Player 1")
            self.player2 = Computer("Player 2")
            self.game_start()
        else:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")
            self.game_start()

    def game_start(self):    # if player picks rocks
        self.player.add_win()
        self.player.human_move = ""
        #self.player2.human_move = ""
        player_score = 0
        player2_score = 0

        # while player_score < 2 and player2_score < 2:

        #     self.player2.human_move = ""
        #     self.player.human_move = ""
        #     self.player2.computer_move = ""       # if player picks rock

        #     self.gesture_choices(Human)

        #     if self.player.human_move == self.player2.computer_move or self.player.human_move == self.player2.human_move:
        #         print("One of us should play better")

        # if self.player.human_move == "Rock":
        #     if self.player2.computer_move == "Paper" or self.player2.human_move == "Paper":
        #         print("Paper covers Rock")
        #         player2_score += 1  # Paper beats rock
        #     elif self.player2.computer_move == "Scissors" or self.player2.human_move == "Scissors":
        #         print("Rock crushes Scissors")
        #         player_score += 1  # Rock beats scissors
        #     elif self.player2.computer_move == "Lizard" or self.player2.human_move == "Lizard":
        #         print("Rock crushes Lizard")
        #         player_score += 1  # Rock beats lizard
        #     elif self.player2.computer_move == "Spock" or self.player2.human_move == "Spock":
        #         print("Spock vaporizes Rock")
        #         return False  # Spock beats rock
game = Run_Game()
game.start()
