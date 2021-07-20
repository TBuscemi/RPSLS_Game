import random
from player import Player
from human import Human
from computer import Computer


class Run_Game:

    def __init__(self):
        self.player = Human(Player)
        self.player2 = Human(Player)  # fix this maybe
        self.player2 = Computer()
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
            "Enter 1 to play against the computer; Enter 2 to play against another human: ")
        if game_type != "1" and game_type != "2":
            self.menu()

        if game_type == "1":
            self.player1 = Human("Player 1")
            self.player2 = Computer("Player 2")
            self.game_start()
        else:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")
            self.game_start()

    def game_start(self, player, player2):    # if player picks rocks
        player_score = 0
        player2_score = 0

        while player_score < 2 and player2_score < 2:

          
            
          
            self.player2.human_move = ""
            self.player.human_move = ""
            self.player2.computer_move = ""       # if player picks rock

            if self.player.human_move == self.player2.computer_move or self.player.human_move == self.player2.human_move:
                print("One of us should play better")
                
            if self.player.human_move == "Rock":     
                if self.player2.computer_move == "Paper" or self.player2.human_move == "Paper":
                    print("Paper covers Rock")
                    player2_score += 1  # Paper beats rock
                elif self.player2.computer_move == "Scissors" or self.player2.human_move == "Scissors":
                    print("Rock crushes Scissors")
                    player_score += 1 # Rock beats scissors
                elif self.player2.computer_move == "Lizard" or self.player2.human_move == "Lizard":
                    print("Rock crushes Lizard")
                    player_score += 1  # Rock beats lizard
                elif self.player2.computer_move == "Spock" or self.player2.human_move == "Spock":
                    print("Spock vaporizes Rock")
                    return False  # Spock beats roc
                        
                    # if player picks paper
            if self.player.human_move == "papper":     
                if self.player2.human_move == "Paper" or self.player2.computer_move == "Rock":
                    print("Paper covers Rock")
                    player_score += 1  # Paper beats rock
                elif self.player2.human_move == "Paper" or self.player2.computer_move == "Scissors":
                    print("Scissors cuts Paper")
                    player2_score += 1  # Scissors beats paper
                elif self.player2.human_move == "Paper" or self.player2.computer_move == "Lizard":
                    print("Lizard eats Paper")
                    player2_score += 1  # Lizard beats paper
                elif self.player2.human_move == "Paper" or self.player2.computer_move == "Spock":
                    print("Paper disproves Spock")
                    player_score += 1  # Paper beats Spock

                # if player picks Scissors
            if self.player.human_move == "Scissors":  
                if self.player2.human_move == "Scissors" or self.player2.computer_move == "Rock":
                    print("Rock crushes Scissors")
                    player2_score += 1  # Rock beats scissors
                elif self.player2.human_move == "Scissors" or self.player2.computer_move == "Paper":
                    print("Scissors cuts Paper")
                    player_score += 1  # Scissors beats paper
                elif self.player2.human_move == "Scissors" or self.player2.computer_move == "Lizard":
                    print("Scissors decapitates Lizard")
                    player_score += 1  # Scissors beats lizard
                elif self.player2.human_move == "Scissors" or self.player2.computer_move == "Spock":
                    print("Spock smashes Scissors")
                    player2_score += 1  # Spock beats scissors

                # if player picks lizard
            if self.player2.human_move == "Lizard":
                if self.player2.human_move == "Lizard" or self.player2.computer_move == "Rock":
                    print("Rock crushes Lizard")
                    player2_score += 1  # Rock beats lizard
                elif self.player2.human_move == "Lizard" or self.player2.computer_move == "Paper":
                    print("Lizard eats Paper")
                    player_score += 1  # Lizard beats paper
                elif self.player2.human_move == "Lizard" or self.player2.computer_move == "Scissors":
                    print("Scissors decapitates Lizard")
                    player2_score += 1  # Scissors beats lizard
                elif self.player2.human_move == "Lizard" or self.player2.computer_move == "Spock":
                    print("Lizard poisons Spock")
                    player_score += 1  # Lizard beats Spock

                # if player picks Spock
            if self.player.human_move == "Spock":    
                if self.player2.human_move == "Spock" or self.player2.computer_move == "Rock":
                    print("Spock vaporizes Rock")
                    player_score += 1  # Spock beats rock
                elif self.player2.human_move == "Spock" or self.player2.computer_move == "Paper":
                    print("Paper disproves Spock")
                    player2_score += 1  # Paper beats Spock
                elif self.player2.human_move == "Spock" or self.player2.computer_move == "Scissors":
                    print("Spock smashes Scissors")
                    player_score += 1  # Spock beats scissors
                elif self.player2.human_move == "Spock" or self.player2.computer_move == "Lizard":
                    print("Lizard poisons Spock")
                    player2_score += 1  # Lizard beats Spock
            
            if player_score == 2:
                print("Player 1 wins!")
                break
            
            elif player2_score == 2:
                print("Player 2 wins!")
                break    
