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
    total_queen = 0
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

    def setup(self, length=0):
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

    def set_queen(self, x=0, y=0):
        """ Assign queen in chess board """
        if self.configured:
            block = self.blocks[x][y]
            if not block.set_block_status():
                block.set_army(army="queen")
                self.update_danger_block(x=x, y=y)
        else:
            print "Class not setup yet."

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


    def set_danger_horisontal(self, x=0, y=0, go_right=True):
        """ Update status to danger horisontal (right) """
        if go_right:
            if x < self.length:
                self.blocks[x][y].set_not_safe()
                self.set_danger_horisontal(x+1, y, True)
            else:
                return
        else:
            if x > -1:
                self.blocks[x][y].set_not_safe()
                self.set_danger_horisontal(x-1, y, False)
            else:
                return

    def set_danger_vertical(self, x=0, y=0, go_up=True):
        """ Update status to danger vertically """
        if go_up:
            if y < self.length:
                self.blocks[x][y].set_not_safe()
                self.set_danger_vertical(x, y+1, True)
            else:
                return
        else:
            if y >= 0:
                self.blocks[x][y].set_not_safe()
                self.set_danger_vertical(x, y-1, False)
            else:
                return

