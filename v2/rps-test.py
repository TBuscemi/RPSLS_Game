# THIS FILE CANE BE DELETED..I was following a tutorial

# importing random module

import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Create subclass that plays randomly


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# Create subclass Human Player that asks for input


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Please enter your move:").lower()
            if human_move.lower() not in moves:
                print("Available moves: Rock, Paper, Scissors")
                print("Please enter a move from the list and try again.")
            else:
                break
        return human_move.lower()

# Create a Reflected Player class that plays the opponents last move next


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = random.choice(moves)

    def move(self):
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move

# Create a Cycle Player class that cycles through the moves


class CyclePlayer(Player):
    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.next_move = "paper"
        elif my_move == "paper":
            self.next_move = "scissors"
        else:
            self.next_move = "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    # Add score at start of game
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player One wins")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player Two wins")
        else:
            print("It's a tie")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        valid_input = False
        rounds = 0
        while valid_input is False:
            user_rounds = input("How many rounds do you want to play?:")
            try:
                rounds = int(user_rounds)
                valid_input = True
            except ValueError:
                print("Please enter a valid number")

        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()
            print(f"'Score: Player One:{self.p1_score}'\
                '; Player Two:{self.p2_score}'")
        if self.p1_score > self.p2_score:
            print("Player One Wins")
        elif self.p2_score > self.p1_score:
            print("Player Two Wins")
        else:
            print("Everybody wins!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
