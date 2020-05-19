#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/13/20
# Board tests

from board import Board


def test_default_board():
    test_board_size = {'x': 200, 'y': 300}
    row = 2
    column = 3
    board = Board(test_board_size, row, column)
    assert board.row == 2
    assert board.column == 3
    assert len(sum(board.centroids, [])) == row * column
    assert len(board.top_centroids) == column
