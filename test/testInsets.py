import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

# create some data to use for the plot
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05)               # impulse response
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)]*dt  # colored noise

# the main axes is subplot(111) by default
plt.plot(t, s)
plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')

# this is an inset axes over the main axes
inset1 = plt.axes([.7, .6, .2, .2])
inset1.patch.set_facecolor(ed.silver)
# n, bins, patches = plt.hist(s, 400, normed=1,edgecolor=ed.saphire)
n, bins, patches = plt.hist(s, 400, density=True, edgecolor=ed.saphire)
plt.title('Probability',fontsize=ed.fontsize)
plt.xticks([])
plt.yticks([])

# this is another inset axes over the main axes
inset2 = plt.axes([0.25, 0.6, .2, .2])
inset2.patch.set_facecolor(ed.silver)
plt.plot(t[:len(r)], r)
plt.title('Impulse',fontsize=ed.fontsize)
plt.xlim(0, 0.2)
inset2.tick_params(axis="x",labelsize=ed.fontsizeTiny)
inset2.tick_params(axis="y",labelsize=ed.fontsizeTiny)
plt.savefig("insets.pdf")
plt.show()
