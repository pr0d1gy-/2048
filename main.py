import sys
from game import Game


# li = [[0] * 10] * 10
# print li
#
# exit()

try:
    game = Game()
except:
    e = sys.exc_info()
    print 'ERROR: ' + str(e[1])