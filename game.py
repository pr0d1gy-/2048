import os
import keypress
import thread
from field import Field
import sqlite3
import json

class Game(object):
    path = os.path.dirname(os.path.abspath(__file__))
    field = None
    score = 0
    moves = 0
    message = ''
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
        moves_ord = {65: 1, 66: 2, 68: 3, 67: 4}
        while not self.end:
            try:
                if keypress.char:
                    key_code = ord(keypress.char)
                    keypress.char = None

                    if key_code in moves_ord.keys():
                        self.score += self.field.move(moves_ord[key_code])
                        if not self.field.not_moved:
                            self.field.fill_random_cell(self.field.get_size() / 2)
                            self.moves += 1
                    elif key_code == 113:
                        self.end = 1
                    elif key_code == 115:
                        self.save_db()
                    elif key_code == 108:
                        self.load_db()
                    elif key_code == 110:
                        self.new_game()
                    else:
                        print key_code

                    self.print_game()

            except Exception, e:
                self.message = e.message

        print 'Game is over. You exited.'

    def save_db(self):
        print 'Saving...'
        try:
            db = sqlite3.connect('game.db')
            db.execute('''CREATE TABLE IF NOT EXISTS saves (
                        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        size INT NOT NULL,
                        score INT NOT NULL,
                        moves INT NOT NULL,
                        field VARCHAR(1000) NOT NULL
                        )''')

            db.execute('''INSERT INTO saves (size, score, moves, field) VALUES (%d, %d, %d, "%s")''' % (
                self.field.get_size(),
                self.score,
                self.moves,
                json.dumps(self.field.cells)
            ))

            db.commit()

            self.message = 'Saved!'

        except Exception, e:
            self.message = e.message
        finally:
            if db:
                db.close()

    def load_db(self):
        print 'Loading..'
        try:
            db = sqlite3.connect('game.db')
            result = db.execute('''SELECT * FROM saves ORDER BY id DESC LIMIT 1''').fetchone()

            self.field.clear_cells()
            self.field.set_size(int(result[1]))
            self.field.create_empty_field()
            self.score = int(result[2])
            self.moves = int(result[3])

            self.field.cells = json.loads(result[4])

            self.message = 'Loaded.'

        except Exception, e:
            self.message = e.message
        finally:
            if db:
                db.close()

    def save(self):
        print 'saving...'
        try:
            f = open(self.path + '/game.save', 'w')

            raw = str(self.field.get_size()) \
                + '\n' + str(self.score) \
                + '\n' + str(self.moves) \
                + '\n'

            for y in self.field.get_size_range():
                raw += ','.join(['%s' % i for i in self.field.get_line(y)])
                raw += '\n'

            f.write(raw)
            self.message = 'Saved!'
        except Exception, e:
            self.message = e.message
        finally:
            f.close()

    def load(self):
        print 'loading...'
        try:
            f = open(self.path + '/game.save', 'r')
            lines = f.readlines()

            size = int(lines[0])
            if size != len(lines) - 3:
                raise Exception, 'Invalid save.'

            self.field.clear_cells()
            self.field.set_size(size)
            self.field.create_empty_field()
            self.score = int(lines[1])
            self.moves = int(lines[2])

            for i in xrange(3, len(lines)):
                self.field.set_line(i - 3, [int(j) for j in lines[i].replace('\n', '').split(',')])

            self.message = 'Loaded.'
        except Exception, e:
            self.message = e.message
        finally:
            f.close()

    def new_game(self):
        self.field.create_empty_field()
        self.field.fill_random_cell(self.field.get_size() / 2)
        self.score = 0
        self.moves = 0

    def print_message(self):
        if self.message:
            self.print_sep()
            print self.message
            self.message = ''

    def print_game(self):
        self.clear_console()
        self.print_score()
        self.print_field()
        self.print_message()

        if self.field.is_filled() and not self.field.is_move_exist():
            self.end = 1
            print 'You lose.'

        if self.field.is_won_game():
            self.end = 1
            print 'You won.'

        self.print_rules()
        self.print_sep()

    def print_rules(self):
        self.print_sep()
        print 'Move - ARROWS' \
            + '\nExit - Q' \
            + '\nSave - S' \
            + '\nLoad - L' \
            + '\nNew - N'

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

except Exception, e:
    print e.message
