import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
#scalar
y0 = np.genfromtxt('eE->h1h2.tab',dtype=float, comments='#',unpack=True)
#vector
y1 = np.genfromtxt('eE->v1v2.tab',dtype=float, comments='#',unpack=True)
#--------------- writing plots -----------------#
#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~x1,~x2')
plt.xlabel('Mx2',fontsize=16)
plt.ylabel('Cross Section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('log')
xmin=7.000000E+01
xmax=1.000000E+02
plt.xlim(xmin,xmax)
plt.ylim(7.296479E-02,15)
xfirst=xmin+0.5*(xmax-xmin)/101
xlast=xmax -0.5*(xmax-xmin)/101
x0=np.linspace(xfirst,xlast,101)

scalar, = plt.plot(x0, y0[0:101],alpha=0.7, label='scalar', linestyle='--')
vector, = plt.plot(x0, y1[0:101],alpha=0.7, label='vector', linestyle='-')

legend1 = plt.legend(handles=[scalar,vector], loc="upper right", title="comparasion" ,ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('eE->x1x2.pdf')
plt.show()
