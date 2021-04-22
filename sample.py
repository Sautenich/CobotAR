import urx
import time
import numpy as np
from math import cos as c
from math import sin as s
from math import pi
from matplotlib import pyplot as plt
import pickle

#Unpickling
with open("Accuracy_Name_experiment.txt", "rb") as fp:
    b = pickle.load(fp)

print(b)