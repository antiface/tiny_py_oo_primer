#!python
"""
schreibe Daten
"""

from os import getcwd, mkdir
from os.path import join
from pylab import *

def func3(x,y):
    return (1- x/2 + x**5 + y**3)*exp(-x**2-y**2)

dx, dy = 0.05, 0.05
x = arange(-3.0, 3.0, dx)
y = arange(-3.0, 3.0, dy)
X,Y = meshgrid(x, y)

loc=getcwd()
datapath=join(loc,'data')
try:
    mkdir(datapath)
    print "data folder didn't exist yet, I just created it"
except:
    print 'data folder seems to exist, I will write in it'

N=10
for i in range(N):
    A1,A2=rand(2)
    w1,w2=4*rand(2)
    Z = func3(X, Y) + A1*sin(2*pi*w1*X) + A2*sin(2*pi*w2*Y)
    fname='data_case_{}.txt'.format(str(i).zfill(2))
    savetxt(join(datapath,fname),Z)

