import unittest
import chessboard

class chessboard_test(unittest.TestCase):

    def setUp(self):
        self.length = 4
        self.chess_1 = chessboard.QueenChessBoard()
        self.chess_1.setup(4)
        self.chess_1.set_queen(2, 1)

    def test_danger_block(self):
        r_hor = []
        for i in range(self.length):
            r_hor.append(self.chess_1.blocks[2][i].get_status())
        self.assertEqual(True, not all(r_hor))
        l_hor = []
        for i in range(self.length):
            r_hor.append(self.chess_1.blocks[i][1].get_status())
        self.assertEqual(True, not all(r_hor))
        self.assertEqual(True, self.chess_1.blocks[0][0].get_status())
        self.assertEqual(True, self.chess_1.blocks[3][3].get_status())

if __name__ == '__main__':
    unittest.main()

'''
        for i in range(self.length):
            line = ''
            for j in range(self.length):
                line += '(['+ str(i) +','+ str(j) +'], '+ \
                str(self.chess_1.blocks[i][j].get_status()) +')'
            print line
        print '-------------'
'''