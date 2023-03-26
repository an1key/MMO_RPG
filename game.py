import time
class GameController:
    def __init__(self, field_size_x: int, field_size_y: int, players: list, mobs: list):
        self.players = players
        self.mobs = mobs
        self.all_cre = [self.players, self.mobs]
        self.clear_field = []
        self.field_filling = '*'
        for i in range(field_size_y):
            self.clear_field.append([])
            for j in range(field_size_x):
                self.clear_field[i].append(self.field_filling)
        self.game_field = self.clear_field
        print('im new game')

    def show_field(self):
        print('=============')
        for i in range(0, len(self.game_field)):
            print('|', *self.game_field[i], '|')
        print('=============')

    def update_field(self):
        self.game_field = self.clear_field
        for player in self.players:
            if player.get_pos() != player.get_prev_pos() and self.game_field[player.get_prev_pos()[1]][player.get_prev_pos()[0]] == 'P':
                self.game_field[player.get_prev_pos()[1]][player.get_prev_pos()[0]] = self.field_filling
            self.game_field[player.get_pos()[1]][player.get_pos()[0]] = 'P'
        for mob in self.mobs:
            if mob.get_pos() != mob.get_prev_pos() and self.game_field[mob.get_prev_pos()[1]][mob.get_prev_pos()[0]] == 'M':
                self.game_field[mob.get_prev_pos()[1]][mob.get_prev_pos()[0]] = self.field_filling
            self.game_field[mob.get_pos()[1]][mob.get_pos()[0]] = 'M'

    def start_game(self):
        old_field = self.clear_field
        if (len(self.players) + len(self.mobs)) > (len(self.game_field) * len(self.game_field[0])):
            print('Error: Too much entities, cannot place them all.')
            return
        self.__players_start_positioning()
        self.__mobs_start_positioning()
        for player in self.players:
            player.update_prev_pos()
        self.update_field()
        self.show_field()
        while len(self.players) != 0 and len(self.mobs) != 0:
            for player in self.players:
               self.move_entity(player, 1, 1)
            self.update_field()
            # if self.game_field != old_field:
            self.show_field()
            for i in self.all_cre:
                for entity in i:
                    entity.update_prev_pos()
            time.sleep(0.5)

        print('im main game loop')

    def __players_start_positioning(self):
        for player in self.players:
            try:
                for y in range(0, len(self.game_field)):
                    for x in range(0, len(self.game_field[0])):
                        if self.game_field[y][x] == self.field_filling:
                            player.set_pos(x, y)
                            self.game_field[y][x] = 'P'
                            raise
                        else:
                            continue

            except:
                pass

    def __mobs_start_positioning(self):
        for mob in self.mobs:
            try:
                for y in range(len(self.game_field) - 1, -1, -1):
                    for x in range(len(self.game_field[0]) - 1, -1, -1):
                        if self.game_field[y][x] == self.field_filling:
                            mob.set_pos(x, y)
                            self.game_field[y][x] = 'M'
                            raise
                        else:
                            continue
            except:
                pass

    def move_entity(self, entity: object, delta_x: int, delta_y: int):
        try:
            if entity.current_od < 1:
                print('You don`t have enough action points')
                raise
            if self.game_field[entity.get_pos()[0] + delta_x][entity.get_pos()[1] + delta_y] != self.field_filling:
                print('This cell is already busy')
                raise
            if entity.get_pos()[0] + delta_x < 0 or entity.get_pos()[0] + delta_x >= len(self.game_field[0]) or entity.get_pos()[1] + delta_y < 0 or entity.get_pos()[1] + delta_y >= len(self.game_field):
                print('This cell is outside the field')
                raise

            entity.move(delta_x, delta_y)
            entity.current_od -= 1

        except Exception as exc:
            print (exc)
            print('you cannot move there')


class UserController:
    def __init__(self):
        print('im user')
