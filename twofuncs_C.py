#!python
"""
Spielerei auf dem naechsten Level: ein Objekt hat in sich andere Objekte
eingebaut (ist in Python eigentlich immer der Fall, denn in Python ist alles
ein Objekt)

Was wird gemacht? Memory war vorher lediglich eine Liste. Nun ist es ein
eigenstaendigs Ding, das selbst agieren kann und an der richtigen Stelle zur
Aktion aufgerufen wird. Es sucht sich aus seinem target alles noetige heraus,
um seine Routine record_stuff() abarbeiten zu koennen.

Entscheidender Qualitaetssprung fuer den Programmierer oder das Programmier-
team: Funktionalitaet von Memory kann erweitert werden, ganz ohne Func2Carrier
zu veraendern. Memory kann spaeter dahingehend modifiziert werden, sich viel
mehr Zustandsinfos von Func2Carrier-Instanzen zu holen, denn sobald der
Kommunikationskanal existiert (sobald Memory sein target beim Namen kennt), hat
Memory Zugriff auf schlichtweg alle Daten der zugeordneten Func2Carrier-
Instanz.

Deshalb ist das Ganze auch ein hinweis darauf, was sich hinter dem Begriff
"namespaces" verbirgt. Wer noch von Wuenschen nach globalen Variablen geplagt
wird, sollte sich fragen, ob es mit Instanzen, die voneinander wissen, nicht
viel geordneter und mit weniger Fehlerquellen abgehen kann.
"""

from numpy import where, sum as npsum, asfarray, arange, mean
from numpy.random import rand
import matplotlib.pyplot as plt

def func1(x):
    x=asfarray(x)
    c=where(x>0.8,1,0)
    n=npsum(c)
    return x+n

class Memory(object):
    
    def __init__(self):
        self.target=None   # die Instanz weiss an der Stelle nichts von ihrem Schoepfer
        self.m=[]
        self.callcounter=0
    
    def record_stuff(self):
        self.m.append(self.target.n)
        self.callcounter+=1
    
class Func2Carrier(object):
    
    def __init__(self,thresh):
        self.thr=thresh
        self.memory=Memory()  # ein Objekt wird als Attribut kreiert
        self.memory.target=self # Kommunikationskanal besteht jetzt in beide Richtungen
        self.n=None
    
    def call(self,x):
        x=asfarray(x)
        c=where(x>self.thr,1,0)
        self.n=npsum(c)
        self.memory.record_stuff()
        return x+self.n


f2c=Func2Carrier(0.8)
func2=f2c.call

N=10
n=4
for i in range(N):
    data=rand(n,n)
    x=(arange(n**2)+rand(n**2)).reshape(n,n)
    shifted1=func1(data)
    shifted2=func2(data)

print 'die Zustandsvariable hatte folgende Werte:'
print f2c.memory.m
