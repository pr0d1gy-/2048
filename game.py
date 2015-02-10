from field import Field


class Game(Field):

    acts = {
        'Up': ['u', 'up', '1'],
        'Down': ['d', 'down', '2'],
        'Left': ['l', 'left', '3'],
        'Right': ['r', 'right', '4']
    }

    def __init__(self):
        isMore = 1
        while isMore:
            self.actions('l')
            self.clearConsole()
            print 'Type field size with comma separate\n or enter twice:'
            print '5,5 ?'
            xy = raw_input()

            if not xy:
                x = 5
                y = 5
            else:
                if ',' in xy:
                    (x, y) = xy.split(',')
                else:
                    x = xy
                    print '\nX-axis: ' + x + '\nType Y-axis:\n'
                    y = raw_input()

            Field.__init__(self, x, y)
            self.fillRandomEmptyPoint(int(x) / 2 + 2)
            self.draw()

            inp = raw_input('Select: ')
            while inp != '0':
                self.actions(inp)
                # self.fillRandomEmptyPoint(int(x) / 2 + 2)
                self.fillRandomEmptyPoint(1)
                self.draw()
                if self.end:
                    print 'Game is over.'
                    inp = '0'
                else:
                    inp = raw_input('Select: ')

            print 'Try again? (0 - exit)'
            choice = raw_input()
            if choice != '0':
                isMore = 1
            else:
                isMore = 0

    def actions(self, action):
        for method in self.acts:
            if action in self.acts[method]:
                getattr(self, 'action' + method)()