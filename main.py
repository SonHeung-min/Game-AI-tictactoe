import sys 
import pygame as pg
import time
import os


from constant import *
from game import Game

#PYGAME SETUP
pg.init()
pg.mixer.init()
pg.mixer.music.load(os.path.join("assets", "background_music.mp3")) 
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1) 
screen = pg.display.set_mode( (WIDTH, HEIGHT) )
pg.display.set_caption("TIC TAC TOE AI GAME")
#screen.fill( BACKGROUND_COLOR )

def main():

    #object
    game = Game(screen)
    board = game.board
    ai = game.ai

    #mainloop
    while True:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                #r - restart 
                if event.key == pg.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE

                if board.empty_sqr(row, col) and game.running == True:
                    game.make_move(row, col)
                    # print(board.squares)

                    if game.is_over():
                        game.running = False
        
        if game.player == ai.player and game.running == True:
            #update the screen 
            pg.display.update()
            time.sleep(0.5)

            #ai methods
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.is_over():
                game.running = False

        pg.display.update()

main()