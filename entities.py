class Entity:
    def __init__(self, name: str, hp: int, dmg: int, od = 1):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.max_od = od
        self.current_od = od
        self.flag = True
        self._pos = [0, 0]
        self._prev_pos = []

    def get_prev_pos(self):
        return self._prev_pos
    # TODO: make property decorators with @ for pos

    def get_pos(self):
        return self._pos

    def set_pos(self, x: int, y: int):
        self._prev_pos = self._pos
        self._pos = [x, y]

    def update_prev_pos(self):
        self._prev_pos = self._pos
    def move(self, delta_x: int, delta_y: int):
        current_pos = self.get_pos()
        self.set_pos(current_pos[0]+delta_x, current_pos[1]+delta_y)

    def attack(self, target: object):
        target.hp -= self.dmg
        print(self.name, 'attack the', target.name, 'and hit on', self.dmg, 'hit-points')
        return target.hp

    def dead_check(self, mas: list):
        if self.hp <= 0:
            print(self.name, 'is dead')
            mas.remove(self)
            return True
        return False


class Player(Entity):
    pass


class Mob(Entity):
    def __init__(self, name: str, hp: int, dmg: int):
        super().__init__(name, hp, dmg)
        self.flag = False
