#!python
"""
Auslagern der Klassendefinition in eigene Datei macht die eigentlichen
Arbeitsskripte viel uebersichtlicher. (Allerdings muss man natuerlich von da
ab immer in die andere Datei hinueberlinsen, um beim Programmieren nachzu-
schauen, wie die Definition einer bestimmten Routine eben nochmal ausgesehen
hat.)

mit
http://docs.python.org/2/library/distutils.html?highlight=distutil#distutils
kann man seine eigenen bibliotheken als richtige Module installieren.

Aber oft reicht der einfache Weg: alles was im selben Ordner liegt, kann
einfach beim Dateinamen packen und importieren.
"""

from os import getcwd, mkdir, listdir
from os.path import join, dirname, isdir
from numpy import amin, amax, loadtxt, zeros, mean, std
from pylab import plt, cm
from cPickle import Pickler


class MyDataAnalyser(object):

    def __init__(self,targetfolder):
        namelist=listdir(getcwd())
        if targetfolder in namelist:
            self.datapath=join(targetfolder)
            if not isdir(self.datapath):
                raise ValueError("I can't find any subfolder {} in my working directory".format(targetfolder))
        self.plotpath=join(dirname(targetfolder),'plots')
        try:
            mkdir(self.plotpath)
            print "plot folder didn't exist yet, I just created it"
        except:
            print 'plot folder seems to exist, I will write in it'
        self.N=0
        self.n=[]
        self.data=[]
        self.min=None
        self.max=None
        self.avg_min=None
        self.avg_max=None
        self.read_data()
    
    def read_data(self):
        fli=listdir(self.datapath)
        if len(fli)==0:
            print 'warning: no datasets present'
        for i,dataset in enumerate(fli):
            fname,ext=dataset.split('.')
            namensbruchstuecke=fname.split('_')
            self.n.append(int(float(namensbruchstuecke[2])))
            self.data.append(loadtxt(join(self.datapath,dataset)))
        self.N=len(fli)
    
    def process_data(self):
        self.min=zeros(self.N)
        self.max=zeros(self.N)
        for i,dat in enumerate(self.data):
            self.min[i]=amin(dat)
            self.max[i]=amax(dat)
    
    def plot_data(self):
        for i,dat in enumerate(self.data):
            plt.imshow(dat, cmap=cm.jet, interpolation=None, extent=[11,22,-3,2])
            txt='plot '.format(self.n[i])
            txt+='\nmin {0:.2f} und max {1:.2f}'.format(self.min[i],self.max[i])
            txt+='\navg. min {0:.2f} und avg. max {1:.2f}'.format(mean(self.min),mean(self.max))
            plt.suptitle(txt,x=0.5,y=0.98,ha='center',va='top',fontsize=10)
            plt.savefig(join(self.plotpath,'pic_oo_'+str(self.n[i])+'.png'))
            plt.close()  # wichtig, sonst wird in den selben Plot immer mehr reingepackt