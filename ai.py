import random

from board import Board

class AI:

    def __init__(self, player = 2):
        self.player = player
    
    def random_sqr(self, board):
        empty_squares = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_squares))
    
        return empty_squares[idx]       # (row, col)

    def minimax(self, board, maximizing):

        #terminal case 
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1, None  # eval, move
        
        # player 2 wins
        if case == 2:
            return -1, None
        
        #draw 
        elif board.is_full():
            return 0, None
        
        if maximizing:
            max_eval = -100
            best_move = None
            empty_squares = board.get_empty_sqrs()

            for (row, col) in empty_squares:
                temp_board = Board(board.screen)  
                temp_board.squares = board.squares.copy()  
                temp_board.marked_squares = board.marked_squares
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                
            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_squares = board.get_empty_sqrs()

            for (row, col) in empty_squares:
                temp_board = Board(board.screen)  
                temp_board.squares = board.squares.copy()  
                temp_board.marked_squares = board.marked_squares
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                
            return min_eval, best_move

    def eval(self, main_board):
        #minimax algorithm choice
        eval, move = self.minimax(main_board, False)
            
        return move  # (row, col)
