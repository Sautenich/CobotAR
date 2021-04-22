

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
import pickle

cord_recorded = []
lines_recorded = []
poses = []
gesture_ml = 0

robot_3 = urx.Robot(host='192.168.88.146', use_rt=True)
time.sleep(1)

while True:
    poses.append(robot_3.getl()[:3])
    with open("Main.txt", "wb") as fp:
        pickle.dump(poses, fp)
    try:
        robot_3.translate((0.15, 0, 0.), acc=0.05, vel=0.05)
        time.sleep(5)
    except:
        pass

    try:
        robot_3.translate((0., -0.15, 0.), acc=0.05, vel=0.05)
        time.sleep(5)
    except:
        pass

    try:
        robot_3.translate((-0.15, 0, 0.), acc=0.05, vel=0.05)
        time.sleep(5)
    except:
        pass

    try:
        robot_3.translate((0., 0.15, 0.), acc=0.05, vel=0.05)
        time.sleep(5)
    except:
        pass




