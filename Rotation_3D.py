def Rx(theta):
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, mt.cos(theta),-mt.sin(theta)],
                   [ 0, mt.sin(theta), mt.cos(theta)]])
  
def Ry(theta):
  return np.matrix([[ mt.cos(theta), 0, mt.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-mt.sin(theta), 0, mt.cos(theta)]])
  
def Rz(theta):
  return np.matrix([[ mt.cos(theta), -mt.sin(theta), 0 ],
                   [ mt.sin(theta), mt.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])

import numpy as np
import math as mt
pi=22/7
degree=180
theta=pi/180*degree
print(np.round([2,1.5,0]*Rx(theta),decimals=2)[0])

