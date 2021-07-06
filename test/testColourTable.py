# # Import packages
import matplotlib.pyplot as plt

# Use our custom style
plt.style.use('shendrukGroupStyle')
# Use our custom colours
import shendrukGroupFormat as ed

# print plt.style.available

# import matplotlib as mpl
# print mpl.get_configdir()

print(ed.saphire)
print(ed.clist().cyclic)
print(ed.clist().cyclic["saphire"])

ed.plot_colortable(ed.clist().cyclic, "Cyclic" )
plt.savefig( 'tableCyclic.pdf' )
ed.plot_colortable(ed.clist().noncyclic, "Noncyclic" )
plt.savefig( 'tableNoncyclic.pdf' )
ed.plot_colortable(ed.clist().official, "Official" )
plt.savefig( 'tableOfficial.pdf' )
ed.plot_colortable(ed.clist().modified, "Modified" )
plt.savefig( 'tableModified.pdf' )
ed.plot_colortable(ed.clist().all, "All" )
plt.savefig( 'tableAll.pdf' )
plt.show()
