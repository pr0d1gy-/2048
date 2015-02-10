import os
import random


class Field(object):

    __score = 0
    __startDigits = [1, 2]
    __factor = 2

    def __init__(self, x = 0, y = 0):
        self.__sizeX = int(x)
        self.__sizeY = int(y)

        self.__checkParams()
        self.__createField()

    def __checkParams(self):
        if not self.__sizeX or not self.__sizeY:
            raise AttributeError, 'X and Y arguments must be ( > 0 )'
        if self.__sizeX > 25 or self.__sizeY > 25:
            raise AttributeError, 'X and Y arguments must be ( <= 25 )'

    def __createField(self):
        self.__field = [[0 for x in range(self.__sizeX)] for y in range(self.__sizeY)]

    def setEmptyPoints(self):
        self.__emptyPoints = []
        for y in range(len(self.__field)):
            for x in range(len(self.__field[y])):
                if self.__field[y][x] == 0:
                    self.__emptyPoints.append([y, x])

    def fillPoint(self, x, y, value):
        self.__field[y][x] = value

    def getPoint(self, x, y):
        return self.__field[y][x]

    def getRandomEmptyPoint(self, count=1):
        self.setEmptyPoints()
        return random.sample(range(len(self.__emptyPoints)), count)

    def fillRandomEmptyPoint(self, count=1):
        keys = self.getRandomEmptyPoint(count)
        for k in keys:
            self.__field[self.__emptyPoints[k][0]][self.__emptyPoints[k][1]] = self.__factor * random.choice(self.__startDigits)
            del self.__emptyPoints[k]

    def getField(self):
        return self.__field

    def getSizeX(self):
        return self.__sizeX

    def getSizeY(self):
        return self.__sizeY

    def clearConsole(self):
        os.system('clear')

    def scoreUp(self, val):
        self.__score += val

    def actionUp(self):
        self.moveY(1)

    def actionDown(self):
        self.moveY(-1)

    def moveY(self, factor):
        for y in range(len(self.__field))[::factor]:
            if (factor > 0 and y == 0) or (factor < 0 and y == len(self.__field) - 1):
                continue

            for x in range(len(self.__field[y])):
                if self.__field[y][x] == 0:
                    continue

                if self.__field[y - 1][x] == 0:
                    self.__field[y - 1][x] = self.__field[y][x]
                    self.__field[y][x] = 0

                    self.moveY(factor)

                if self.__field[y - 1][x] == self.__field[y][x]:
                    self.__field[y - 1][x] += self.__field[y][x]
                    self.__field[y][x] = 0
                    self.__score += self.__field[y - 1][x]


        # for y in range(len(self.__field))[::factor]:
        #     if y == 0:
        #         continue
        #
        #     for x in range(len(self.__field)):
        #         if self.__field[y * factor][x] == 0:
        #             continue
        #
        #         if self.__field[(y - 1) * factor][x] == 0:
        #             self.__field[(y - 1) * factor][x] = self.__field[y * factor][x]
        #             self.__field[y * factor][x] = 0
        #
        #             self.moveY(factor)
        #
        #         if self.__field[y * factor][x] == self.__field[(y - 1) * factor][x]:
        #             self.__field[(y - 1) * factor][x] += self.__field[y * factor][x]
        #             self.__field[y * factor][x] = 0
        #             self.__score += self.__field[(y - 1) * factor][x]
        #
        #             self.moveY(factor)

    def actionLeft(self):
        print 'left'
        pass
    def actionRight(self):
        print 'right'
        pass

    def printField(self):
        for y in self.__field:
            print y

    def draw(self):
        self.clearConsole()
        print '-' * 100 \
            + '\nScore: ' + str(self.__score) \
            + '\n' + '-' * 100 + '\n'
        self.printField()
        print '\n' + '-' * 100 \
                + '\nUp - (u|up|1)' \
                + '\nDown - (d|down|2)' \
                + '\nLeft - (l|left|3)' \
                + '\nRight - (r|right|4)' \
                + '\nExit - 0' \
                + '\n' + '-' * 100