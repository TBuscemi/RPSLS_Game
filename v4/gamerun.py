from human import Human
from computer import Computer


class Run_Game:

    def __init__(self):
        self.player1 = Human()
        self.player2 = Human()  # fix this maybe
        self.player_ai = Computer()
        
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
            self.player1 = Human()
            self.player_ai = Computer()
            self.game_start(game_type)
        else:
            self.player1 = Human()
            self.player2 = Human()
            self.game_start(game_type)

    def game_start(self,game_type):    # if player picks rocks
        player_score = 0
        player2_score = 0
        game_type
        while player_score < 2 and player2_score < 2:
            player1_gesture = ""
            player2_gesture = ""
            print("P1 Score")
            print(player_score)
            print("P2 Score")
            print(player2_score)
            
            
            
            player1_gesture = self.player1.choose_gesture()
            print("Player 1 Throws Out! "+player1_gesture)
           
            if game_type == "1":
                player2_gesture = self.player_ai.choose_gesture()
                print("Player 2 Throws Out! "+player2_gesture)
            elif game_type == "2":
                player2_gesture = self.player2.choose_gesture()
                print("Player 2 Throws Out! "+player2_gesture)
      

            if player1_gesture == player2_gesture:
                print("One of us should play better")
                
            if  player1_gesture == "Rock":     
                if player2_gesture == "Paper":
                    print("Paper covers Rock")
                    player2_score += 1  # Paper beats rock
                elif player2_gesture == "Scissors":
                    print("Rock crushes Scissors")
                    player_score += 1 # Rock beats scissors
                elif player2_gesture == "Lizard":
                    print("Rock crushes Lizard")
                    player_score += 1  # Rock beats lizard
                elif player2_gesture == "Spock":
                    print("Spock vaporizes Rock")
                    player2_score += 1
                      # Spock beats roc
                        
                    # if player picks paper
            if  player1_gesture == "papper":     
                if player2_gesture == "Rock":
                    print("Paper covers Rock")
                    player_score += 1  # Paper beats rock
                elif player2_gesture == "Scissors":
                    print("Scissors cuts Paper")
                    player2_score += 1  # Scissors beats paper
                elif player2_gesture == "Lizard":
                    print("Lizard eats Paper")
                    player2_score += 1  # Lizard beats paper
                elif player2_gesture == "Spock":
                    print("Paper disproves Spock")
                    player_score += 1  # Paper beats Spock

                # if player picks Scissors
            if  player1_gesture == "Scissors":  
                if  player2_gesture == "Rock":
                    print("Rock crushes Scissors")
                    player2_score += 1  # Rock beats scissors
                elif player2_gesture == "Paper":
                    print("Scissors cuts Paper")
                    player_score += 1  # Scissors beats paper
                elif player2_gesture == "Lizard":
                    print("Scissors decapitates Lizard")
                    player_score += 1  # Scissors beats lizard
                elif player2_gesture == "Spock":
                    print("Spock smashes Scissors")
                    player2_score += 1  # Spock beats scissors

                # if player picks lizard
            if  player1_gesture == "Lizard":
                if player2_gesture == "Rock":
                    print("Rock crushes Lizard")
                    player2_score += 1  # Rock beats lizard
                elif player2_gesture == "Paper":
                    print("Lizard eats Paper")
                    player_score += 1  # Lizard beats paper
                elif player2_gesture == "Scissors":
                    print("Scissors decapitates Lizard")
                    player2_score += 1  # Scissors beats lizard
                elif player2_gesture == "Spock":
                    print("Lizard poisons Spock")
                    player_score += 1  # Lizard beats Spock

                # if player picks Spock
            if  player1_gesture == "Spock":    
                if  player2_gesture == "Rock":
                    print("Spock vaporizes Rock")
                    player_score += 1  # Spock beats rock
                elif player2_gesture == "Paper" :
                    print("Paper disproves Spock")
                    player2_score += 1  # Paper beats Spock
                elif player2_gesture == "Scissors" :
                    print("Spock smashes Scissors")
                    player_score += 1  # Spock beats scissors
                elif player2_gesture == "Spock" :
                    print("Lizard poisons Spock")
                    player2_score += 1  # Lizard beats Spock
            
            if  player_score == 2:
                print("Player 1 wins!")
                break
            
            elif player2_score == 2:
                print("Player 2 wins!")
                break 
Run_Game().start()