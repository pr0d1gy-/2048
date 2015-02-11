# -*- coding: UTF-8 -*-
import sys
import random
from field import Field


try:

    score = 0
    moves = 0
    ways = 'LEFT'
    field = Field()
    for y in field.cells:
        print y

    for moves in xrange(2000):
        if not field.is_move_exist():
            break

        ways = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        score += field.move(getattr(field, ways))
        field.fill_random_cell(1)

    print '\n\n'
    print 'Moves: ' + str(moves)
    print 'Score: ' + str(score)
    print 'Last Way: ' + str(ways)
    for y in field.cells:
        print y

except:
    print sys.exc_info()[1]
