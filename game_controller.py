#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by minh at 3/30/20
# Main console class

from disk import Disk
from board import Board
from game_checker import GameChecker
from computer_agent import ComputerAgent
import random
import re

SPEED = 10
PLAYERS = {0: {'color': 'red', 'score': 1},
           1: {'color': 'yellow', 'score': 2}}
TEXT_COORDINATE_X = 3
TEXT_COORDIATE_Y = 2
TEXT_SIZE = 40


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, row, col):
        """
        Constructor containing all necessary setup
        :param SPACE: dict of width and height
        :param row: int
        :param col: int
        """
        self.space = {'x': SPACE['width'],
                      'y': SPACE['height']}

        self.board = Board(self.space, row, col)
        self.row = row
        self.col = col
        self.offset = self.board.offset
        self.top_spaces = self.board.top_centroids
        self.disks = []
        self.current_disk = None
        self.scored = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.turn = 0
        self.total = row * col
        self.playable = True
        self.falling = False
        self.stop_point_y = None
        self.final_row = None
        self.final_col = None
        self.current_score = 0
        self.win = ''
        self.timer = 100

    def update(self):
        """
        Function to render the main game
        """
        if self.current_disk is not None:
            self.current_disk.display()
            if self.falling and self.current_disk.y < self.stop_point_y:
                self.current_disk.y += SPEED
                self.playable = False  # prevent mind changing mid-fall
            self.board.display()
            # When the disk touch the lowest point possible
            # switch turn and reset state while recording
            # the score and count down to game over
            if self.current_disk.y >= self.stop_point_y:
                self.current_disk.y = self.stop_point_y
                self.disks.append(self.current_disk)
                self.scored[self.final_row][self.final_col] = \
                    self.current_score
                if len(self.disks) > 6:
                    # only start checking after 6 disks to save memory
                    score_to_check = int(self.current_score)
                    checker = GameChecker(self.scored,
                                          score_to_check)
                    if checker.check_matrix():
                        fill(0)
                        textSize(TEXT_SIZE)
                        self.win = PLAYERS[int(self.turn + 0.5)][
                            'color'].upper()
                        text(self.win + " WINS!",
                             self.space['x'] / TEXT_COORDINATE_X,
                             self.offset / TEXT_COORDIATE_Y)
                        self.playable = False
                        self.total = -1
                        if self.turn == 0:
                            self.enter_name()
                            self.turn = -1
                    else:
                        self.turn = 1 - (int(self.turn + 0.5))
                        self.reset_all()
                        self.total -= 1
        # display existing disks
        for disk in self.disks:
            disk.display()
            self.board.display()
        self.board.display()

        # AI Component
        ######################
        if self.turn != 0:
            self.timer -= 1
            self.playable = False
        # check if game is over by seeing if board is filled
        if self.turn == 1 and self.timer <= 0:
            computer_disk = self.computer_play()
            to_drop = self.top_spaces[computer_disk[1]]
            self.create_new_disk(to_drop, computer_disk[0], computer_disk[1])
            self.falling = True
            self.turn = 0.5  # trick to make sure the game render
        #######################

        if self.total == 0:
            fill(0)
            textSize(TEXT_SIZE)
            text("GAME OVER", self.space['x'] / TEXT_COORDINATE_X,
                 self.offset / TEXT_COORDIATE_Y)
            self.playable = False
            self.turn = -1

    def show_disk(self, x, y):
        """
        Function to display a disk when mouse is click or hover
        :param x: int x coord
        :param y: int y coord
        """
        # Only allow to choose when mouse hover
        # around the blank space above the grid
        if y <= self.offset and 0 <= x <= self.space['x']:
            try:
                current_col = x // self.board.grid_space
                position = self.top_spaces[current_col]
                found = False
                for row_avail in range(self.row - 1, -1, -1):
                    if self.scored[row_avail][current_col] == 0:
                        found = True
                        break
                if found:
                    # Only allow when the position is not filled
                    self.create_new_disk(position, row_avail, current_col)
            except IndexError:
                pass
        else:
            self.current_disk = None

    def drop_disk(self):
        """
        Function to change the state of
        falling in the main game
        """
        # Change the state of the disk
        if self.current_disk:
            self.falling = True

    def reset_all(self):
        """
        Function to reset the state of the game after
        every non-winning turn and display whose turn
        """
        # reset all states
        self.current_disk = None
        self.falling = False
        self.final_row = None
        self.final_col = None
        self.current_score = 0
        self.playable = True
        self.timer = random.randint(20, 50)
        # print whose turn it is
        print(PLAYERS[int(self.turn + 0.5)][
                  'color'].upper() + "'S TURN")

    def create_new_disk(self, coordinate, row, col):
        """
        Function to create a new disk in the game to drop
        :param coordinate: list containing x,y coord
        :param row: int
        :param col: int
        :return:
        """
        final_position = self.board.centroids[row][col]
        self.stop_point_y = final_position[1]
        self.final_row = row
        self.final_col = col
        disk_color = PLAYERS[int(self.turn + 0.5)]['color']
        self.current_score = PLAYERS[self.turn]['score']
        self.current_disk = Disk(coordinate[0],
                                 coordinate[1],
                                 self.board.grid_space,
                                 disk_color)

    def computer_play(self):
        """
        Function to initiate computer's turn
        :return: list, coordinates of disk
        """
        computer = ComputerAgent(self.scored,
                                 PLAYERS[0]['score'],
                                 PLAYERS[1]['score'])
        potential_position = computer.make_move()
        return potential_position

    @staticmethod
    def enter_name():
        """
        Function to ask user to enter name if they win
        :return: None, end game
        """

        def input(message=''):
            from javax.swing import JOptionPane
            return JOptionPane.showInputDialog(frame, message)

        def create_score_sheet(winner):
            try:
                f = open('scores.txt', "r")
            except FileNotFoundError:
                print("Can't find file")
                return
            current_content = {}
            for line in f.readlines():
                score = re.findall(r'\d', line)[0]  # get digit
                name = line.replace(score, '').strip()
                current_content[name] = int(score)
            if winner in current_content:
                current_content[winner] += 1
            else:
                current_content[winner] = 1
            result_high_to_low = sorted(current_content.items(),
                                        key=lambda x: x[1], reverse=True)
            new_content = ''
            f = open('scores.txt', "w+")
            for r in result_high_to_low:
                new_content += r[0] + ' ' + str(r[1]) + '\n'
            f.write(new_content)

        answer = input('You win! Enter your name! Leave blank to cancel')
        if answer:
            create_score_sheet(answer)
            return
        elif answer == '':
            return
