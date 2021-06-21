# Import packages
from pylab import *
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D

# Use our custom style
plt.style.use('shendrukGroupStyle')
import shendrukGroupFormat as ed

# For looking at colormaps
def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]
    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)
def view_colormap(cmap,title):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))
    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
    fig.suptitle(title)
def compare_colormaps(cmap1,subtitle1,cmap2,subtitle2,title):
    """Plot a colormap with its grayscale equivalent"""
    cmap1 = plt.cm.get_cmap(cmap1)
    colors1 = cmap1(np.arange(cmap1.N))
    cmap1 = grayscale_cmap(cmap1)
    grayscale1 = cmap1(np.arange(cmap1.N))
    cmap2 = plt.cm.get_cmap(cmap2)
    colors2 = cmap2(np.arange(cmap2.N))
    cmap2 = grayscale_cmap(cmap2)
    grayscale2 = cmap2(np.arange(cmap2.N))
    fig, ax = plt.subplots(2, 2, figsize=(12, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0][0].set_title(subtitle1,fontsize=20)
    ax[0][0].imshow([colors1], extent=[0, 10, 0, 1])
    ax[1][0].imshow([grayscale1], extent=[0, 10, 0, 1])
    ax[0][1].set_title(subtitle2,fontsize=20)
    ax[0][1].imshow([colors2], extent=[0, 10, 0, 1])
    ax[1][1].imshow([grayscale2], extent=[0, 10, 0, 1])
    fig.suptitle(title,fontsize=28)

edinburghTitle="Edinburgh"
matplotlibTitle="Matplotlib"
# name="plasma"
# myMap=ed.plasma
# theirMap=cm.plasma
# name="inferno"
# myMap=ed.inferno
# theirMap=cm.inferno
# name="seismic"
# myMap=ed.seismic
# theirMap=cm.seismic
# name="bombpops"
# myMap=ed.bombpops
# theirMap=cm.coolwarm
# name="hot"
# myMap=ed.hot
# theirMap=cm.hot
# name="deepsea"
# myMap=ed.deepsea
# theirMap=cm.winter
# name="viridis"
# myMap=ed.viridis
# theirMap=cm.viridis
# name="rain"
# myMap=ed.rain_r
# theirMap=cm.Blues
# name="cherry"
# myMap=ed.cherry_r
# theirMap=cm.Reds
name="spring"
myMap=ed.spring_r
theirMap=cm.spring
# name="cool"
# myMap=ed.cool
# theirMap=cm.cool
# name="xmas"
# myMap=ed.xmas
# theirMap=cm.RdYlGn
# name="autumn"
# myMap=ed.autumn
# theirMap=cm.autumn

# view_colormap(myMap,'Mine')
# savefig( 'myMap.pdf' )
# view_colormap(theirMap,'Theirs')
# savefig( 'theirMap.pdf' )

# compare_colormaps(myMap,edinburghTitle,theirMap,matplotlibTitle,name)
# savefig( '%sBars.pdf'%name )
# show()

fig, ax = plt.subplots(3, 2, figsize=(18,18))

# make up data.
np.random.seed(0)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x*np.exp(-x**2 - y**2)
xi = np.linspace(-2.1, 2.1, 100)
yi = np.linspace(-2.1, 2.1, 200)
zi = griddata(x, y, z, xi, yi, interp='linear')
lobes = ax[0][0].contourf(xi, yi, zi, 25,vmax=abs(zi).max(), vmin=-abs(zi).max(),cmap= myMap)
fig.colorbar(lobes, ax=ax[0][0])
ax[0][0].set_xlim([-2, 2])
ax[0][0].set_ylim([-2, 2])
ax[0][0].grid(False)

grad = ax[0][1].imshow(np.arange(100).reshape((10, 10)),cmap=myMap)
fig.colorbar(grad, ax=ax[0][1])
ax[0][1].grid(False)

ax[1][0] = plt.subplot(323, projection='3d')
# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.25, 300)
p = np.linspace(0, 2*np.pi, 300)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
X, Y = R*np.cos(P), R*np.sin(P)
ax[1][0].plot_surface(X, Y, Z, cmap=myMap, linewidth=0)
ax[1][0].set_zlim(0, 1)
# ax[1][0].set_xlabel(r'$\phi_\mathrm{real}$')
# ax[1][0].set_ylabel(r'$\phi_\mathrm{im}$')
# ax[1][0].set_zlabel(r'$V(\phi)$')

speckle=ax[1][1].imshow(np.random.random((100, 100)), cmap=myMap)
fig.colorbar(speckle, ax=ax[1][1])
ax[1][1].grid(False)

n = 100000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()
hb = ax[2][0].hexbin(x, y, gridsize=50, bins='log', cmap=myMap)
ax[2][0].set(xlim=(xmin, xmax), ylim=(ymin, ymax))
cb = fig.colorbar(hb, ax=ax[2][0])
cb.set_label('log10(N)')

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
strm = ax[2][1].streamplot(X, Y, U, V, color=U, linewidth=2, cmap=myMap)
fig.colorbar(strm.lines, ax=ax[2][1])

fig.suptitle(name, fontsize=ed.fontsize_axes)
savefig( '%sExamples.pdf'%name )
plt.show()
