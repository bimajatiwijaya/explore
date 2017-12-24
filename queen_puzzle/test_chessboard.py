import unittest
import chessboard

class chessboard_test(unittest.TestCase):

    def setUp(self):
        self.length = 4
        self.chess_1 = chessboard.QueenChessBoard()
        self.chess_2 = chessboard.QueenChessBoard()
        self.chess_3 = chessboard.QueenChessBoard()
        self.chess_1.setup(4)
        self.chess_2.setup(2)
        self.chess_3.setup(2)

    def test_danger_block(self):
        self.chess_1.set_queen(2, 1)
        r_hor = []
        for i in range(self.length):
            r_hor.append(self.chess_1.blocks[2][i].get_status())
        self.assertEqual(True, True not in r_hor)
        l_hor = []
        for i in range(self.length):
            l_hor.append(self.chess_1.blocks[i][1].get_status())
        self.assertEqual(True, True not in l_hor)
        self.assertEqual(True, self.chess_1.blocks[0][0].get_status())
        self.assertEqual(True, self.chess_1.blocks[3][3].get_status())
        """ Diagonal test set_danger_diagonal_1 """
        self.assertEqual(False, self.chess_1.blocks[3][2].get_status())
        self.assertEqual(False, self.chess_1.blocks[1][0].get_status())
        self.assertEqual(False, self.chess_1.blocks[3][0].get_status())
        self.assertEqual(False, self.chess_1.blocks[1][2].get_status())
        self.assertEqual(False, self.chess_1.blocks[0][3].get_status())
        """ Test Undo """
        self.chess_1.take_queen(2, 1)
        for i in range(self.length):
            for j in range(self.length):
                self.assertTrue(self.chess_1.blocks[i][j].safe, 
                "Ups, this's false.")

    def test_search_save_block(self):
        self.chess_2.set_queen(0, 0)
        i, j = self.chess_2.search_save_block()
        self.assertTrue(i == -1, "Negative!")
        self.assertTrue(j == -1, "Negative!")
        i, j = self.chess_3.search_save_block()
        self.assertTrue(i >= 0, "Negative!")
        self.assertTrue(j >= 0, "Negative!")
    
    def test_play_4_x_4(self):
        self.chess_1.non_assigned_queen = 4
        solution = self.chess_1.play(3, 3)
        print "TOTAL solution ", solution
        print "Remaining queen ", self.chess_1.non_assigned_queen
        self.assertTrue(solution == 2)

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