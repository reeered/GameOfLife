import random
import unittest
from unittest.mock import patch, Mock

from Map import Map


class TestClass(unittest.TestCase):
    def setUp(self):
        self.game_map = Map([[1, 0, 1], [0, 1, 0], [0, 0, 0], [1, 1, 0]])

    def test_height(self):
        self.assertEqual(4, self.game_map.height, "Should get correct rows")

    def test_width(self):
        self.assertEqual(3, self.game_map.width, "Should get correct cols")

    def test_get_set(self):
        self.assertEqual(1, self.game_map.get_cell(1, 1))
        self.game_map.set_cell(1, 1, 0)
        self.assertEqual(0, self.game_map.get_cell(1, 1))

    def test_flip(self):
        self.assertEqual(0, self.game_map.get_cell(0, 1))
        self.game_map.flip_cell(0, 1)
        self.assertEqual(1, self.game_map.get_cell(0, 1))

    @patch('Map.Map.get_neighbor_count_map')
    def test_update(self, mock_function):
        expected_value = [[0, 1, 0],
                          [0, 1, 0],
                          [1, 1, 0],
                          [0, 0, 0]]
        mock_function.return_value = [[1, 3, 1],
                                      [2, 2, 2],
                                      [3, 3, 2],
                                      [1, 1, 1]]
        self.game_map.Update()
        for i in range(4):
            for j in range(3):
                self.assertEqual(expected_value[i][j], self.game_map.get_cell(i, j))

    def test_get_neighbor_map(self):
        expected_value = [[1, 3, 1],
                          [2, 2, 2],
                          [3, 3, 2],
                          [1, 1, 1]]
        neighbor_count_map = self.game_map.get_neighbor_count_map()
        for i in range(4):
            for j in range(3):
                self.assertEqual(expected_value[i][j], neighbor_count_map[i][j], '(%d, %d)' % (i, j))
