#!python
"""
ein cooles Feature von Klassen: magic methods

siehe auch:
http://www.rafekettler.com/magicmethods.html
"""

from numpy import where, sum as npsum, asfarray, arange, mean
from numpy.random import rand
import matplotlib.pyplot as plt

def func1(x):
    x=asfarray(x)
    c=where(x>0.8,1,0)
    n=npsum(c)
    return x+n

class Func2Carrier(object):
    
    def __init__(self,thresh):
        self.thr=thresh
        self.memory=[]
        self.n=None
    
    def __lt__(self,other):
        return self.thr<other.thr

    def __gt__(self,other):
        return self.thr>other.thr

    def __le__(self,other):
        return self.thr<=other.thr

    def __ge__(self,other):
        return self.thr>=other.thr

    def __eq__(self,other):
        return self.thr==other.thr

    def __ne__(self,other):
        return self.thr!=other.thr
    
    def __add__(self,other):
        return Func2Carrier(self.thr+other.thr)

    def call(self,x):
        x=asfarray(x)
        c=where(x>self.thr,1,0)
        self.n=npsum(c)
        self.memory.appen(self.n)
        return x+self.n
    



f2c=Func2Carrier(0.8)
f2d=Func2Carrier(0.5)

print 'is f2d < f2c ? ',f2d<f2c
print 'is f2d > f2c ? ',f2d>f2c
f2sum=f2c+f2d
print 'f2c+f2d = f2sum = ',f2sum
print 'f2sum has threshold ',f2sum.thr
