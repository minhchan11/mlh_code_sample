#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/13/20
# Testing suite computer agent

from computer_agent import ComputerAgent


def test_computer_find_possible_places():
    new_array = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 2, 0]]
    ca = ComputerAgent(new_array, 2, 1)
    assert ca.available_space == [[3, 0], [3, 1], [2, 2], [3, 3]]


def test_computer_find_adjacent_enemy():
    new_array = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [2, 0, 2, 0],
                 [2, 2, 2, 0]]
    ca = ComputerAgent(new_array, 2, 1)
    assert ca.best_choices == [[2, 1]]


def test_computer_make_move_block():
    new_array = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [2, 2, 2, 0]]
    ca = ComputerAgent(new_array, 2, 1)
    assert ca.make_move() == [3, 3]


def test_computer_make_move_win():
    new_array = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 0]]
    ca = ComputerAgent(new_array, 2, 1)
    assert ca.make_move() == [3, 3]
