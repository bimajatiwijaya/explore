import chess_block
"""
1.  Set 1 queen in position (x,y).
2.  Mark as danger for chess_block which possible 
    attack by queen.
3.  Is all chessboard danger and total queen in board < 8
    a. yes : return 0 and back to poin 1 with different position
4.  Total queen == 8
    return 1
"""
class QueenChessBoard():
    """ Class queen board """
    non_assigned_queen = 0
    length = 0
    configured = False
    blocks = []
    save_blocks = []
    danger_blocks = []

    def __init__(self):
        """ constructor chessboard """
        self.length = 0
        self.configured = False
        self.blocks = []
        self.save_blocks = []
        self.danger_blocks = []

    def setup(self, length=0, total_queen=0):
        """ setup chessboard and chess_block """
        self.length = length
        self.blocks = \
            [[0 for x in range(length)] for y in range(length)] 
        for i in range(0, self.length):
            for j in range(0, self.length):
                a_block = chess_block.ChessBlock()
                a_block.set_chess_block(
                    x=i, y=j, army="")
                self.blocks[i][j] = a_block
        self.save_blocks = self.blocks
        self.configured = True
        self.non_assigned_queen = total_queen

    def set_queen(self, x=0, y=0):
        """ Assign queen in chess board """
        if self.configured:
            block = self.blocks[x][y]
            if not block.set_block_status():
                block.set_army(army="queen")
                self.update_danger_block(x, y)
        else:
            print "Class not setup yet."

    def play(self, x=0, y=0):
        """ play and return total solution """
        i, j = self.search_save_block()
        if i == -1 and self.non_assigned_queen > 0:
            # No place for non assigned queen
            return 0
        elif i == -1 and self.non_assigned_queen == 0:
            # solution found
            return 1
        else:
            self.blocks[i][j].set_army(army="queen")
            self.update_danger_block(i, j)
            self.non_assigned_queen -= 1 
            return 0 + self.play(i, j)

    def search_save_block(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.blocks[i][j].get_status():
                    return i, j
        return -1, -1

    def update_danger_block(self, x=0, y=0):
        """ 
        Update status each block (up and down):
        1. horisontal (right & left)
        2. vertical (up & down)
        3. diagonal (right & left)
        """
        self.set_danger_horisontal(x, y, True)
        self.set_danger_horisontal(x, y, False)
        self.set_danger_vertical(x, y, True)
        self.set_danger_vertical(x, y, False)
        self.set_danger_diagonal_1(x, y, True)
        self.set_danger_diagonal_1(x, y, False)
        self.set_danger_diagonal_2(x, y, True)
        self.set_danger_diagonal_2(x, y, False)

    def take_queen(self, x=0, y=0):
        self.set_save_horisontal(x, y, True)
        self.set_save_horisontal(x, y, False)
        self.set_save_vertical(x, y, True)
        self.set_save_vertical(x, y, False)
        self.set_save_diagonal_1(x, y, True)
        self.set_save_diagonal_1(x, y, False)
        self.set_save_diagonal_2(x, y, True)
        self.set_save_diagonal_2(x, y, False)

    # DANGER
    def set_danger_horisontal(self, x=0, y=0, go_right=True):
        """ Update status to danger horisontal (right) """
        if go_right:
            if x < self.length:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_horisontal(x+1, y, True)
            else:
                return
        else:
            if x > -1:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_horisontal(x-1, y, False)
            else:
                return

    def set_danger_vertical(self, x=0, y=0, go_up=True):
        """ Update status to danger vertically """
        if go_up:
            if y < self.length:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_vertical(x, y+1, True)
            else:
                return
        else:
            if y >= 0:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_vertical(x, y-1, False)
            else:
                return

    def set_danger_diagonal_1(self, x=0, y=0, go_up=True):
        """ Diagonal 1 x and y increase and diagoal left 
        x and y decrease """
        if go_up:
            if y < self.length and x < self.length:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_diagonal_1(x+1, y+1, True)
            else:
                return
        else:
            if y >= 0 and x >=0:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_diagonal_1(x-1, y-1, False)
            else:
                return

    def set_danger_diagonal_2(self, x=0, y=0, go_up=True):
        """ diagonal 2 x decrease and y increase
        diagoal x increase and y decrease """
        if go_up:
            if y < self.length and x >= 0:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_diagonal_2(x-1, y+1, True)
            else:
                return
        else:
            if x < self.length and y >= 0:
                self.blocks[x][y].attack_queen_block()
                self.set_danger_diagonal_2(x+1, y-1, False)
            else:
                return False

    # SET SAVE
    def set_save_horisontal(self, x=0, y=0, go_right=True):
        """ Update status to danger horisontal (right) """
        if go_right:
            if x < self.length:
                self.blocks[x][y].clean_block()
                self.set_save_horisontal(x+1, y, True)
            else:
                return
        else:
            if x > -1:
                self.blocks[x][y].clean_block()
                self.set_save_horisontal(x-1, y, False)
            else:
                return

    def set_save_vertical(self, x=0, y=0, go_up=True):
        """ Update status to danger vertically """
        if go_up:
            if y < self.length:
                self.blocks[x][y].clean_block()
                self.set_save_vertical(x, y+1, True)
            else:
                return
        else:
            if y >= 0:
                self.blocks[x][y].clean_block()
                self.set_save_vertical(x, y-1, False)
            else:
                return

    def set_save_diagonal_1(self, x=0, y=0, go_up=True):
        """ Diagonal 1 x and y increase and diagoal left 
        x and y decrease """
        if go_up:
            if y < self.length and x < self.length:
                self.blocks[x][y].clean_block()
                self.set_save_diagonal_1(x+1, y+1, True)
            else:
                return
        else:
            if y >= 0 and x >=0:
                self.blocks[x][y].clean_block()
                self.set_save_diagonal_1(x-1, y-1, False)
            else:
                return

    def set_save_diagonal_2(self, x=0, y=0, go_up=True):
        """ diagonal 2 x decrease and y increase
        diagoal x increase and y decrease """
        if go_up:
            if y < self.length and x >= 0:
                self.blocks[x][y].clean_block()
                self.set_save_diagonal_2(x-1, y+1, True)
            else:
                return
        else:
            if x < self.length and y >= 0:
                self.blocks[x][y].clean_block()
                self.set_save_diagonal_2(x+1, y-1, False)
            else:
                return False

