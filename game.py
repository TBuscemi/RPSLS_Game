from os import system, name
from player import Player
from human import Human
from computer import Computer


class Game:

    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        pass

    def start(self):
        print("\nGREETINGS PROFESSOR FALKEN "
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
              "Best two out of three wins..good luck!\n"
              "\n* game is limited to Rock Paper Scissors Lizard Spock."
              "\nGlobal Thermonuclear War is currently out of order.\n")
        self.game_type()

    def game_type(self):
        player_mode = int(input(
            "\nEnter 1 to play against the computer; Enter 2 to play against another human: "))
        while player_mode != 1 and player_mode != 2:
            player_mode = int(input(
                "Invalid. Enter 1 to play against the computer; Enter 2 to play against another human: "))
        if player_mode == 1:
            self.player1 = Human("Player 1")
            self.player2 = Computer("Player 2")
            self.start_game()
        else:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")
            self.start_game()

    def start_game(self):
        while self.player1.player_score < 2 and self.player2.player_score < 2:
            self.player1.gesture_beats = []
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            self.show_gestures()
            self.compare_gestures()
            self.display_score()
        self.winner()
        self.start()

    def show_gestures(self):
        print("\nPlayer 1 chose " +
              self.player1.gesture_list[self.player1.gesture_choice - 1] + ".")
        print("Player 2 chose " +
              self.player2.gesture_list[self.player2.gesture_choice - 1] + ".")

    def compare_gestures(self):
        if self.player1.gesture_choice == self.player2.gesture_choice:
            print("\nIt's a tie. No points awarded.")
            return
        round_point = False
        for i in self.player1.gesture_beats:
            if i == self.player2.gesture_choice:
                round_point = True
        if round_point == True:
            print("\nPlayer 1 wins the round.")
            self.player1.score()
        else:
            print("\nPlayer 2 wins the round.")
            self.player2.score()

    def display_score(self):
        print("\nPlayer 1 score: " + str(self.player1.player_score))
        print("Player 2 score: " + str(self.player2.player_score))

    def clear(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def winner(self):
        if self.player1.player_score > self.player2.player_score:
            print("\n.·: * :· Player 1 is the winner! .·: * :·\n")
        else:
            print("\n.·: * :· Player 2 is the winner! .·: * :·\n")
