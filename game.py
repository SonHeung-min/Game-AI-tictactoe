import pygame as pg
from constant import *
from board import Board
from ai import AI

class Game: 

    def __init__(self, screen):
        self.screen = screen
        self.board = Board(self.screen)
        self.ai = AI()
        self.player = 1         #player_1 - crosses   #player_2 - circles
        self.running = True
        self.show_lines()

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_figures(row, col)
        self.next_turn()

    def show_lines(self):
        #fill BG 
        self.screen.fill( BACKGROUND_COLOR )

        #vertical line
        pg.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pg.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)

        #horizontal
        pg.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pg.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)

    def draw_figures(self, row, col):
        if self.player == 1:
            #draw cross
            #descending line
            start_descending = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            end_descending = (col * SQUARE_SIZE + 3 * OFFSET, row * SQUARE_SIZE + 3 * OFFSET)
            pg.draw.line(self.screen, CROSS_COLOR, start_descending, end_descending, CROSS_WIDTH)

            #ascending line
            start_ascending = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + 3 * OFFSET)
            end_ascending = (col * SQUARE_SIZE + 3 * OFFSET, row * SQUARE_SIZE + OFFSET)
            pg.draw.line(self.screen, CROSS_COLOR, start_ascending, end_ascending, CROSS_WIDTH)

        elif self.player == 2:
            #draw circle
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pg.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def reset(self):
        self.__init__(self.screen)

    def is_over(self):
        return (self.board.final_state(show = True) != 0) or self.board.is_full()