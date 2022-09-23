import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
y0 = np.genfromtxt('eE->v1v2.tab',dtype=float, comments='#',unpack=True)
#--------------- writing plots -----------------#
#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e1,E1 ->~v1,~v2')
plt.xlabel('Mv2',fontsize=16)
plt.ylabel('Cross Section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
xmin=7.000000E+01
xmax=1.000000E+02
plt.xlim(xmin,xmax)
plt.ylim(3.079630E+00,1.168243E+01)
xfirst=xmin+0.5*(xmax-xmin)/101
xlast=xmax -0.5*(xmax-xmin)/101
x0=np.linspace(xfirst,xlast,101)
plt.plot(x0, y0[0:101],alpha=0.7, label='Cross Section [pb]', linestyle='-')
plt.savefig('eE->v1v2.pdf')
plt.show()
