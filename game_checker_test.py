#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/13/20
# Game checker testing suite
from game_checker import GameChecker


def test_game_checker_default():
    gc = GameChecker([1, 2, 3, 4], 2)
    assert gc.score == 16


def test_slice_four_1d_array():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [1, 2, 3, 4, 5, 6]
    assert gc.slice_four(new_array) == [[1, 2, 3, 4], [2, 3, 4, 5],
                                        [3, 4, 5, 6]]


def test_slice_four_2d_array():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1],
                 [2, 2, 2, 2, 2, 2],
                 [3, 3, 3, 3, 3, 3],
                 [4, 4, 4, 4, 4, 4],
                 [5, 5, 5, 5, 5, 5],
                 [6, 6, 6, 6, 6, 6]]
    assert gc.slice_four(new_array) == [[[0, 0, 0, 0, 0, 0],
                                         [1, 1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2, 2],
                                         [3, 3, 3, 3, 3, 3]],
                                        [[1, 1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2, 2],
                                         [3, 3, 3, 3, 3, 3],
                                         [4, 4, 4, 4, 4, 4]],
                                        [[2, 2, 2, 2, 2, 2],
                                         [3, 3, 3, 3, 3, 3],
                                         [4, 4, 4, 4, 4, 4],
                                         [5, 5, 5, 5, 5, 5]],
                                        [[3, 3, 3, 3, 3, 3],
                                         [4, 4, 4, 4, 4, 4],
                                         [5, 5, 5, 5, 5, 5],
                                         [6, 6, 6, 6, 6, 6]]]


def test_calculate_product():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [1, 2, 3, 4]
    assert gc.calculate_product(new_array) == 24


def test_calculate_vertical_win():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[0, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0]]
    assert gc.calculate_vertical(new_array) is True


def test_calculate_vertical_nowin():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[2, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0]]
    assert gc.calculate_vertical(new_array) is False


def test_calculate_horizontal_win():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[0, 0, 2, 2, 2, 2],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
    assert gc.calculate_horizontal(new_array) is True


def test_calculate_horizontal_nowin():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[0, 0, 0, 2, 2, 2],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
    assert gc.calculate_horizontal(new_array) is False


def test_calculate_diagonal_left_win():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[0, 0, 0, 0, 0, 2],
                 [0, 0, 0, 0, 2, 0],
                 [0, 0, 0, 2, 0, 0],
                 [0, 0, 2, 0, 0, 0]]
    assert gc.calculate_diagonal(new_array) is True


def test_calculate_diagonal_right_win():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[2, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0]]
    assert gc.calculate_diagonal(new_array) is True


def test_calculate_diagonal_nowin():
    gc = GameChecker([1, 2, 3, 4], 2)
    new_array = [[2, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 0]]
    assert gc.calculate_diagonal(new_array) is False


def test_check_matrix_win():
    new_array = [[2, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0],
                 [2, 0, 2, 0, 0, 0],
                 [2, 0, 0, 2, 0, 0]]
    gc = GameChecker(new_array, 2)
    assert gc.check_matrix() is True


def test_check_matrix_nowin():
    new_array = [[2, 0, 0, 0, 0, 0],
                 [2, 0, 0, 0, 0, 0],
                 [0, 0, 2, 0, 0, 0],
                 [2, 0, 0, 2, 0, 0]]
    gc = GameChecker(new_array, 2)
    assert gc.check_matrix() is None
