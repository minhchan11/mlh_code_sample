#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 3/30/20
# Class board for grid

LINE_WIDTH = 10
BLUE = (0, 0, 255)


class Board():
    """
    Class Board for display in Processing
    """

    def __init__(self, board_size, row, column):
        """
        Constructor to create board
        :param board_size: dict of 'x' and 'y'
        :param row: int
        :param column: int
        """
        self.board_size = board_size
        self.row = row
        self.column = column
        self.line_width = LINE_WIDTH
        self.grid_space = (self.board_size['x'] - self.line_width
                           * self.column) / self.column + self.line_width
        self.offset = self.board_size['y'] - self.board_size['x'] - (
                row - column) * self.grid_space
        self.centroids = self.generate_centroids()
        self.top_centroids = [[c[0], c[1] - self.grid_space] for c in
                              self.centroids[0]]  # space above board to drop

    def display(self):
        """
        Function to display the horizontal and vertical lines
        """
        # draw grids
        vertical_lines = self.column + 1
        horizontal_lines = self.row + 1
        original_start_horizontal = [0, self.offset]
        original_end_horizontal = [self.board_size['x'], self.offset]
        for h in range(horizontal_lines):
            line(*(original_start_horizontal + original_end_horizontal))
            strokeWeight(self.line_width)
            stroke(*BLUE)
            original_start_horizontal[1] += self.grid_space
            original_end_horizontal[1] += self.grid_space
        original_start_vertical = [0, self.offset]
        original_end_vertical = [0, self.board_size['y']]
        for v in range(vertical_lines):
            line(*(original_start_vertical + original_end_vertical))
            strokeWeight(self.line_width)
            stroke(*BLUE)
            original_start_vertical[0] += self.grid_space
            original_end_vertical[0] += self.grid_space

    def generate_centroids(self):
        """
        Function to generate possible coordinates for disks
        to be placed
        :return: list of coordinates
        """
        # create centroids from grid and space
        original_x = 0 + self.grid_space / 2
        original_y = self.offset + self.grid_space / 2
        result = []
        for i in range(self.row):
            start_x = original_x
            sub_result = []
            for j in range(self.column):
                sub_result.append([start_x, original_y])
                start_x += self.grid_space
            result.append(sub_result)
            original_y += self.grid_space
        return result
