'''creating a connect 4 game inspired by Keith Galli'''

from numpy import zeros as array_zero
from numpy import flip as flip_that

##=========================================== PLAYER
class LOGIC():
    def __init__(self):
        self.OVER = False
        self.YOUR_TURN = 0
        self.change_turn = True
        self.fill_that_space_OBJ = self.Filler()
        self.piece = 0
        self.main_location = (0,0)
        self.WIN = False
        self.winning_location = []
        self.game_condition = None #has 4 possible values 'NONE', 'TIE', 'NEXT ROUND', 'GAME TIED'
        self.GAME_MODE = 'SINGLE MATCH'
        self.back_up_MODE = ''
        self.make_win = 0
        self.loser = 0

        self.PLAYER_1_SCORE = 0
        self.PLAYER_2_SCORE = 0

        ##========================================== INIT OF PLAYERS AND GAME BOARD
        '''init of main_gameboard'''
        self.main_gameboard = self.Game_Board()
        '''normal unflipped board'''
        self.main_gameboard._main_gameboard()
        self.board = self.main_gameboard.temp_board
        '''board specifications'''
        self.board_ROW = self.main_gameboard.Gboard_DIM[0] #this is equal to six
        self.board_COL = self.main_gameboard.Gboard_DIM[1] #this is equal to seven

        '''players init'''
        self.player1 = self.Players(1)
        self.player2 = self.Players(2)
##----------------------------------------- saving variables BETA
        self.save_board = []
        self.FROM_SAVES = False

    def reset_LOGIC(self):
        self.OVER = False
        self.YOUR_TURN = 0
        self.change_turn = True
        self.fill_that_space_OBJ = self.Filler()
        self.piece = 0
        self.main_location = (0,0)
        self.WIN = False
        self.winning_location = []
        self.game_condition = None #has 4 possible values 'NONE', 'TIE', 'NEXT ROUND', 'GAME TIED'
        self.GAME_MODE = 'SINGLE MATCH'
        self.back_up_MODE = ''
        self.make_win = 0
        self.loser = 0

        self.PLAYER_1_SCORE = 0
        self.PLAYER_2_SCORE = 0

        ##========================================== INIT OF PLAYERS AND GAME BOARD
        '''init of main_gameboard'''
        self.main_gameboard = self.Game_Board()
        '''normal unflipped board'''
        self.main_gameboard._main_gameboard()
        self.board = self.main_gameboard.temp_board
        '''board specifications'''
        self.board_ROW = self.main_gameboard.Gboard_DIM[0] #this is equal to six
        self.board_COL = self.main_gameboard.Gboard_DIM[1] #this is equal to seven

        '''players init'''
        self.player1 = self.Players(1)
        self.player2 = self.Players(2)


    def get_GAME_CONDITION(self):
        return self.game_condition

    def get_B4_winner(self):
        return self.make_win

    def get_CURRENT_SCORE(self,player_num = 0):
        if player_num == 1:
            return self.PLAYER_1_SCORE
        elif player_num == 2:
            return self.PLAYER_2_SCORE
        else: pass

    def save_try(self): #BETA
        return self.save_board

    def reset_SM_match(self):
        self.YOUR_TURN = 0
        self.PLAYER_1_SCORE = 0
        self.PLAYER_2_SCORE = 0
        self.piece = 0;self.WIN = False

    def reset_B4_match(self):
        if self.back_up_MODE == 'BEST OF 4': self.YOUR_TURN = self.loser
        elif self.back_up_MODE == 'SINGLE MATCH': self.YOUR_TURN = 0
        if self.PLAYER_1_SCORE == 4 or self.PLAYER_2_SCORE == 4:
            self.PLAYER_1_SCORE = 0
            self.PLAYER_2_SCORE = 0
        self.piece = 0;self.WIN = False

    def create_GAME_MODE(self,mode='SINGLE MATCH'):
        self.GAME_MODE = mode
        self.back_up_MODE = mode

    def get_GAME_MODE(self):
        return self.GAME_MODE

    def get_BLITPOS(self):
        return [self.piece,self.main_location]

    def get_TURN(self):
        return self.YOUR_TURN

    def tell_WINNER(self):
        return [self.piece,self.WIN]

    def create_new_board(self):
        self.make_win = 0
        self.game_condition = None
        self.main_gameboard = self.Game_Board()
        '''normal unflipped board'''
        self.main_gameboard._new_gameboard()
        self.board = self.main_gameboard.temp_board

    def create_board_from_SAVE(self): #BETA
        self.YOUR_TURN = 0
        self.FROM_SAVES = True
        self.board = self.save_board

    class Players():
        '''containes the selected column of the player and to initialize input'''
        def __init__(self,player_num=0):
                self.player_piece =player_num
                self.selected_col = 0
                self.player_number = player_num

        def _player_selected(self,col):
                self.selected_col = col

        def _player_selectedtest(self):
                self.selected_col = input('col: ')

    ##=========================================== GAME BOARD

    class Game_Board():
        '''the class to create the main gameboard'''
        def __init__(self):
                '''dimension of main_gameboard'''
                self.Gboard_DIM = grow, gcol = 6,7
                self.temp_board = []

        def _main_gameboard(self):
                '''this will create the gameboard'''
                gameboard = array_zero(self.Gboard_DIM)
                self.temp_board = gameboard

        def _new_gameboard(self):
            '''this will create a new blank board'''
            gameboard = array_zero(self.Gboard_DIM)
            self.temp_board = gameboard

    ##=========================================== VALIDATOR CHECKER

    class Validator():
        '''validator test if the space is free or not yet occupied'''
        def __init__(self,gameboard,col_num=0):
                self.gboard = gameboard
                self.col_num = int(col_num)
                self.Main_Board_DIM = grow, gcol = 6,7
                self.count_truth = 0


        def _check_pos_possible(self):
                return self.gboard[5][self.col_num] == 0

        def _check_for_TIE(self):
                for col_scan in range(self.Main_Board_DIM[1]):
                    if self.gboard[5][col_scan] != 0:
                        self.count_truth += 1
                return self.count_truth

        def _tell_emptyrow(self):
                for row_scan in range(self.Main_Board_DIM[0]):
                        if self.gboard[row_scan][self.col_num] == 0:
                                return row_scan

    ##=========================================== GAME BOARD FILLER AND FLIPPER

    class Filler():
        '''assign the player choice to the space of the array and flip the game board'''
        def __init__(self,board=[],row=0,col=0,p_num=0):
            self.board = board
            self.row = int(row)
            self.col = int(col)
            self.p_num = p_num
            self.board_flipped_OBJ = self._Board_flipper(self.board)
            self.flipped_board = self.board_flipped_OBJ._flip()
            self.__BLIT_POS = {}

        def _fill_that_space(self):
            self.board[self.row][self.col] = self.p_num
            self.flipped_board = self.board_flipped_OBJ._flip()
            return self.board

        class _Board_flipper():
            def __init__(self,board):
                self.gboard_to_flip = board

            def _flip(self):
                return flip_that(self.gboard_to_flip,0)

    ##=========================================== WIN VALIDATOR

    class Win_Validator():
        '''check if formed a winning combination'''
        def __init__(self,board,board_size=(),p1=''):
            self._board_size = board_size
            self._board = board
            self._player_piece = p1
            self.win_location = []

        def _win(self):
            '''horiz'''
            for col in range(self._board_size[1]-3): ##column - 3
                for row in range(self._board_size[0]): ##row
                    if self._board[row][col] == self._player_piece and self._board[row][col+1] == self._player_piece and self._board[row][col+2] == self._player_piece and self._board[row][col+3] == self._player_piece:
                        self.win_location = [(row,col),(row,col+1),(row,col+2),(row,col+3)]
                        return True
            '''ver'''
            for col in range(self._board_size[1]): ##column
                for row in range(self._board_size[0]-3): ##row - 3
                    if self._board[row][col] == self._player_piece and self._board[row+1][col] == self._player_piece and self._board[row+2][col] == self._player_piece and self._board[row+3][col] == self._player_piece:
                        self.win_location = [(row,col),(row+1,col),(row+2,col),(row+3,col)]
                        return True

            '''pos_diag'''
            for col in range(self._board_size[1]-3): ##column - 3
                for row in range(self._board_size[0]-3): ##row -3
                    if self._board[row][col] == self._player_piece and self._board[row+1][col+1] == self._player_piece and self._board[row+2][col+2] == self._player_piece and self._board[row+3][col+3] == self._player_piece:
                        self.win_location = [(row,col),(row+1,col+1),(row+2,col+2),(row+3,col+3)]
                        return True

            '''neg_diag'''
            for col in range(self._board_size[1]-3): ##column - 3
                for row in range(3,self._board_size[0]): ##row -3
                    if self._board[row][col] == self._player_piece and self._board[row-1][col+1] == self._player_piece and self._board[row-2][col+2] == self._player_piece and self._board[row-3][col+3] == self._player_piece:
                        self.win_location = [(row,col),(row-1,col+1),(row-2,col+2),(row-3,col+3)]
                        return True

 ##=========================================== LOGIC ENDS HERE

    def Player_input(self,colx):
        print('\nPLAYER:',self.YOUR_TURN+1)
        ##============================================= player 1 ==============================================
        if self.YOUR_TURN == 0: #PLAYER 1 INPUT
            self.change_turn = True
            self.player1._player_selected(colx) #INPUT METHOD INCLUDING THE PLAYER PIECE
            col = self.player1.selected_col
            is_valid1 = self.Validator(self.board,col) #CREATING AN OBJECT FOR THE CLASS VALIDATOR
            if is_valid1._check_pos_possible(): #POSITION IS POSSIBLE
                    row = is_valid1._tell_emptyrow() #RETURN THE EMPTY ROW
                    col = self.player1.selected_col
                    self.main_location = (row, col)
                    self.piece = self.player1.player_piece
                    filler = self.Filler(self.board,row,col,self.player1.player_piece) #CREATING AN OBJECT FOR THE CLASS FILLER
                    self.save_board = self.board
                    testBoard = filler._fill_that_space() #FILL THE BOARD WITH PLAYER PIECE
                    printedBoard = filler.flipped_board #FLIPPED THE BOARD
                    win1 = self.Win_Validator(testBoard,(self.board_ROW,self.board_COL),self.player1.player_piece) #VALIDATE THE WIN
                    print('TURN NUMBER:"-',self.YOUR_TURN)
                    print('BOARD:\n',printedBoard)
                    ## ========================================= SINGLE MATCH =====================================
                    if self.GAME_MODE == 'SINGLE MATCH':
                        if win1._win():
                            #-------------------------------------------- WIN MATCH PLAYER 1 WIN
                            print ('PLAYER 1 WIN')
                            print('FINAL BOARD:\n',printedBoard)
                            self.WIN = True
                            self.winning_location = win1.win_location
                        elif is_valid1._check_for_TIE() == 7 and self.WIN == False: #--------- TIE MATCH
                            self.game_condition = 'TIE'
                    ## ========================================= BEST OF 4 =====================================
                    elif self.GAME_MODE == 'BEST OF 4':
                        if win1._win():
                            self.loser = 1 #-------------------------------------------- WIN MATCH PLAYER 2 WIN
                            self.make_win = 1
                            self.PLAYER_1_SCORE += 1
                            if self.PLAYER_1_SCORE == 4:
                                print ('PLAYER 1 WIN')
                                print('FINAL BOARD:\n',printedBoard)
                                self.WIN = True
                                self.winning_location = win1.win_location
                            else: self.game_condition = 'NEXT ROUND'; print(self.PLAYER_1_SCORE)
                        elif is_valid1._check_for_TIE() == 7 and self.WIN == False: #--------- TIE MATCH
                            self.game_condition = 'GAME TIED'
            else:
                self.change_turn = False
                self.YOUR_TURN = 0

        else:
            ##============================================= player 2 ==============================================
            self.player2._player_selected(colx)
            col = self.player2.selected_col
            is_valid2 = self.Validator(self.board,col)
            if is_valid2._check_pos_possible():
                    self.change_turn = True
                    row2 = is_valid2._tell_emptyrow()
                    col2 = self.player2.selected_col
                    self.main_location = (row2, col2)
                    self.piece = self.player2.player_piece
                    filler2 = self.Filler(self.board,row2,col2,self.player2.player_piece)
                    self.save_board = self.board
                    testBoard = filler2._fill_that_space()
                    printedBoard = filler2.flipped_board
                    win2 = self.Win_Validator(testBoard,(self.board_ROW,self.board_COL),self.player2.player_piece)
                    print('TURN NUMBER:"-',self.YOUR_TURN)
                    print('BOARD:\n',printedBoard)
                    ## ========================================= SINGLE MATCH =====================================
                    if self.GAME_MODE == 'SINGLE MATCH':
                        if win2._win(): #-------------------------------------------- WIN MATCH PLAYER 2 WIN
                            print ('PLAYER 2 WIN')
                            print('FINAL BOARD:\n',printedBoard)
                            self.WIN = True
                            self.winning_location = win2.win_location
                        elif is_valid2._check_for_TIE() == 7 and self.WIN == False: #--------- TIE MATCH
                            self.game_condition = 'TIE'
                    ## ========================================= BEST OF 4 =====================================
                    elif self.GAME_MODE == 'BEST OF 4':
                        if win2._win():
                            self.loser = 0 #-------------------------------------------- WIN MATCH PLAYER 2 WIN
                            self.make_win = 2
                            self.PLAYER_2_SCORE += 1
                            if self.PLAYER_2_SCORE == 4:
                                print ('PLAYER 2 WIN')
                                print('FINAL BOARD:\n',printedBoard)
                                self.WIN = True
                                self.winning_location = win2.win_location
                            else: self.game_condition = 'NEXT ROUND'; print(self.PLAYER_2_SCORE)
                        elif is_valid2._check_for_TIE() == 7 and self.WIN == False: #--------- TIE MATCH
                            self.game_condition = 'GAME TIED'

            else:
                self.change_turn = False
                self.YOUR_TURN = 1

        if self.change_turn:
            self.YOUR_TURN +=  1
            self.YOUR_TURN %= 2

logic = LOGIC()


if __name__ == '__main__':
    logic = LOGIC()
