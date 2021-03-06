import unittest
from unittest.case import TestCase
from field import Field


class FieldTest(TestCase):

    def setUp(self):
        self.field = Field(3)

    def test1_field_size(self):
        self.assertTrue(len(self.field.cells) == 3 and False not in [3 == len(i) for i in self.field.cells],
                        'Field size is not true.')

        print 'Field Size - True'

    def test2_empty_cell(self):
        self.field.create_empty_field()
        self.assertTrue(len(self.field.get_empty_cells()) == 9,
                        'Get empty cell returned false result.')
        self.field.cells = [[2] * 3] * 3
        self.assertTrue(len(self.field.get_empty_cells()) == 0)

        print 'Empty cells - True'

    def test3_fill_line(self):
        self.field.set_line(0, [0, 2, 2])

        with self.assertRaises(AttributeError):
            self.field.set_line(3, [0, 2, 2])

        with self.assertRaises(AttributeError):
            self.field.set_line(4, [0, 2, 2])

        with self.assertRaises(AttributeError):
            self.field.set_line(2, [0, 2, '2'])

        with self.assertRaises(AttributeError):
            self.field.set_line(2, [0, 2, 2, 2])

        with self.assertRaises(AttributeError):
            self.field.set_line(2, [0, 2])

        print 'Fill Line - True'

    def test4_fill_cell(self):
        self.field.set_cell(0, 1, 2)

        with self.assertRaises(AttributeError):
            self.field.set_cell(3, 0, 0)

        with self.assertRaises(AttributeError):
            self.field.set_cell(-4, 0, 0)

        with self.assertRaises(AttributeError):
            self.field.set_cell(0, 3, 0)

        with self.assertRaises(AttributeError):
            self.field.set_cell(0, -4, 0)

        with self.assertRaises(AttributeError):
            self.field.set_cell(0, 0, 3)

        with self.assertRaises(AttributeError):
            self.field.set_cell(0, 0, '2')

        print 'Fill Cell - True'

    def test5_move(self):
        self.field.cells = [[2, 2, 4], [0, 0, 0], [4, 0, 4]]
        result_lines = [[4, 4, 0], [0, 0, 0], [8, 0, 0]]
        result_score = 12

        ''' move left '''
        self.assertTrue(self.field.move(3) == result_score and self.field.cells == result_lines,
                        'Move left is wrong')

        self.field.cells = [[2, 2, 4], [0, 2, 0], [4, 4, 4]]
        result_lines = [[0, 4, 4], [0, 0, 2], [0, 4, 8]]
        result_score = 12

        ''' move right '''
        self.assertTrue(self.field.move(4) == result_score and self.field.cells == result_lines,
                        'Move right is wrong')

        self.field.cells = [[2, 2, 4], [2, 0, 4], [4, 0, 4]]
        result_lines = [[4, 2, 8], [4, 0, 4], [0, 0, 0]]
        result_score = 12

        ''' move up '''
        self.assertTrue(self.field.move(1) == result_score and self.field.cells == result_lines,
                        'Move up is wrong')

        self.field.cells = [[2, 2, 4], [0, 0, 0], [4, 0, 4]]
        result_lines = [[0, 0, 0], [2, 0, 0], [4, 2, 8]]
        result_score = 8

        ''' move down '''
        self.assertTrue(self.field.move(2) == result_score and self.field.cells == result_lines,
                        'Move down is wrong')

        print 'Move - True'

    def test6_is_filled(self):
        self.field.cells = [[2, 2, 4], [0, 0, 0], [4, 0, 4]]
        self.assertFalse(self.field.is_filled())
        self.field.cells = [[2, 2, 4], [2, 2, 2], [4, 2, 4]]
        self.assertTrue(self.field.is_filled())

        print 'Is Filled - True'

    def test7_can_move(self):
        # can't move
        self.field.cells = [[2, 4, 8], [4, 8, 2], [16, 32, 64]]
        self.assertFalse(self.field.is_move_exist(),
                         'Can move function return false result.')

        # left
        self.field.cells = [[4, 4, 8], [4, 8, 2], [16, 32, 64]]
        self.assertTrue(self.field.is_move_exist(),
                        'Can move function return false result.')

        # right
        self.field.cells = [[2, 4, 4], [4, 8, 2], [16, 32, 64]]
        self.assertTrue(self.field.is_move_exist(),
                        'Can move function return false result.')

        # down
        self.field.cells = [[2, 4, 8], [4, 32, 2], [16, 32, 64]]
        self.assertTrue(self.field.is_move_exist(),
                        'Can move function return false result.')

        # up
        self.field.cells = [[2, 4, 8], [2, 8, 2], [16, 32, 64]]
        self.assertTrue(self.field.is_move_exist(),
                        'Can move function return false result.')

        print 'Can move - True'

    def test8_won_game(self):
        self.field.cells = [[2, 4, 8], [2, 8, 2], [16, 32, 64]]
        self.assertFalse(self.field.is_won_game(),
                         '"is_won_game" function work is not true.')

        self.field.cells[2][2] = 8196
        self.assertTrue(self.field.is_won_game(),
                        '"is_won_game" function work is not true.')

        print 'Won game - True'

    def test9_get_size(self):
        self.assertTrue(self.field.get_size() == 3,
                        'Get size returned wrong result.')

        print 'Get Size - True'

    def test10_get_size_range(self):
        self.assertTrue(len([i for i in self.field.get_size_range()]) == 3,
                        'Get Size Range returned wrong result.')

        print 'Get Size Range - True'

    def test11_clear_cells(self):
        self.field.cells = [[2] * 3] * 3
        self.field.clear_cells()
        self.assertTrue(not self.field.cells,
                        'Clear cells do not work.')

        print 'Clear Cells - True'

    def test12_get_line(self):
        line = self.field.get_line(0)
        self.assertTrue(line and isinstance(line, list),
                        'Get line do not work.')

        with self.assertRaises(AttributeError):
            self.field.get_line(-4)

        with self.assertRaises(AttributeError):
            self.field.get_line(3)

        with self.assertRaises(AttributeError):
            self.field.get_line('2')

        print 'Get Line - True'

    def test14_set_size(self):
        with self.assertRaises(AttributeError):
            self.field.set_size('2')

        with self.assertRaises(AttributeError):
            self.field.set_size(-2)

        with self.assertRaises(AttributeError):
            self.field.set_size(30)

        print 'Set Size - True'

    def test15_fill_random_cell(self):
        self.field.set_size(2)

        self.field.cells = [[2, 2], [2, 2]]
        self.assertTrue(self.field.fill_random_cell(1) == 0, 'Fill random cell work is not valid.')

        self.field.cells = [[0, 0], [2, 2]]
        self.assertTrue(self.field.fill_random_cell(1) == 1, 'Fill random cell work is not valid.')

        self.field.cells = [[0, 0], [2, 2]]
        self.assertTrue(self.field.fill_random_cell(2) == 2, 'Fill random cell work is not valid.')

        self.field.cells = [[0, 2], [2, 2]]
        self.assertTrue(self.field.fill_random_cell(2) == 1, 'Fill random cell work is not valid.')

        print 'Fill Random Cell - True'


if __name__ == '__main__':
    unittest.main()