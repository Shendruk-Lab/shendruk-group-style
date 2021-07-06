import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

np.random.seed(0)
mu = 10
sigma = 15
x = mu + sigma * np.random.randn(1000)
fig, ax = plt.subplots()
# n, bins, patches = ax.hist(x, 50, normed=1)
n, bins, patches = ax.hist(x, 50, density=True)
# y = mlab.normpdf(bins, mu, sigma)
y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '-o')
ax.set_ylabel('Probability density')
ax.set_title(r'$\mu=100$, $\sigma=15$')
plt.savefig( 'hist.pdf' )
plt.show()
