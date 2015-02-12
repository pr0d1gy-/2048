import os
import sys
import keypress
import thread
from field import Field


class Game(object):
    field = None
    score = 0
    moves = 0
    error = ''
    end = 0

    COLOR_DIGITS = {
        0: '\033[1;30m-\033[1;m',
        2: '\033[1;34m2\033[1;m',
        4: '\033[1;35m4\033[1;m',
        8: '\033[1;37m8\033[1;m',
        16: '\033[1;36m16\033[1;m',
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
        self.field = Field(self.input_size())
        self.play()

    def play(self):
        self.print_game()

        thread.start_new_thread(keypress.keypress, ())

        moves = {'w': 1, 's': 2, 'a': 3, 'd': 4}

        while True:
            if keypress.char:
                if keypress.char == 'q':
                    break
                elif keypress.char in moves.keys():
                    self.score += self.field.move(moves[keypress.char])
                    self.moves += 1
                    self.field.fill_random_cell(1)
                    self.print_game()
                    keypress.char = None
                else:
                    print keypress.char
                    keypress.char = None

    def print_error(self):
        if self.error:
            self.print_sep()
            print self.error
            self.error = ''

    def print_game(self):
        self.clear_console()
        self.print_score()
        self.print_field()
        self.print_error()

        if not self.field.is_move_exist():
            exit()

        self.print_sep()

    def print_sep(self):
        print '-' * (self.field.get_size() * 7)

    def print_score(self):
        self.print_sep()
        print 'Score: %s | Moves: %s' % (self.score, self.moves)

    @staticmethod
    def input_size():
        size = raw_input('Enter size of field, 5?: ')
        if not size:
            size = 5
        else:
            size = int(size)

        if 0 > size or size > 25:
            raise AttributeError, 'Size of field must be 0..25'

        return size

    @staticmethod
    def clear_console():
        os.system('clear')

    def print_field(self):
        self.print_sep()
        for y in xrange(len(self.field.cells)):
            print ' ' * 5 + ''.join(
                ['{0:{width}}'.format(self.COLOR_DIGITS[x], width=18) for x in self.field.get_line(y)])


try:

    game = Game()

except:
    print sys.exc_info()[1]
