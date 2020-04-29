import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
y0 = np.genfromtxt('scalan.tab',dtype=float, comments='#',unpack=True)
css = 0.14 #(pb)#
y1 = np.genfromtxt('vecan.tab',dtype=float, comments='#',unpack=True)
csv = 7.8 #(pb)#
#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~x1,~x2')
plt.xlabel('cos(p1,p3)',fontsize=16)
plt.ylabel('Diff. cross section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
xmin=-9.990000E-01
xmax=9.990000E-01
plt.xlim(xmin,xmax)
plt.ylim(2.441050E-03,1.2)
xfirst=xmin+0.5*(xmax-xmin)/100
xlast=xmax -0.5*(xmax-xmin)/100
x0=np.linspace(xfirst,xlast,100)

scalar, = plt.plot(x0, y0[0:100]/css,alpha=0.7, label='scalars', linestyle='--')
vector, = plt.plot(x0, y1[0:100]/csv,alpha=0.7, label='vectors', linestyle='-')

legend = plt.legend(handles=[scalar,vector], loc="upper right", title="comparasion" ,ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('scalan.pdf')
plt.show()
