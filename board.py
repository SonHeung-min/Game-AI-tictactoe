import numpy as np
import pygame as pg

from constant import *

class Board:

    def __init__(self, screen):
        self.screen = screen
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_squares = self.squares   # [squares]
        self.marked_squares = 0

    def final_state(self, show = False):
        '''
        @return 0 if there is no win yet
        @return 1 if player 1 wins
        @return 2 if player 2 wins
        '''

        #vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    initial_Pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 20)
                    final_Pos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 20)
                    pg.draw.line(self.screen, color, initial_Pos, final_Pos, LINE_WIDTH)
                
                return self.squares[0][col]
        
        #horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    initial_Pos = (20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    final_Pos = (WIDTH - 20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pg.draw.line(self.screen, color, initial_Pos, final_Pos, LINE_WIDTH)
                
                return self.squares[row][0]
            
        #descending diagonal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                initial_Pos = (20, 20)
                final_Pos = (WIDTH - 20, HEIGHT - 20)
                pg.draw.line(self.screen, color, initial_Pos, final_Pos, LINE_WIDTH)
            return self.squares[1][1]
        
        #ascending diagonal wins
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                initial_Pos = (20, HEIGHT - 20)
                final_Pos = (WIDTH - 20, 20)
                pg.draw.line(self.screen, color, initial_Pos, final_Pos, LINE_WIDTH)
            return self.squares[1][1]
        
        #there is no win yet
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1
    
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )

        return empty_sqrs
    
    def is_full(self):
        return self.marked_squares == 9
    
    def is_empty(self):
        return self.marked_squares == 0