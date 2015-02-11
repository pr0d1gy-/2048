# -*- coding: UTF-8 -*-
import random


class Field(object):

    UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
    SIZE = 5

    def __init__(self, size=SIZE):
        self.__size = size;
        self.__range_size = xrange(0, self.__size)
        self.cells = [[0] * self.__size for _ in self.__range_size]
        self.fill_random_cell(cell_count=8)
        self.__way = 0
        self.__score = 0

    def get_empty_cells(self):
        return [(x, y) for x in self.__range_size for y in self.__range_size if self.get_cell(x, y) == 0]

    def get_cell(self, x, y):
        return self.cells[y][x]

    def set_cell(self, x, y, val):
        self.cells[y][x] = val

    def fill_random_cell(self, cell_count=1):
        empty_cells = self.get_empty_cells()
        if empty_cells:
            for i in random.sample(xrange(len(empty_cells)), cell_count):
                self.set_cell(empty_cells[i][0], empty_cells[i][1], random.choice([2] * 4 + [4]))

    def is_filled(self):
        return not self.get_empty_cells()

    def turn_cells(self):
        self.cells = [list(x) for x in zip(*self.cells)]
        pass

    def move_line(self, line):
        n = [n for n in line if n != 0][::1 if self.__way in [self.LEFT, self.UP] else -1]
        if not n:
            return [0] * self.__size

        new_line = []
        for i in xrange(len(n)):
            if new_line:
                if new_line[-1] == n[i]:
                    new_line[-1] += n[i]
                else:
                    new_line.append(n[i])
            else:
                new_line.append(n[i])

        if self.__way in [self.LEFT, self.UP]:
            return new_line + [0] * (self.__size - len(new_line))

        return [0] * (self.__size - len(new_line)) + new_line[::-1]

    def move(self, way):
        self.__way = way
        self.__score = 0

        if self.__way in [self.UP, self.DOWN]:
            self.turn_cells()

        self.cells = map(self.move_line, self.cells)

        if self.__way in [self.UP, self.DOWN]:
            self.__way = self.UP if self.__way == self.UP else self.DOWN
            self.turn_cells()

        return self.__score


field = Field()
for y in field.cells:
    print y
print '\n\n'
print field.move(field.DOWN)
for y in field.cells:
    print y