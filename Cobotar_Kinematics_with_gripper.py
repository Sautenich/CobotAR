import urx
import numpy as np
from math import cos as c
from math import sin as s
from math import pi
import time
from matplotlib import pyplot as plt

robot_3 = urx.Robot(host='192.168.88.161', use_rt=True)
time.sleep(15)
robot_10 = urx.Robot(host='192.168.88.162', use_rt=True)
time.sleep(15)


in_3 = [-1.5514910856830042,
 -1.6902769247638147,
 -1.8206923643695276,
 -1.1367257277118128,
 1.5630582571029663,
 -20.37917019524056]

in_10 = [0.24709974229335785,
 -2.098222557698385,
 -1.8164876143084925,
 2.08876371383667,
 -0.2021549383746546,
 0.2890205681324005]


robot_10.movej(in_10, 0.5, 0.5)
time.sleep(5)
robot_3.movej(in_3, 0.5, 0.5)
time.sleep(5)

while True:
    p_1 = robot_3.getl()
    time.sleep(0.01)
    p_2 = robot_3.getl()


    while robot_3.is_program_running() and round(p_2[1], 4) - round(p_1[1], 4) < 0 and round(p_2[0], 3) - round(p_1[0],
                                                                                                                3) == 0 and round(
            p_2[2], 3) - round(p_1[2], 3) == 0:
        robot_10.speedl((0, -0.025, -0.0085, 0, 0, 0), 0.228, 0.1)
        joint_pos = robot_3.getj()

        th_1 = joint_pos[0]
        a_1 = 0
        d_1 = 0.1519
        alpha_1 = pi / 2

        th_2 = joint_pos[1]
        a_2 = -0.24365 / 2
        d_2 = 0
        alpha_2 = 0

        _0T1 = np.array(([c(th_1), -(s(th_1)) * c(alpha_1), s(th_1) * s(alpha_1), a_1 * c(th_1)],
                         [s(th_1), c(th_1) * c(alpha_1), -(c(th_1)) * s(alpha_1), a_1 * s(th_1)],
                         [0, s(alpha_1), c(th_1), d_1],
                         [0, 0, 0, 1]))

        _1T2 = np.array(([c(th_2), -(s(th_2)) * c(alpha_2), s(th_2) * s(alpha_2), a_2 * c(th_2)],
                         [s(th_2), c(th_2) * c(alpha_2), -(c(th_2)) * s(alpha_2), a_2 * s(th_2)],
                         [0, s(alpha_2), c(th_2), d_2],
                         [0, 0, 0, 1]))

        res = (_0T1 @ _1T2)[:, 3][:3]
        res_1.append(res)
        #         print(res_1)

        r = robot_3.getl()[:3]
        r_1.append(r)
    #         print(r_1)

    while robot_3.is_program_running() and round(p_2[0], 4) - round(p_1[0], 4) > 0 and round(p_2[1], 3) - round(p_1[1],
                                                                                                                3) == 0 and round(
            p_2[2], 3) - round(p_1[2], 3) == 0:
        robot_10.speedl((0.0135, -0.0162, 0.0028, 0, 0, 0), 0.1, 0.1)

        joint_pos = robot_3.getj()
        th_1 = joint_pos[0]
        a_1 = 0
        d_1 = 0.1519
        alpha_1 = pi / 2

        th_2 = joint_pos[1]
        a_2 = -0.24365 / 2
        d_2 = 0
        alpha_2 = 0

        _0T1 = np.array(([c(th_1), -(s(th_1)) * c(alpha_1), s(th_1) * s(alpha_1), a_1 * c(th_1)],
                         [s(th_1), c(th_1) * c(alpha_1), -(c(th_1)) * s(alpha_1), a_1 * s(th_1)],
                         [0, s(alpha_1), c(th_1), d_1],
                         [0, 0, 0, 1]))

        _1T2 = np.array(([c(th_2), -(s(th_2)) * c(alpha_2), s(th_2) * s(alpha_2), a_2 * c(th_2)],
                         [s(th_2), c(th_2) * c(alpha_2), -(c(th_2)) * s(alpha_2), a_2 * s(th_2)],
                         [0, s(alpha_2), c(th_2), d_2],
                         [0, 0, 0, 1]))

        res = (_0T1 @ _1T2)[:, 3][:3]
        res_2.append(res)
        #         print(res_2)

        r = robot_3.getl()[:3]
        r_2.append(r)
    #         print(r_2)

    while robot_3.is_program_running() and round(p_2[1], 4) - round(p_1[1], 4) > 0 and round(p_2[0], 3) - round(p_1[0],
                                                                                                                3) == 0 and round(
            p_2[2], 3) - round(p_1[2], 3) == 0:
        robot_10.speedl((0, 0.023, 0.006, 0, 0, 0), 0.125, 0.1)

        joint_pos = robot_3.getj()
        th_1 = joint_pos[0]
        a_1 = 0
        d_1 = 0.1519
        alpha_1 = pi / 2

        th_2 = joint_pos[1]
        a_2 = -0.24365 / 2
        d_2 = 0
        alpha_2 = 0

        _0T1 = np.array(([c(th_1), -(s(th_1)) * c(alpha_1), s(th_1) * s(alpha_1), a_1 * c(th_1)],
                         [s(th_1), c(th_1) * c(alpha_1), -(c(th_1)) * s(alpha_1), a_1 * s(th_1)],
                         [0, s(alpha_1), c(th_1), d_1],
                         [0, 0, 0, 1]))

        _1T2 = np.array(([c(th_2), -(s(th_2)) * c(alpha_2), s(th_2) * s(alpha_2), a_2 * c(th_2)],
                         [s(th_2), c(th_2) * c(alpha_2), -(c(th_2)) * s(alpha_2), a_2 * s(th_2)],
                         [0, s(alpha_2), c(th_2), d_2],
                         [0, 0, 0, 1]))

        res = (_0T1 @ _1T2)[:, 3][:3]
        res_3.append(res)
        #         print(res_3)

        r = robot_10.getl()[:3]
        r_3.append(r)
    #         print(r_3)

    while robot_3.is_program_running() and round(p_2[0], 4) - round(p_1[0], 4) < 0 and round(p_2[1], 3) - round(p_1[1],
                                                                                                                3) == 0 and round(
            p_2[2], 3) - round(p_1[2], 3) == 0:
        robot_10.speedl((-0.0135, 0.02, -0.001, 0, 0, 0), 0.1, 0.1)

        joint_pos = robot_3.getj()
        th_1 = joint_pos[0]
        a_1 = 0
        d_1 = 0.1519
        alpha_1 = pi / 2

        th_2 = joint_pos[1]
        a_2 = -0.24365 / 2
        d_2 = 0
        alpha_2 = 0

        _0T1 = np.array(([c(th_1), -(s(th_1)) * c(alpha_1), s(th_1) * s(alpha_1), a_1 * c(th_1)],
                         [s(th_1), c(th_1) * c(alpha_1), -(c(th_1)) * s(alpha_1), a_1 * s(th_1)],
                         [0, s(alpha_1), c(th_1), d_1],
                         [0, 0, 0, 1]))

        _1T2 = np.array(([c(th_2), -(s(th_2)) * c(alpha_2), s(th_2) * s(alpha_2), a_2 * c(th_2)],
                         [s(th_2), c(th_2) * c(alpha_2), -(c(th_2)) * s(alpha_2), a_2 * s(th_2)],
                         [0, s(alpha_2), c(th_2), d_2],
                         [0, 0, 0, 1]))

        res = (_0T1 @ _1T2)[:, 3][:3]
        res_4.append(res)
        #         print(res_4)

        r = robot_10.getl()[:3]
        r_4.append(r)
#         print(r_4)
