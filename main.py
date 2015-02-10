import sys
from game import Game


# li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print li[10 * -1]
#
# exit()

try:
    game = Game()
except:
    e = sys.exc_info()
    print 'ERROR: ' + str(e[1])