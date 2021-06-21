import os
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

lagtime=[]
msd=[]
t=0
p='/home/lunet/matns/Documents/research/results/polymerNematicsExtended/'
files=[p+'N15_KN20.0_KB0.0_S0.1_HI1_U5_I0/20200705-148348/MSD_dirPerpendicular.dat', p+'N15_KN10.0_KB0.0_S0.1_HI1_U5_I0/20200705-148318/MSD_dirPerpendicular.dat', p+'N15_KN2.0_KB0.0_S0.1_HI1_U5_I0/20200705-148205/MSD_dirPerpendicular.dat', p+'N15_KN0.1_KB0.0_S0.1_HI1_U5_I0/20200705-147970/MSD_dirPerpendicular.dat']
for file in files:
    lagtime.append([])
    msd.append([])
    if not os.path.isfile(file):
        print("File not found: %s"%file)
        exit()
    file=open(file,"r")
    while file:
        buff=file.readline()
        if( not buff ):
            break
        buff=buff.split()
        lagtime[-1].append(float(buff[0]))
        msd[-1].append(float(buff[1]))
        t+=1
    file.close()
    lagtime[-1]=array(lagtime[-1])
    msd[-1]=array(msd[-1])

fig=plt.figure(1)
ax=fig.add_subplot(1, 1, 1)
for i in range(len(files)):
    plt.plot(lagtime[i],msd[i],'-')
plt.xlabel("Time")
plt.ylabel("MSD")
ax.set_xscale('log')
ax.set_yscale('log')
# ax.grid(which='both')
plt.savefig('loglog.pdf')
plt.show()
