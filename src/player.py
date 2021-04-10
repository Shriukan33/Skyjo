class Player:

    player_list = []
    def __init__(self, player_num, name):
        self.player_list.append(self) # List to cycle through instances of Player
        self.player_num = player_num  # player number: 1, 2, 3 or 4
        self.name = name
        self.score = 0


    def __repr__(self):
        return str(self.name)
