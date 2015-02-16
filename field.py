# -*- coding: UTF-8 -*-
import random


class Field(object):

    MAX_CELL = 8196
    UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
    SIZE = 5
    VALID_VALUES = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2058, 4096, 8196]

    cells = []

    __size = 0
    __range_size = 0

    def __init__(self, size=SIZE):
        self.set_size(size)
        self.create_empty_field()
        self.fill_random_cell(cell_count=self.__size / 2)
        self.__way = 0
        self.__score = 0
        self.not_moved = 1

    def get_size(self):
        return self.__size

    def get_size_range(self):
        return self.__range_size

    def set_size(self, size):
        self.__size = size
        self.__range_size = xrange(0, self.__size)

    def create_empty_field(self):
        self.cells = [[0] * self.__size for _ in self.__range_size]

    def get_empty_cells(self):
        return [(x, y) for x in self.__range_size for y in self.__range_size if self.get_cell(x, y) == 0]

    def clear_cells(self):
        self.cells = []

    def get_cell(self, x, y):
        return self.cells[y][x]

    def set_cell(self, x, y, val):
        if not isinstance(val, int) or val not in self.VALID_VALUES:
            raise AttributeError, 'Invalid value.'

        if y > self.__size - 1 or y * -1 > self.__size or x > self.__size - 1 or x * -1 > self.__size:
            raise AttributeError, 'Invalid field sizes.'

        self.cells[y][x] = val

    def get_line(self, y):
        if y > self.__size - 1 or y * -1 > self.__size:
            raise AttributeError, 'Size of field are less than this value.'

        return self.cells[y]

    def set_line(self, y, v):
        if y > self.__size - 1 or y * -1 > self.__size or len(v) != self.__size:
            raise AttributeError, 'Line is invalid or error in size of field.'

        for i in v:
            if not isinstance(i, int) or i not in self.VALID_VALUES:
                raise AttributeError, 'Invalid value in line.'

        self.cells[y] = v

    def fill_random_cell(self, cell_count=1):
        empty_cells = self.get_empty_cells()
        if empty_cells:
            len_empty_cells = len(empty_cells)
            if len_empty_cells < cell_count:
                cell_count = len_empty_cells
            elif len_empty_cells == 1:
                self.set_cell(empty_cells[0][0], empty_cells[0][1], random.choice([2] * 4 + [4]))
                return

            for i in random.sample(xrange(len_empty_cells), cell_count):
                self.set_cell(empty_cells[i][0], empty_cells[i][1], random.choice([2] * 4 + [4]))

    def is_filled(self):
        return not self.get_empty_cells()

    def turn_cells(self):
        self.cells = [list(x) for x in zip(*self.cells)]

    def move_line(self, line):
        n = [n for n in line if n != 0][::1 if self.__way in [self.LEFT, self.UP] else -1]
        if not n:
            return [0] * self.__size

        new_line = []
        summed = 0
        for i in n:
            if new_line:
                if new_line[-1] == i and not summed:
                    new_line[-1] = i * 2
                    self.__score += i * 2
                    summed = 1
                else:
                    new_line.append(i)
                    summed = 0
            else:
                new_line.append(i)

        if self.__way in [self.LEFT, self.UP]:
            new_line = new_line + [0] * (self.__size - len(new_line))
        else:
            new_line = [0] * (self.__size - len(new_line)) + new_line[::-1]

        if new_line != line:
            self.not_moved = 0

        return new_line

    def move(self, way):
        self.__way = way
        self.__score = 0
        self.not_moved = 1

        if self.__way in [self.UP, self.DOWN]:
            self.turn_cells()

        self.cells = map(self.move_line, self.cells)

        if self.__way in [self.UP, self.DOWN]:
            self.__way = self.DOWN if self.__way == self.UP else self.DOWN
            self.turn_cells()

        return self.__score

    def is_move_exist(self):
        if not self.is_filled():
            return True

        for y in self.__range_size:
            for x in self.__range_size:
                c = self.get_cell(x, y)
                if (x < self.__size - 1 and c == self.get_cell(x + 1, y)) \
                        or (y < self.__size - 1 and c == self.get_cell(x, y + 1)):
                    return True

        return False

    def is_won_game(self):
        for y in self.__range_size:
            for x in self.__range_size:
                if self.get_cell(x, y) >= self.MAX_CELL:
                    return True

        return False