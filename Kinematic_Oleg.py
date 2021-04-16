import urx
import numpy as np
from math import cos as c
from math import sin as s
from math import pi
import time

from IPython.core.display import clear_output

def move_x_y_z(x, y, z):
    p = np.array(robot_10.getl())
    p[0] = x
    p[1] = y
    p[2] = z
    robot_10.movel(p, vel=0.05, acc=0.05)


vy = 0.02

def speed_x_y_z(x, y, z):
    p = np.array(robot_10.getl())
    p[0] = x
    p[1] = y
    p[2] = z



    # if abs(p_current[0] + xa) < 0.005:
    #     try:
    #         for i in range(0, 2):
    #             robot.speedl((0, 0, 0., 0, 0, 0), 0.1, 0.1)  ##*-0.02*
    #     except:
    #         pass
    #
    # else:
    #     if xa < p_current[0]:
    #         try:
    #             for i in range(0, 2):
    #                 robot.speedl((0, vy, 0., 0, 0, 0), 0.1, 0.1)  ##*-0.02*
    #         except:
    #             pass
    #     else:
    #         try:
    #             for i in range(0, 2):
    #                 robot.speedl((0, vy, 0., 0, 0, 0), 0.1, 0.1)  ##*-0.02*
    #         except:
    #             pass



    robot_10.movel(p, vel=0.05, acc=0.05)

robot_3 = urx.Robot(host='192.168.88.161', use_rt=True)
time.sleep(1)
robot_10 = urx.Robot(host='192.168.88.162', use_rt=True)
time.sleep(1)



#th_1 = joint_pos[0]

while True:
    p_3 = robot_3.getj()
    p_10 = robot_10.getl()

    #th_1_grad = 50
    th_1 = p_3[0]
    a_1 = 0
    d_1 = 0.15185
    alpha_1 = pi/2

    #th_2 = joint_pos[1]

    #th_2_grad = 50
    th_2 = p_3[1]

    a_2 = -0.24355/2
    d_2 = 0
    alpha_2 = 0

    _0T1 = np.array([[c(th_1), -(s(th_1)) * c(alpha_1), s(th_1) * s(alpha_1), a_1 * c(th_1)],
                     [s(th_1), c(th_1) * c(alpha_1), -(c(th_1)) * s(alpha_1), a_1 * s(th_1)],
                     [0, s(alpha_1), c(alpha_1), d_1],
                     [0, 0, 0, 1]])

    _1T2 = np.array(([[c(th_2), -(s(th_2)) * c(alpha_2), s(th_2) * s(alpha_2), a_2 * c(th_2)],
                     [s(th_2), c(th_2) * c(alpha_2), -(c(th_2)) * s(alpha_2), a_2 * s(th_2)],
                     [0, s(alpha_2), c(alpha_2), d_2],
                     [0, 0, 0, 1]]))

    res = (_0T1 @ _1T2)#[:, 3][:3]




    beta = np.arctan2(-res[2,0],np.sqrt(res[0,0]**2+res[1,0]**2))

    alpha = np.arctan2(res[1,0]/c(beta), res[0,0]/c(beta))


    # print(_0T1)
    # print('===================================================================')
    #
    # print(_1T2)
    # print('===================================================================')

    #print('res =',res)

    #print('p_1 =',p_1)

    print('===================================================================')

    print('x_3c = ',res[0,3],'y_3c = ',res[1,3])

    #print('y = ',res[1,3]-0.05)

    #print('z = ',res[2,3])

    print('===================================================================')

    #print('p_10 =',p_10)

    print('x_10 =', p_10[0],'y_10 =', p_10[1])

    print('===================================================================')
    print('-------------------------------------------------------------------')
    #print('y_c =', p_2[1])

    #print('z_c =', p_2[2])



    move_x_y_z(res[0,3]+0.9, res[1,3], res[2,3])
    #p_new=(res[0,3]+0.9, res[1,3])



    time.sleep(1)
    clear_output()
    # print('alpha = ',alpha)
    #
    # print('beta = ',beta)
    #
    # print('gamma = ',np.arctan2(1, 1))
    #
    # print('alphadeg = ',90+np.rad2deg(alpha))
    #
    # print('betadeg = ',90-np.rad2deg(beta))
    #
    # print('gammadeg = ',np.arctan2(1, 1))

    #res_1 = []
    #res_1.append(res)
    #         print(res_1)

    # r = robot_3.getl()[:3]
    # r_1.append(r)