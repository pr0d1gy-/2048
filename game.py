# -*- coding: UTF-8 -*-
import sys
import random
from field import Field


class Game(object):

    field = None
    score = 0
    moves = 0

    COLOR_DIGITS = {
        0: '0',
        2: '2',
        4: '4',
        8: '8',
        16: '\033[1;38m16\033[1;m',
        32: '\033[1;38m32\033[1;m',
        64: '\033[1;37m64\033[1;m',
        128: '\033[1;35m128\033[1;m',
        256: '\033[1;36m256\033[1;m',
        512: '\033[1;34m512\033[1;m',
        1024: '\033[1;32m1024\033[1;m',
        2048: '\033[1;33m2048\033[1;m',
        4096: '\033[1;31m4096\033[1;m',
        8192: '\033[1;31m8192\033[1;m'
    }

    def __init__(self):
        self.field = Field(5)
        self.print_field()

    def print_field(self):
        for y in xrange(len(self.field.cells)):
            print ', '.join(self.COLOR_DIGITS[x * 512] for x in self.field.get_line(y))


game = Game()

# try:
#
#     score = 0
#     moves = 0
#     ways = 'LEFT'
#     field = Field()
#     for y in field.cells:
#         print y
#
#     for moves in xrange(2000):
#         if not field.is_move_exist():
#             break
#
#         ways = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
#         score += field.move(getattr(field, ways))
#         field.fill_random_cell(1)
#
#     print '\n\n'
#     print 'Moves: ' + str(moves)
#     print 'Score: ' + str(score)
#     print 'Last Way: ' + str(ways)
#     for y in field.cells:
#         print y
#
# except:
#     print sys.exc_info()[1]
