import unittest
import point

class point_test(unittest.TestCase):

    def test_point(self):
        point_1 = point.Point()
        point_1.set_point(4, 5)
        self.assertEqual(4, point_1.get_x())

if __name__ == '__main__':
    unittest.main()