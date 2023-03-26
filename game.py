class GameController:
    def __init__(self, field_size_x: int, field_size_y: int, players: list, mobs: list):
        self.players = players
        self.mobs = mobs
        self.all_cre = [self.players, self.mobs]
        self.game_field = []
        for i in range(field_size_y):
            self.game_field.append([])
            for j in range(field_size_x):
                self.game_field[i].append('0')
        print('im new game')
    def show_field(self):
        for i in range(0,len(self.game_field)):
            print(self.game_field[i])
class UserController:
    def __init__(self):
        print('im user')