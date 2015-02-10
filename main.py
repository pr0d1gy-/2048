import sys
from game import Game


try:
    game = Game()
except:
    e = sys.exc_info()
    print 'ERROR: ' + str(e[1])