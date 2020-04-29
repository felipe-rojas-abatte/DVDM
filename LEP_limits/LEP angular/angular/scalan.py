import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
y0 = np.genfromtxt('scalan.tab',dtype=float, comments='#',unpack=True)
#--------------- writing plots -----------------#
#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~H3,~X')
plt.xlabel('cos(p1,p3)',fontsize=16)
plt.ylabel('Diff. cross section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
xmin=-9.990000E-01
xmax=9.990000E-01
plt.xlim(xmin,xmax)
plt.ylim(2.441050E-03,1.138447E-01)
xfirst=xmin+0.5*(xmax-xmin)/100
xlast=xmax -0.5*(xmax-xmin)/100
x0=np.linspace(xfirst,xlast,100)
plt.plot(x0, y0[0:100],alpha=0.7, label='Diff. cross section [pb]', linestyle='-')
plt.savefig('scalan.pdf')
plt.show()
