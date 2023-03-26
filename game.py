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
        self.clear_field = self.game_field
        print('im new game')

    def show_field(self):
        for i in range(0,len(self.game_field)):
            print(self.game_field[i])
    def update_field(self):
        self.game_field = self.clear_field
        for player in self.players:
            self.game_field[player.pos[0]][player.pos[1]] = 'P'
        for mob in self.mobs:
            self.game_field[mob.pos[0]][mob.pos[1]] = 'M'
    def start_game(self):
        self.__players_start_positioning()
        self.__mobs_start_positioning()
        while len(self.players) != 0 and len(self.mobs) != 0:
            old_field = self.game_field
            self.update_field()
            # if self.game_field != old_field:
            self.show_field()

        print('im main game loop')

    def __players_start_positioning(self):
        for player in self.players:
            for x in range(0, len(self.game_field)):
                for y in range(0, len(self.game_field[x])):
                    if self.game_field[x][y] == '0':
                        player.pos = [x, y]
                        self.game_field[x][y] = 'P'
                    else:
                        continue

    def __mobs_start_positioning(self):
        for mob in self.mobs:
            for x in range(len(self.game_field) - 1, -1, -1):
                for y in range(len(self.game_field[0]) - 1, -1,-1):
                    if self.game_field[x][y] == '0':
                        mob.pos = [x, y]
                        self.game_field[x][y] = 'M'
                    else:
                        break




class UserController:
    def __init__(self):
        print('im user')