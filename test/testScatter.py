import numpy as np
import matplotlib.pyplot as plt
# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

N = 10
for i in ed.clist().official:
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.scatter(x, y, s=area, c=ed.clist().official[i], alpha=0.75, label=i)
# plt.xlim(0,1.4)
# plt.ylim(0,1)
# plt.legend(loc='right',prop={'size': ed.fontsizeTiny})
plt.savefig( 'scatter.pdf' )
plt.show()
