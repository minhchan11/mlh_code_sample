#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 3/30/20
# class disk
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Disk:
    """
    Class Disk for display
    """
    def __init__(self, x, y, width, color='red'):
        """
        Constructor to create a disk
        :param x: int
        :param y: int
        :param width: int
        :param color: str
        """
        self.x = x
        self.y = y
        if color == 'red':
            self.color = RED
        else:
            self.color = YELLOW
        self.width = self.height = width

    def display(self):
        """
        Function to display disk
        """
        noStroke()
        fill(*self.color)
        ellipse(self.x, self.y, self.width, self.height)
