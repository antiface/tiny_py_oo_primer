#!python
"""
ein Unterschied zwischen Funktion und Objekt: Gedaechtnis

Fuer dieses Beispiel benutzen wir eine Funktion, die jedesmal in einem anderen
Zustand arbeitet, sie addiert jedesmal eine andere Zahl auf ihre Eingangswerte.
Hier lauft alles immerhin noch deterministisch ab und man kann die Zustaende
ableiten, wenn man sich die Daten auf dem Plot genau anschaut. Aber es muss
ja nicht immer so deterministisch sein und die Ableitung nicht immer so muehelos.
"""

from numpy import where, sum as npsum, asfarray, arange
from numpy.random import rand
import matplotlib.pyplot as plt

def func1(x):
    x=asfarray(x)
    c=where(x>0.8,1,0)
    n=npsum(c)
    return x+n


class Func2Carrier(object):

    def __init__(self):
        self.memory=[]
        self.n=None

    def call(self,x):
        x=asfarray(x)
        c=where(x>0.8,1,0)
        self.memory.append(npsum(c))
        return x+self.memory[-1]
    



f2c=Func2Carrier()
func2=f2c.call

N=10
n=4
for i in range(N):
    data=rand(n,n)
    x=(arange(n**2)+rand(n**2)).reshape(n,n)
    shifted1=func1(data)
    shifted2=func2(data)
    plt.plot(x.flatten(),data.flatten(),'kx')
    plt.plot(x,data,'kx')
    plt.plot(x,shifted1,'gx',markersize=12)
    plt.plot(x,shifted2,'yd')

print 'die Zustandsvariable hatte folgende Werte:'
print f2c.memory

plt.xlabel(r'eine Variable $x$')
plt.ylabel(r'eine griechische Variable $\gamma$')
plt.suptitle(r'eine Formel, z. B. $\gamma=\sum_{i=0}^N \, x_i$',x=0.5,y=0.992,ha='center',va='top')

plt.show()

