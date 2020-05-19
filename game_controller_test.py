#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/14/20
# Game controller testing suite

from game_controller import GameController


def test_game_controller_setup_none():
    SPACE = {'width': 500, 'height': 700}
    try:
        gc = GameController(SPACE, 0, 0)
        assert gc.scored == []
    except ZeroDivisionError:
        failedwithzerodivision = True
    assert failedwithzerodivision


def test_game_controller_setup_one():
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 1, 1)
    assert gc.scored == [[0]]


def test_game_controller_setup_two():
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 2, 2)
    assert gc.scored == [[0, 0], [0, 0]]


def test_if_in_correct_space_fail():
    # can only drop if mouse is in the empty area
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 2, 2)
    assert gc.show_disk(100, 300) is None


def test_create_new_disk():
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 2, 2)
    gc.create_new_disk([300, 200], 1, 1)
    assert gc.current_disk


def test_create_drop_disk():
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 2, 2)
    gc.create_new_disk([300, 200], 1, 1)
    gc.drop_disk()
    assert gc.falling is True


def test_reset_all():
    SPACE = {'width': 500, 'height': 700}
    gc = GameController(SPACE, 2, 2)
    gc.create_new_disk([300, 200], 1, 1)
    gc.drop_disk()
    gc.reset_all()
    assert gc.current_disk is None
    assert gc.falling is False
    assert gc.final_row is None
    assert gc.final_col is None
    assert gc.current_score == 0
    assert gc.playable is True
