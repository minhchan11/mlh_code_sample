#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/9/20
# Computer Agent class

from game_checker import GameChecker
from itertools import product
import copy
import random


class ComputerAgent():
    """
    Class to make computer moves
    """

    def __init__(self, input_matrix, enemy_score, computer_score):
        """
        Constructor to gather all information needed to make a move
        :param input_matrix: current board
        :param enemy_score: score of human
        :param computer_score: score of computer
        """
        self.input_matrix = input_matrix
        self.enemy_score = enemy_score
        self.computer_score = computer_score
        self.available_space = self.find_possible_places()
        self.best_choices = self.find_adjacent_enemy()

    def find_possible_places(self):
        """
        Function to return a list of coordinates that
        are available to play
        :return: list of coordinates
        """
        result = []
        for i in range(len(self.input_matrix[0])):
            start_row = 0
            while self.input_matrix[start_row][i] == 0 \
                    and start_row < len(self.input_matrix):
                try:
                    if self.input_matrix[start_row + 1][i] != 0:
                        result.append([start_row, i])
                        break
                    else:
                        start_row += 1
                except IndexError:
                    result.append([start_row, i])
                    break

        return result

    def find_adjacent_enemy(self):
        """
        Function to find the density of human's
        moves so far
        :return: list, coordinate of the maximum
        density coordinate
        """
        result = {}
        to_check = [list(combi) for combi in
                    product([-1, 0, 1], repeat=2)]
        for i in self.available_space:
            enemy_count = 0
            for j in to_check:
                adjacent = [sum(_) for _ in zip(i, j)]
                try:
                    if self.input_matrix[adjacent[0]][adjacent[1]] == \
                            self.enemy_score:
                        enemy_count += 1
                except IndexError:
                    continue
            if enemy_count not in result:
                result[enemy_count] = [i]
            else:
                result[enemy_count].append(i)
        return max(result.items())[1]

    def make_move(self):
        """
        Function to make calculated move
        :return: list, coordinate of move
        """
        for s in self.available_space:
            temp = copy.deepcopy(self.input_matrix)
            temp[s[0]][s[1]] = self.computer_score
            checker = GameChecker(temp, self.computer_score)
            # if computer can win next move go for it
            if checker.check_matrix():
                return s
            else:
                # if human win next move block it
                temp[s[0]][s[1]] = self.enemy_score
                checker = GameChecker(temp, self.enemy_score)
                if checker.check_matrix():
                    return s
        # else choose one of the most dense to infiltrate
        return random.choice(self.best_choices)
