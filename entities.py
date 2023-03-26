class Entity:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.flag = True

    def attack(self, target):
        target.hp -= self.dmg
        print(self.name, 'attack the', target.name, 'and hit on', self.dmg, 'hit-points')
        return target.hp

    def dead_check(self, mas):
        if self.hp <= 0:
            print(self.name, 'is dead')
            mas.remove(self)
            return True
        return False

class Player(Entity):
    pass


class Mob(Entity):
    def __init__(self, name, hp, dmg):
        super().__init__(name, hp, dmg)
        self.flag = False
