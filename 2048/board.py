# -*- coding: UTF-8 -*-
import random


class Field(object):
    ''' 2048 field '''

    SIZE = 5

    def __init__(self, size=SIZE):
        ''' init class '''
        self.__size = size;
        self.__range_size = xrange(0, self.__size)
        self.cells = [[0] * self.__size for _ in self.__range_size]
        self.fill_random_cell(cell_count=4)

    def get_empty_cells(self):
        ''' get empty cells '''
        return [(x, y) for x in self.__range_size for y in self.__range_size if self.get_cell(x, y) == 0]

    def get_cell(self, x, y):
        ''' get cell '''
        return self.cells[y][x]

    def set_cell(self, x, y, val):
        ''' set cell value '''
        self.cells[y][x] = val

    def fill_random_cell(self, cell_count=1):
        ''' fill random empty cells '''
        empty_cells = self.get_empty_cells()
        if empty_cells:
            for i in random.sample(xrange(len(empty_cells)), cell_count):
                self.set_cell(empty_cells[i][0], empty_cells[i][1], random.choice([2] * 4 + [4]))

    def is_filled(self):
        ''' check filled cells '''
        return len(self.get_empty_cells()) == 0

    def move(self):
        pass


field = Field()
print field.cells