class Player:

    def __init__(self, name):
        self.name = name  # should be the player name (ex: Player 1)
        self.chosen_gesture = None  # there's no gesture that's been chosen yet
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.wins = 0
        self.wins_against = []  # the wins_against is appended to this array
        self.human_move = ""

    def add_win(self):
        player_score = 0
        player2_score = 0

        while player_score < 2 and player2_score < 2:

            # if player picks rock

            self.gesture_choices(Player)

            if self.player.human_move == self.player2.computer_move or self.player.human_move == self.player2.human_move:
                print("One of us should play better")

        if self.player.human_move == "Rock":
            if self.player2.computer_move == "Paper" or self.player2.human_move == "Paper":
                print("Paper covers Rock")
                player2_score += 1  # Paper beats rock
            elif self.player2.computer_move == "Scissors" or self.player2.human_move == "Scissors":
                print("Rock crushes Scissors")
                player_score += 1  # Rock beats scissors
            elif self.player2.computer_move == "Lizard" or self.player2.human_move == "Lizard":
                print("Rock crushes Lizard")
                player_score += 1  # Rock beats lizard
            elif self.player2.computer_move == "Spock" or self.player2.human_move == "Spock":
                print("Spock vaporizes Rock")
                return False  # Spock beats rock
            # if player picks paper:
        if self.player.human_move == "paper":
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

        elif player2_score == 2:
            print("Player 2 wins!")

    # def wins_against(self, gesture):
    #     if gesture == "Rock":  # if this is used
    #         self.wins_against.append("Scissors")  # it beats these
    #         self.wins_against.append("Lizard")
    #     if gesture == "Paper":
    #         self.wins_against.append("Rock")
    #         self.wins_against.append("Spock")
    #     if gesture == "Scissors":
    #         self.wins_against.append("Paper")
    #         self.wins_against.append("Lizard")
    #     if gesture == "Lizard":
    #         self.wins_against.append("Paper")
    #         self.wins_against.append("Spock")
    #     if gesture == "Spock":
    #         self.wins_against.append("Rock")
    #         self.wins_against.append("Scissors")
