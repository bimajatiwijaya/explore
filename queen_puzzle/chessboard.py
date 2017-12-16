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
        self.blocks = [[0 for x in range(length)] for y in range(length)] 
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
        """ Update status each block (up and down):
        1. horisontal 
        2. vertical
        3. diagonal
        """
        if self.length == x or x == -1:
            return
        elif x < self.length or x > -1:
            self.blocks[x][y].set_not_safe()
            self.update_danger_block(x=x+1, y=y)
            self.update_danger_block(x=x-1, y=y)
        elif self.length == y or y == -1:
            return
        elif y < self.length or y > -1:
            self.blocks[x][y].set_not_safe()
            self.update_danger_block(x=x, y=y+1)
            self.update_danger_block(x=x, y=y-1)
        elif self.length == x == y or x == y == -1:
            pass
        else:
            self.blocks[x][y].set_not_safe()
            self.update_danger_block(x=x+1, y=y+1)
            self.update_danger_block(x=x-1, y=y-1)
