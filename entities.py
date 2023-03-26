class Entity:
    def __init__(self, name: str, hp: int, dmg: int):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.flag = True
        self.__pos = [0,0]
        self.__prev_pos = [0,0]
    # TODO: make property decorators with @ for pos
    def get_pos(self):
        return self.__pos
    def set_pos(self,x: int,y: int):
        self.__prev_pos = self.__pos
        self.__pos = [x,y]
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
