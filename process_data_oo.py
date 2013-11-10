#!python
"""
lese und verarbeite Daten, nun objektorientiert
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
    
    def write_importand_characteristic_data(self,extended_output=False):
        """
        Man erwischt sich oft beim Schreiben solcher Ausgabefunktionen, und spaeter
        muss man dann noch eventuell Einlesefunktionen fuer viele gleiche Ausgabedateien
        schreiben. Das ist oft unnoetig, denn es gibt z.B. Pickler und Unpickler.
        """
        if extended_output==1:
            "blablabla"
        elif extended_output==2:
            "blablabla" # irgendwann wurde noch eine andere Version fuer  noetig gehalten - oje
        else:
            "blablabla" 
            # schlanke Ausgabeoption --> Ziel ist Uebersichtlichkeit wenn nicht alles gebraucht
            # wird, ABER: Nachteil --> jetzt sind die Ausgabedateien nicht mehr standardisiert
            # man muss das Einleseprogramm umschreiben, um es wieder tolerant zu machen
            # Oft ist das alle unnoetiger Mumpitz, denn mit Pickler und Unpickler gehts meist auch
            # und es ist immer das komplette Objekt gespeichert (sofern nicht grosse Dinger vor dem
            # pickling ueber Bord geworfen werden).
        raise NotImplementedError('sorry, not implemented, (aber meist besser so)')
            
    


"""
Version 1:
"""
#mda=MyDataAnalyser('data')
#mda.process_data()
## jetzt hab ich auch die Information, um Statistische Groessen in die Plots
## reinschreiben zu koennen
#minmean, maxmean = mean(mda.min),mean(mda.max)
#for i,dat in enumerate(mda.data):
#    plt.imshow(dat, cmap=cm.jet, interpolation=None, extent=[11,22,-3,2])
#    txt='plot '.format(mda.n[i])
#    txt+='\nmin {} und max {}'.format(mda.min[i],mda.max[i])
#    txt+='\navg. min {} und avg. max {}'.format(minmean,maxmean)
#    plt.suptitle(txt,x=0.5,y=0.98,ha='center',va='top',fontsize=10)
#    plt.savefig(join(mda.plotpath,'pic_oo_'+str(mda.n[i])+'.png'))
#    plt.close()  # wichtig, sonst wird in den selben Plot immer mehr reingepackt
#
## Man haette natuerlich auch in process_data.py zweimal durch die Datenbank
## gehen koennen, einmal fuer die Statistik, und das zweite Mal, um die
## Plots machen zu koennen und die statistische Info mit reinschreiben zu koennen.
## Ausserdem passiert das hier ja auch nicht anders, eine Schleife in mda.read_data(),
## eine in mda.process_data(), eine dritte zum Plotten --> Rechenzeit.
## ABER: oft wird ein prozedurales Auswerteskript lang und kompliziert, und je laenger
## und komplizierter es wird, desto groesser wird die Hemmschwelle, daran auch nur kleine
## Dinge zu aendern --> Hemmung der Kreativitaet, man probiert nichts mehr aus
##
## bei der objektorientierten Version wird der Code nicht kuerzer. In der
## Klassendefinition steht oft fast derselbe Code wie vorher im prozeduralen Prototyp.
## ABER: die prozedurale Version wird oft nicht gescheit kommentiert, rein wegen Faulheit.
## Faellt nicht auf, dass die Namen der Methoden oben (read_data, process_data, plot_data)
## genau das ist, was als Abschnittsueberschriften (Mindestkommentarmenge sozusagen)
## in der Prozeduralen Version stehen sollte?
## 
## Wenn man in einem langen prozeduralen Auswerteskript Abschnitte an- oder ausschaltet,
## dann bekommt man probleme wenn man sich nicht mehr daran erinnert, wie sie voneinander
## abhangen. In der obigen Version muss man solche Probleme nicht haben, man kann ja
## uebungsweise mal in die Plotfunktion einbauen, der nachprueft ob process_data schon
## gelaufen ist, so dass es im Notfall automatisch nachgeholt wird.






"""
Version 2:
    ich habe bemerkt, dass ich die Plots haeufig benutze, also rein damit in
    die Klassendefinition!
"""
## man bemerke die Uebersichtlichkeit der folgenden drei Befehle,
## sie sind knapp, aber doch geht hervor was alles gemacht wird

mda=MyDataAnalyser('data')
mda.process_data()
mda.plot_data()

print 'standard deviations: ',std(mda.min),std(mda.max) # Warum nicht rein damit in die Klassendefinition?



"""
noch was:
    Instanz speichern, alles, ohne Arbeit mit dem Schreiben von Ausgaberoutinen
"""
output=open('einmachglas.txt','w')
einmachglas=Pickler(output)
einmachglas.dump(mda)
output.close()

# aber: Datei wird gross, weil die ganzen Datensaetze mit drin sind
# Uebung: Klassendefinition umschreiben, dass eine Instanz nicht einen
# riesigen Speicher belegt
# Grundsatzfrage stellt sich immer: Was alles als Instanzattribute mitschleppen?

