from detection import *
import os
directory = os.getcwd()
path = directory + '/Original.PNG'
min_radius =10
max_radius = 300
param1 = 105
param2 = 33
detect_circles(path, min_radius, max_radius, param1, param2)
