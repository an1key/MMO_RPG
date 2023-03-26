class GameController:
    def __init__(self, field_size_x: int, field_size_y: int, players: list, mobs: list):
        self.players = players
        self.mobs = mobs
        self.all_cre = [self.players, self.mobs]
        self.clear_field = []
        for i in range(field_size_y):
            self.clear_field.append([])
            for j in range(field_size_x):
                self.clear_field[i].append('0')
        self.game_field = self.clear_field
        print('im new game')

    def show_field(self):
        print('=========================')
        for i in range(0,len(self.game_field)):
            print(self.game_field[i])
        print('=========================')
    def update_field(self):
        self.game_field = self.clear_field
        for player in self.players:
            self.game_field[player.get_pos()[0]][player.get_pos()[1]] = 'P'
        for mob in self.mobs:
            self.game_field[mob.get_pos()[0]][mob.get_pos()[1]] = 'M'
    def start_game(self):
        old_field = self.clear_field
        if (len(self.players) + len(self.mobs)) > (len(self.game_field) * len(self.game_field[0])):
            print('Error: Cannot place all entities. Goodbye.')
            return
        self.__players_start_positioning()
        self.__mobs_start_positioning()
        while len(self.players) != 0 and len(self.mobs) != 0:
            self.update_field()
            # if self.game_field != old_field:
            self.show_field()

        print('im main game loop')
    def __players_start_positioning(self):
        for player in self.players:
            try:
                for x in range(0, len(self.game_field)):
                    for y in range(0, len(self.game_field[x])):
                        if self.game_field[x][y] == '0':
                            player.set_pos(x,y)
                            self.game_field[x][y] = 'P'
                            raise
                        else:
                            continue
            except: pass



    def __mobs_start_positioning(self):
        for mob in self.mobs:
            try:
                for x in range(len(self.game_field) - 1, -1, -1):
                    for y in range(len(self.game_field[0]) - 1, -1,-1):
                        if self.game_field[x][y] == '0':
                            mob.set_pos(x,y)
                            self.game_field[x][y] = 'M'
                            raise
                            break
                        else:
                            continue
            except: pass




class UserController:
    def __init__(self):
        print('im user')