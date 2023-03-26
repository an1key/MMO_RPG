from entities import Player, Mob
from game import GameController
import random

# all_cre = [[Player('KINNG', 50, 15)],
#            [Mob('Insipid', 10, 5),
#            Mob('Boris', 30, 10),
#             Mob('Destroyer', 100, 1)]]
#
# while len(all_cre[0]) != 0 and len(all_cre[1]) != 0:
#     for i in all_cre:
#         for i1 in i:
#             if i1.flag:
#                 if isinstance(i1, Player):
#                     target_i = random.randint(0, len(all_cre[1]) - 1)
#                     i1.attack(all_cre[1][target_i])
#                     if all_cre[1][target_i].dead_check(all_cre[1]):
#                         break
#                     i1.flag = False
#                     for i in all_cre[1]:
#                         i.flag = True
#                 else:
#                     i1.attack(all_cre[0][0])
#                     if all_cre[0][0].dead_check(all_cre[0]):
#                         break
#                     i1.flag = False
#                     for flag in all_cre[1]:
#                         if flag.flag:
#                             break
#                         all_cre[0][0].flag = True
#
# if len(all_cre[0]) == 0:
#     print('Mobs won')
#
# if len(all_cre[1]) == 0:
#     print('Player won')

game = GameController(10,10,
                      [Player('KINNG', 50, 15, 1000),Player('BORIS', 100, 20, 1000)],
                      [Mob('Insipid', 10, 5, 1000), Mob('Prikolist',10,5,1000)])
game.start_game()
print('finished')