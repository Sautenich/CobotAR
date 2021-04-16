
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



robot_3 = urx.Robot(host='192.168.88.146', use_rt=True)
time.sleep(3)
robot_10 = urx.Robot(host='192.168.88.162', use_rt=True)
time.sleep(3)


# in_3_1 = [-1.5563376585589808,
#  -2.1601994673358362,
#  -2.034036938344137,
#  -0.5079453627215784,
#  1.5514748096466064,
#  -14.1198191165766]
# robot_3.movej(in_3_1, 0.5, 0.5)

in_10_1 = [0.15278202295303345,
 -1.8995736281024378,
 -1.971581761037008,
 2.416182518005371,
 -0.6119654814349573,
 -0.01534444490541631]
robot_10.movej(in_10_1, 0.5, 0.5)




#Пoложение точки в конкретной позиции

b=[0,0]
a=0
c=0



# def move(c):
#     if c == 1:
#         for i in 60:
#             robot_3.speedl((0, -0.02, 0, 0, 0, 0), 0.1, 0.5)
#             robot_10.speedl((0, -0.008, -0.004, 0.077, 0, 0), 0.1, 0.5)
#
#     elif c == 2:
#         for i in 60:
#             robot_3.speedl((0.02, 0, 0, 0, 0, 0), 0.1, 0.5)
#             robot_10.speedl((0.002, -0.006, 0, -0.02, 0, 0), 0.1, 0.5)
#
#     elif c == 3:
#         for i in 60:
#             robot_3.speedl((0, 0.02, 0, 0, 0, 0), 0.1, 0.5)
#             robot_10.speedl((0, 0.007, 0.004, -0.07, 0, 0), 0.1, 0.5)
#
#     elif c == 4:
#         for i in 60:
#             robot_3.speedl((-0.02, 0, 0, 0, 0, 0), 0.1, 0.5)
#             robot_10.speedl((-0.002, 0.007, 0, 0, 0, 0), 0.1, 0.5)


def callback(data):
    try:
        #rospy.loginfo(data.data)
        a = data.data
        b.append(a)

        return a
        #print('b =',b)
    except:
        pass



def listener():
    try:
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('/robot_control', String, callback)
        #print(b)

        #rospy.spin()
    except:
        pass



if __name__ == '__main__':

    while True:
        try:



            listener()

            c = int(b[-1])

            # print('A =', a)
            # print('B =', b)
            print('C =', c)

            if c == 1:
                # for i in range(0,1):
                    robot_3.speedl((0, -0.02, 0, 0, 0, 0), 0.1, 0.5)
                    robot_10.speedl((0, -0.0035, -0.0055, 0.055, 0, 0), 0.1, 0.5)

                # print('The process is finished Ok')
                # if c !=1:
                #     break
            if c == 2:
                # for i in range(0, 1):
                    robot_3.speedl((0.02, 0, 0, 0, 0, 0), 0.1, 0.5)
                    robot_10.speedl((0.01, -0.005, 0.001, -0.009, 0, 0), 0.1, 0.5)
                # if c !=2:
                #     break

            if c == 3:
                # for i in range(0, 1):
                    robot_3.speedl((0, 0.02, 0, 0, 0, 0), 0.1, 0.5)
                    robot_10.speedl((0.004, 0.001, 0.0055, -0.06, 0, 0), 0.1, 0.5)
                # if c !=3:
                #     break

            if c == 4:
                # for i in range(0, 1):
                    robot_3.speedl((-0.02, 0, 0, 0, 0, 0), 0.1, 0.5)
                    robot_10.speedl((-0.008, 0.006, 0, 0.01, 0, 0), 0.1, 0.5)
                # if c !=4:
                #     break
        except:
            pass


