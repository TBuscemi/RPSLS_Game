# # def how_many_players():
# #     user_input = input("would you like to play with a friend or vs the AI")
# #     if(user_input.lower() =="friend"):
# #         #take them to playing with friends
# #     if(user_input.lower() == "ai"):
# #         #take them to playing with ai 

# # ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]
# # p1 = 0
# # p2 = 0



# # def rock(input_1, input_2):
# #     if(input_1 == "rock" and input_2 == "scissors"):

# # MIGHT MAKE THE INPUT AN NUMBER TO IT WILL MATCH UP WITH A LIST
# # player_input = ""
# def player_move():
#     player_input = input("Please choose an option?\nROCK\nPAPER\nSCISSORS\nSPOCK\nLIZARD")
#     if(player_input.lower == "rock"):
#         player_input = "rock"
#     elif(player_input.lower == "paper"):
#         player_input = "paper"
#     elif(player_input.lower == "scissors"):
#         player_input =  "scissors" 
#     elif(player_input.lower == "spock"):
#         player_input = "spock"
#     elif(player_input.lower == "lizard"):
#         player_input = "lizard"     
#     else:
#         print("Hmmmm looks woops try again!")
#         player_move()

# p1 = 0
# p2 = 0
# user_1 = "rock"
# user_2 = "paper"

# # ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]
# def who_wins():
#     if(user_1 == user_2):
#         print("no one wins")
#     if(user_1 == "rock"):
#         if(user_2 == "scissors"):
#             print("rock smashes scissors you win #1!")
#             return p1 + 1    
#         elif(user_2 == "paper"):
#             print("paper covers rock you win #2")
#             return p2 + 1
#         elif(user_2 == "spock"):
#             print("spock vaporizes rock you win #2!")
#             return p2 + 1
#         elif(user_2 == "lizard"):
#             print("rock crushes lizard you win #1!")
#             return p1 + 1 
#     if(user_1 == "paper"):
#         if(user_2 == "rock"):
#             print("paper covers rock you win #1!")
#             return p1 + 1
#         elif(user_2 == "scissors"):
#             print("scissors cuts papper you win #2!")    
#             return p2 + 1
#         elif(user_2 == "lizard"):
#             print("lizard eats paper you win #2!")
#             return p2 + 1
#         elif(user_2 == "spock"):
#             print("paper disproves spock you win #1!")
#             return p1 + 1   
#     if(user_1 == "scissors"):
#         if(user_2 == "rock"):
#             print("rock crushes scissors you win #2!")
#             return p2 + 1
#         elif(user_2 == "papper"):
#             print("scissors cut paper you win #1!")
#             return p1 + 1
#         elif(user_2 == "lizard"):
#             print("scissors decapitates lizard you win #1!")
#             return p1 + 1
#         elif(user_2 == "spock"):
#             print("spock smashes scissors you win #2!")
#             return p2 + 1
#     if(user_1 == "lizard"):
#         if(user_2 == "rock"):
#             print("rock smashes lizard you win #2!")
#             return p2 + 1
#         elif(user_2 == "paper"):
#             print("lizard eats papper you win #1!")
#             return p1 + 1
#         elif(user_2 == "scissors"):
#             print("scissors decapitates lizard you win#2!")
#             return p2 + 1
#         elif(user_2 == "spock"):
#             print("lizard poisons spock you win #1!")
#             return p1 + 1 
#     if(user_1 == "spock"):
#         if(user_2 == "rock"):
#             print("spock vaporizes rock you win #1!")
#             return p1 + 1
#         elif(user_2 == "paper"):
#             print("paper disproves spock you win #2")
#             return p2 + 1
#         elif(user_2 == "scissors"):
#             print("spock smashes scissors you win #1!")
#             return p1 + 1
#         elif(user_2 == "lizard"):
#             print("lizard poisons spock you win #2")
#             return p2 + 1


# def win_condition():
#     while(p1 <= 2 and p2 <= 2):
#         #restart the input move function
#     if(p1 == 2):
        
        




# print(p1)
# print(p2)


# who_wins()
# print(p1)
# print(p2)




from human import Human
from computer import Computer
from player import Player

#     # instantiating human and computer objects:
# def single_player_round(self):
#     player = Human()
#     player2 = Computer()



# player_score = 0
# player2_score = 0
# player2.human_move ="Scissors" 

class game_start:
   
    
    def __init__(self):
        self.player = Human(Player)
        self.player2 = Human(Player)
        self.player2 = Computer()
    
    #hello intro

    #rules
    # 
    # one or 2 player
    # 
    #    
    
    def comparing_gestures(self):
        player_score = 0
        player2_score = 0
        
        
        
        
        
        while player_score < 2 and player2_score < 2:

            self.player2.human_move ="" 
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


game_start().comparing_gestures()
