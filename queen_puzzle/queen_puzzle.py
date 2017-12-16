import chessboard


board = chessboard.QueenChessBoard()
board.setup(length=8)
board.set_queen(x=0, y=0)
print board.blocks[0][0].get_army()
print board.blocks[0][0].get_status()
