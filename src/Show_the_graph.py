import urx
import time
import numpy as np
from math import cos as c
from math import sin as s
from math import pi
from matplotlib import pyplot as plt
import pickle
import matplotlib.pyplot as plt

#Unpickling
with open("/home/cobotar/Desktop/venv/SwarmGesture-main/Main.txt", "rb") as fp:
    b = pickle.load(fp)

print(b)
plt.plot(np.array(b)[:,0], np.array(b)[:,1])

plt.show()

