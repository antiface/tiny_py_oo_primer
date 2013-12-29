#!python
"""
lese und verarbeite Daten
"""

from os import getcwd, mkdir, listdir
from os.path import join
from pylab import *


loc=getcwd()
datapath=join(loc,'data')
plotpath=join(loc,'plots')
try:
    mkdir(plotpath)
    print "plot folder didn't exist yet, I just created it"
except:
    print 'plot folder seems to exist, I will write in it'


fli=listdir(datapath)

for dataset in fli:
    fname,ext=dataset.split('.')
    namensbruchstuecke=fname.split('_')
    n=int(float(namensbruchstuecke[2]))
    
    data=loadtxt(join(datapath,dataset))
    
    print 'case {}: min = {}   max = {}'.format(n,amin(data),amax(data))
    plt.imshow(data, cmap=cm.jet, interpolation=None, extent=[11,14,-3,2])
    plt.savefig(join(plotpath,'pic_'+str(n)+'.png'))
    plt.close()  # wichtig, sonst wird in den selben Plot immer mehr reingepackt

