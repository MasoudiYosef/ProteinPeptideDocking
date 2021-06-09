from math import *
import numpy as np
import sys

def rotation(line,point,theta):
    theta=theta*3.14/180
    x,y,z=point[0],point[1],point[2]
    a,b,c=line[0],line[1],line[2]
    d,e,f=line[3],line[4],line[5]
    u,v,w=d-a,e-b,f-c
    L=pow(u,2)+pow(v,2)+pow(w,2)
    first=(a*(pow(v,2)+pow(w,2))-u*(b*v+c*w-u*x-v*y-w*z))*(1-cos(theta))
    second=L*x*cos(theta)
    third=sqrt(L)*(-c*v+b*w-w*y+v*z)*sin(theta)
    a1=first+second+third
    first=(b*(pow(u,2)+pow(w,2))-v*(a*u+c*w-u*x-v*y-w*z))*(1-cos(theta))
    second=L*y*cos(theta)
    third=sqrt(L)*(c*u-a*w-w*x-u*z)*sin(theta)
    a2=first+second+third
    first=(c*(pow(u,2)+pow(v,2))-w*(a*u+b*v-u*x-v*y-w*z))*(1-cos(theta))
    second=L*z*cos(theta)
    third=sqrt(L)*(-b*u+a*v-v*x+u*y)*sin(theta)
    a3=first+second+third
    return [a1/L,a2/L,a3/L]

def Rx(theta):
  theta=theta*3.14/180
  return np.matrix([[ 1, 0           , 0           ],
                   [ 0, cos(theta),-sin(theta)],
                   [ 0, sin(theta),cos(theta)]])
  
def Ry(theta):
  theta=theta*3.14/180
  return np.matrix([[cos(theta), 0,sin(theta)],
                   [ 0           , 1, 0           ],
                   [sin(theta), 0,cos(theta)]])
  
def Rz(theta):
  theta=theta*3.14/180
  return np.matrix([[cos(theta),sin(theta), 0 ],
                   [sin(theta),cos(theta), 0 ],
                   [ 0           , 0            , 1 ]])

def get_teta(p1,p2,p3):
    x1,y1,z1=p1[0],p1[1],p1[2]
    x2,y2,z2=p2[0],p2[1],p2[2]
    x3,y3,z3=p3[0],p3[1],p3[2]
    a=sqrt(pow(x2-x1,2)+pow(y2-y1,2)+pow(z2-z1,2))
    b=sqrt(pow(x3-x1,2)+pow(y3-y1,2)+pow(z3-z1,2))
    c=sqrt(pow(x2-x3,2)+pow(y2-y3,2)+pow(z2-z3,2))
    if (a==0)|(b==0):
        t=0
    else:
        t=(a*a+b*b-c*c)/(2*a*b)
    return np.arccos(t)*180/3.14
