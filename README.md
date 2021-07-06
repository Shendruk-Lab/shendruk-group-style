# Shendruk Lab Group Style
Matplotlib style file that keeps the group figures looking consistent. Decent documentation is available [here](doc/shendrukGroupStyleGuide.pdf) (you may need to download this file).

## Installation Instructions
Installation is non-trivial to get matplotlib to recognise the groupstyle. 
Do the following:
1. Open Python in terminal
2. Call `import matplotlib as mpl` then `print(mpl.get_configdir())` (for Python 3, change as necessary for Py2). Note down this directory
3. Navigate to this directory and look for a subdirectory there called "stylelib". If it doesn't exist then create it. 
4. From this repo's src directory, copy shedrunkGroupStyle.mplstyle to the above location. For me this is in `/home/tk/.config/matplotlib/stylelib/shendrukGroupStyle.mplstyle`.
5. When you use Matplotlib for plotting, copy shendrukGroupFormat.py from this repo's src directory to your project. Import it into every relevent file as:
```
#handle graph formatting and style
plt.style.use('shendrukGroupStyle')
import shendrukGroupFormat_py3 as ed
MYLW=1.0 #line width
```

## Repo Format
In the directory doc/ is a PDF guide (shendrukGroupStyleGuide.pdf). 
It requires substantial improvement by group members to be more useful. 
The directory doc/src/ includes images and LaTeX to create the guide.

In test/ are python scripts to make various types of figures. They should be good test cases to see if things are generally working.

In src/ are the two source codes. The file src/shendrukGroupStyle.mplstyle is the matplotlib style file. 
The other file src/shendrukGroupFormat.py. 
This defines colour names, colourmaps, filled errorbars, etc. 
See the test codes and the guide for how to include these in your python scripts.
