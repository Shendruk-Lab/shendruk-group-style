import numpy as np
import matplotlib.pyplot as plt
# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
y2 = 1.0-np.exp(-x)
y2err=0.2*y

fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4, marker='o')
ax.errorbar(x, y2, yerr=y2err)
ax.errorbar(x, y2-y, yerr=0.4, marker='s')
plt.savefig( 'errorbar.pdf' )

fig, ax = plt.subplots()
ed.errorbar_fill(x,y,yerr=0.4,marker='o')
ed.errorbar_fill(x,y2,yerr=y2err)
ed.errorbar_fill(x,y2-y,yerr=0.4,marker='s')
plt.savefig( 'errorfill.pdf' )
plt.show()
