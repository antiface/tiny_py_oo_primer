#!python
"""
mda auftauen
"""
from numpy import shape
from cPickle import Unpickler
from mda_classdef import MyDataAnalyser

infile=open('einmachglas.txt','r')
einmachglas=Unpickler(infile)
mda_reloaded=einmachglas.load()
infile.close()


print mda_reloaded
print 'number of data sets: ',mda_reloaded.N
print 'shape of first data set: ',shape(mda_reloaded.data[0])
print 40*'-'
print 'Minima: ',mda_reloaded.min
print 'Maxima: ',mda_reloaded.max
print 40*'-'
print 'a segment of a data set:'
print mda_reloaded.data[0][:5,:4]