#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 4/8/20
# game checker class
from functools import reduce


class GameChecker():
    """
    Class Game Checker to check for scores and wins
    """

    def __init__(self, original_matrix, score):
        """
        Constructor to create game checker
        :param original_matrix: current board state
        :param score: score to check for
        """
        self.original_matrix = original_matrix
        self.score = score**4

    @staticmethod
    def slice_four(input_array):
        """
        Function to chunk matrix into 4*4 chunks
        :param input_array: list
        :return: list of list
        """
        result = []
        for i in range(len(input_array)):
            if len(input_array[i:i + 4]) == 4:
                result.append(input_array[i:i + 4])
        return result

    @staticmethod
    def calculate_product(input_list):
        """
        Function to return score product of an array
        :param input_list: list
        :return: int
        """
        return reduce(lambda x, y: x * y, input_list, 1)

    def calculate_vertical(self, filtered_matrix):
        """
        Function to check win on all vertical product
        :param filtered_matrix: list
        :return: bool
        """
        column_product = [self.calculate_product(list(s)) for s in
                          zip(*filtered_matrix)]
        if sum(column_product) > 0:
            for s in column_product:
                if s == self.score:
                    return True
        return False

    def calculate_horizontal(self, filtered_matrix):
        """
        Function to check win on horizontal product
        :param filtered_matrix: list
        :return: bool
        """
        for each_row in filtered_matrix:
            single_row = self.slice_four(each_row)
            for s in single_row:
                if self.calculate_product(s) == self.score:
                    return True
        return False

    def calculate_diagonal(self, filtered_matrix):
        """
        Function to check win on diagonal product
        :param filtered_matrix: list
        :return: bool
        """
        result = []
        for i in range(3, len(filtered_matrix[0])):
            start_row = 0
            start_col = i
            sub_array = []
            for _ in range(4):
                sub_array.append(filtered_matrix[start_row][start_col])
                start_row += 1
                start_col -= 1
            result.append(sub_array)
        for k in range(len(filtered_matrix[0]) - 4, -1, -1):
            start_row = 0
            start_col = k
            sub_array = []
            for _ in range(4):
                sub_array.append(filtered_matrix[start_row][start_col])
                start_row += 1
                start_col += 1
            result.append(sub_array)
        for r in result:
            if self.calculate_product(r) == self.score:
                return True
        return False

    def check_matrix(self):
        """
        Function to check win in all directions
        :return: bool
        """
        filter_matrix = [m for m in self.original_matrix if sum(m) > 0]
        if len(filter_matrix) < 4:
            # When the rows are not filled up to 4 rows
            # only check horizontal
            hor_result = self.calculate_horizontal(filter_matrix)
            if hor_result:
                return hor_result
        else:
            # when rows are more than 4 rows then check all
            # directions
            to_check = self.slice_four(self.original_matrix)
            for sub_matrix in to_check:
                vert_result = self.calculate_vertical(sub_matrix)
                if vert_result:
                    return True
                hor_result = self.calculate_horizontal(sub_matrix)
                if hor_result:
                    return True
                diag_result = self.calculate_diagonal(sub_matrix)
                if diag_result:
                    return True
