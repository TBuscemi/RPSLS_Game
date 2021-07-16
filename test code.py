# def how_many_players():
#     user_input = input("would you like to play with a friend or vs the AI")
#     if(user_input.lower() =="friend"):
#         #take them to playing with friends
#     if(user_input.lower() == "ai"):
#         #take them to playing with ai 

# ["ROCK","PAPER","SCISSORS","LIZARD","SPOCK"]
# p1 = 0
# p2 = 0



# def rock(input_1, input_2):
#     if(input_1 == "rock" and input_2 == "scissors"):

# MIGHT MAKE THE INPUT AN NUMBER TO IT WILL MATCH UP WITH A LIST
# player_input = ""
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

p1 = 0
p2 = 0
user_1 = ""
user_2= ""


def who_win():
    if(user_1 == user_2):
        print("no one wins")
    if(user_1 == "rock"):
        elif(user_2 == "scissors"):
            print("rock smashes scissors you win #1!")
            return p1 + 1    
        elif(user_2 == "paper"):
            print("paper covers rock you win #2")
            return p2 + 1
        elif(user_2 == "spock"):
            print("spock vaporizes rock you win #2!")
            return p2 + 1
        elif(user_2 == "lizard"):
            print("rock crushes lizard you win #1!")
            return p1 + 1 
    elif(user_1 == "papper"):
