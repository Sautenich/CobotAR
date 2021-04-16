

#!/usr/bin/env python
import roslib;


import rospy
from std_msgs.msg import String
import urx
import numpy as np
from math import cos as c
from math import sin as s
from math import pi
import time


robot_3 = urx.Robot(host='192.168.88.146', use_rt=True)
time.sleep(1)
# robot_10 = urx.Robot(host='192.168.88.162', use_rt=True)
# time.sleep(1)

# in_10_1 = [0.15278202295303345,
#  -1.8995736281024378,
#  -1.971581761037008,
#  2.416182518005371,
#  -0.6119654814349573,
#  -0.01534444490541631]
# robot_10.movej(in_10_1, 0.5, 0.5)

in_3_1 = [-1.5563376585589808,
 -2.1601994673358362,
 -2.034036938344137,
 -0.5079453627215784,
 1.5514748096466064,
 -14.1198191165766]
robot_3.movej(in_3_1, 0.5, 0.5)





