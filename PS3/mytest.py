import random

from ps3 import *


# #z = RectangularRoom(3, 3, 5)
z = EmptyRoom(3 ,3 ,5)
r = StandardRobot(z, 1, 5)

r.update_position_and_clean()


