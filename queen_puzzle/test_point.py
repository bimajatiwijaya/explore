import unittest
import point

class point_test(unittest.TestCase):

    def test_point(self):
        point_1 = point.Point(4, 5)
        self.assertEqual(43, point_1.get_x())

