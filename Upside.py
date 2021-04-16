

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


robot_3.translate((0.0, 0, 0.1), acc=0.05, vel=0.05) #acceleration, velocity

