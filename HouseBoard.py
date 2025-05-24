import random

class house_board:
    def __init__(self, player_names):
        self.player_names = player_names
        self.number_of_players = len(player_names)
        self.player_numbers = {}

    def display_player_info(self):
        for i in range(len(self.player_names)):
            print(self.player_names[i])
        print(self.number_of_players)

def assign_random_numbers(self):
    for i in range(len(self.player_names)):
        l = []
        for j in range(5):
            l.append(random.randrange(0, 100))
        self.player_numbers[self.player_names[i]] = l


game = house_board(["nithran", "sanjay"])

game.display_player_info()
game.assign_random_numbers()
print(game.player_numbers.values())
