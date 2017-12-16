import point
import chees_block

a = point.Point(4, 5)
print a.get_x()
print a.get_y()

a = chees_block.CheesBlock(army='sss', safe=True)
a.set_point(x=0, y=0)
print a.get_block_status()
print a.get_x()
print a.get_y()
# print a.get_x()
