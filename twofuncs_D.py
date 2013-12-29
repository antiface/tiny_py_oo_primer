#!python
"""
das naechste coole Feature: Vererbung
"""

from numpy import where, sum as npsum, asfarray, arange, mean
from numpy.random import rand
import matplotlib.pyplot as plt

def func3(x):
    x=asfarray(x)
    return x**2

def func1(x):
    x=asfarray(x)
    c=where(x>0.8,1,0)
    n=npsum(c)
    return x+n



class Memory(object):
    
    def __init__(self):
        self.target=None
        self.m=[]
        self.callcounter=0
    
    def record_stuff(self):
        self.m.append(self.target.n)
        self.callcounter+=1
    
    def tell(self):
        print 'I have recorded {} entries'.format(self.callcounter)
        print 'they are ',self.m
        print 'the mean is: ',mean(self.m)

class Mem2(Memory):
    """Vererbung: diese Klasse erbt alle Methoden der Basisklasse"""
    def tell(self):
        """Vererbung 1: ueberschreiben von Methoden"""
        print "J'ai recu {} donnees".format(self.callcounter)
        print 'ils sont ',self.m
        print 'la moyenne: ',mean(self.m)
    
    def save_stuff(self):
        """Vererbung 2: eine neue Methode"""
        outfile=open('memory_inhalt.txt','w')
        outfile.write(str(self.m))
        outfile.close()

class Func2Carrier(object):
    
    def __init__(self,thresh,style='en'):
        self.thr=thresh
        if style =='fr':
            self.memory=Mem2()
        else:
            self.memory=Memory()
        self.memory.target=self
        self.n=None
    
    def call(self,x):
        x=asfarray(x)
        c=where(x>self.thr,1,0)
        self.n=npsum(c)
        self.memory.record_stuff()
        return x+self.n
    

f2c=Func2Carrier(0.8)
f2d=Func2Carrier(0.5,style='fr')
func2=f2c.call
func4=f2d.call

N=10
n=4
for i in range(N):
    data=rand(n,n)
    x=(arange(n**2)+rand(n**2)).reshape(n,n)
    shifted1=func1(data)
    shifted2=func2(data)
    shifted4=func4(data)

f2c.memory.tell()
print 40*'-'
f2d.memory.tell()

f2d.memory.save_stuff()

