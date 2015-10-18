import matplotlib, numpy
from math import *
from numpy import linspace
from matplotlib.figure import AxesStack 
from matplotlib.figure import Figure as figure
import matplotlib.pyplot as plt


def joints_to_hand(a1,a2,l1,l2):
  Ex = l1 * cos(a1)
  Ey = l1 * sin(a1)
  Hx = Ex + (l2 * cos(a1+a2))
  Hy = Ey + (l2 * sin(a1+a2))
  return Ex,Ey,Hx,Hy

# limb geometry
l1 = 0.34 # metres
l2 = 0.46 # metres

# decide on a range of joint angles
n1steps = 10
n2steps = 10


a1range = linspace(0*pi/180, 120*pi/180, n1steps) # shoulder
a2range = linspace(0*pi/180, 120*pi/180, n2steps)   # elbow

# sample all combinations and plot joint and hand coordinates
f=figure(figsize=(8,12))
print('This ia rhw initial type of a',type(f))
for i in range(n1steps):
  for j in range(n2steps):
    plt.subplot(2,1,1)
    plt.plot(a1range[i]*180/pi,a2range[j]*180/pi,'r+')
    ex,ey,hx,hy = joints_to_hand(a1range[i], a2range[j], l1, l2)
    plt.subplot(2,1,2)
    plt.plot(hx, hy, 'r+')
plt.subplot(2,1,1)
plt.xlabel('Shoulder Angle (deg)')
plt.ylabel('Elbow Angle (deg)')
plt.title('Joint Space')
plt.subplot(2,1,2)
plt.xlabel('Hand Position X (m)')
plt.ylabel('Hand Position Y (m)')
plt.title('Hand Space')
a1 = a1range[n1steps/2]
a2 = a2range[n2steps/2]
ex,ey,hx,hy = joints_to_hand(a1,a2,l1,l2)
plt.subplot(2,1,1)
plt.plot(a1*180/pi,a2*180/pi,'bo',markersize=5)
plt.axis('equal')
#fm = fg.AxesStack
fg = AxesStack()
print('####This is the value of fg.get', fg.get(f))
xl = fg.get(fg.get(f),'xlim')
yl = fm.get(fm.get(f),'ylim')
plt.plot((xl[0],xl[1]),(a2*180/pi,a2*180/pi),'b-')
plt.plot((a1*180/pi,a1*180/pi),(yl[0],yl[1]),'b-')
plt.subplot(2,1,2)
plt.plot((0,ex,hx),(0,ey,hy),'b-')
plt.plot(hx,hy,'bo',markersize=5)
plt.axis('equal')
xl = fm.get(fm.get(f,'axes')[1],'xlim')
yl = fm.get(fm.get(f,'axes')[1],'ylim')
plt.plot((xl[0],xl[1]),(hy,hy),'b-')
plt.plot((hx,hx),(yl[0],yl[1]),'b-')
