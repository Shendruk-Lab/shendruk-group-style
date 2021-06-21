# Import packages
import matplotlib.pyplot as plt
import numpy as np

# Use our custom style
plt.style.use('shendrukGroupStyle')
import shendrukGroupFormat as ed

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = []
for i in range(38):
    s.append( i + np.sin(2 * (np.pi+i*np.pi/19.) * t) )

# Plots
fig, ax = plt.subplots()
for i in range(2):
    ax.plot(t, s[i], label="%s"%i)
ax.set(xlabel=r'time, $\tau$', ylabel=r'density, $\rho$',title='Shendruk Group Style')
ax.legend(loc='upper right')
plt.savefig( 'linestyle.pdf' )

fig, ax = plt.subplots()
for i in range(10):
    ax.plot(t, s[i], label="%s"%i)
ax.set(xlabel=r'time, $\tau$', ylabel=r'density, $\rho$')
ax.set_title('Many Curves', fontdict={'fontsize': 50})
ax.legend(loc='best',prop={'size': ed.fontsizeSmall})
plt.savefig( 'manylines.pdf' )
plt.show()
