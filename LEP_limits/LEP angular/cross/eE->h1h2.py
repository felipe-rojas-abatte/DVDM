import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
y0 = np.genfromtxt('eE->h1h2.tab',dtype=float, comments='#',unpack=True)
#--------------- writing plots -----------------#
#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~H3,~X')
plt.xlabel('MH3',fontsize=16)
plt.ylabel('Cross Section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
xmin=7.000000E+01
xmax=1.000000E+02
plt.xlim(xmin,xmax)
plt.ylim(7.296479E-02,1.904072E-01)
xfirst=xmin+0.5*(xmax-xmin)/101
xlast=xmax -0.5*(xmax-xmin)/101
x0=np.linspace(xfirst,xlast,101)
plt.plot(x0, y0[0:101],alpha=0.7, label='Cross Section [pb]', linestyle='-')
plt.savefig('eE->h1h2.pdf')
plt.show()
