import os
import random


class Field(object):

    __score = 0
    __field = []
    __startDigits = [1, 2]
    __factor = 2

    def __init__(self, x = 0, y = 0):
        self.end = 0
        self.__score = 0
        self.__field = []

        self.__sizeX = int(x)
        self.__sizeY = int(y)

        self.__checkParams()
        self.__createField()

    def __checkParams(self):
        if self.__sizeX < 1 or self.__sizeY < 1:
            raise AttributeError, 'X and Y arguments must be ( > 0 )'
        if self.__sizeX > 25 or self.__sizeY > 25:
            raise AttributeError, 'X and Y arguments must be ( <= 25 )'

    def __createField(self):
        self.__field = [[0 for x in range(self.__sizeX)] for y in range(self.__sizeY)]

        print self.__field

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

        if len(self.__emptyPoints) < count:
            count = len(self.__emptyPoints)

        if self.__emptyPoints:
            return random.sample(range(len(self.__emptyPoints)), count)
        else:
            self.end = 1
            return 0

    def fillRandomEmptyPoint(self, count=1):
        keys = self.getRandomEmptyPoint(count)
        if keys:
            for k in keys:
                self.__field[self.__emptyPoints[k][0]][self.__emptyPoints[k][1]] = self.__factor * random.choice(self.__startDigits)

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
        self.__moveY(1)

    def actionDown(self):
        self.__moveY(-1)

    def actionLeft(self):
        self.__moveX(1)

    def actionRight(self):
        self.__moveX(-1)

    def __moveX(self, factor):
        for y in range(len(self.__field)):

            for x in range(len(self.__field[y])):
                if x == 0:
                    continue

                if factor < 0:
                    x += 1

                if self.__field[y][x * factor] == 0:
                    continue

                if self.__field[y][(x - 1) * factor] == 0:
                    self.__field[y][(x - 1) * factor] = self.__field[y][x * factor]
                    self.__field[y][x * factor] = 0

                    self.__moveX(factor)

                if self.__field[y][(x - 1) * factor] == self.__field[y][x * factor]:
                    self.__field[y][(x - 1) * factor] += self.__field[y][x * factor]
                    self.__field[y][x * factor] = 0
                    self.scoreUp(self.__field[y][(x - 1) * factor])

                    self.__moveX(factor)

    def __moveY(self, factor):
        for y in range(len(self.__field)):
            if y == 0:
                continue

            if factor < 0:
                y += 1

            for x in range(len(self.__field)):
                if self.__field[y * factor][x] == 0:
                    continue

                if self.__field[(y - 1) * factor][x] == 0:
                    self.__field[(y - 1) * factor][x] = self.__field[y * factor][x]
                    self.__field[y * factor][x] = 0

                    self.__moveY(factor)

                if self.__field[y * factor][x] == self.__field[(y - 1) * factor][x]:
                    self.__field[(y - 1) * factor][x] += self.__field[y * factor][x]
                    self.__field[y * factor][x] = 0
                    self.scoreUp(self.__field[(y - 1) * factor][x])

                    self.__moveY(factor)

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