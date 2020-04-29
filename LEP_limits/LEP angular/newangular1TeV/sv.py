import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
ys40 = np.genfromtxt('s40.tab',dtype=float, comments='#',unpack=True)
cs40 = 0.013 #(pb)#
ys100 = np.genfromtxt('s100.tab',dtype=float, comments='#',unpack=True)
cs100 = 0.012 #(pb)#
ys400 = np.genfromtxt('s400.tab',dtype=float, comments='#',unpack=True)
cs400 =  0.0028 #(pb)#

yv40 = np.genfromtxt('v40.tab',dtype=float, comments='#',unpack=True)
cv40 = 1269.13 #(pb)#
yv100 = np.genfromtxt('v100.tab',dtype=float, comments='#',unpack=True)
cv100 = 37.001 #(pb)#
yv400 = np.genfromtxt('v400.tab',dtype=float, comments='#',unpack=True)
cv400 = 0.125 #(pb)#

#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~x1,~x2 at 1 TeV')
plt.xlabel('cos(p1,p3)',fontsize=16)
plt.ylabel('Normalized Diff. cross section [pb]',fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
xmin=-9.990000E-01
xmax=9.990000E-01
plt.xlim(xmin,xmax)
plt.ylim(2.441050E-03,1.2)
xfirst=xmin+0.5*(xmax-xmin)/100
xlast=xmax -0.5*(xmax-xmin)/100
x0=np.linspace(xfirst,xlast,100)

ps40, = plt.plot(x0, ys40/cs40, alpha=0.7, label='s 40', linestyle='--', color= 'green')
ps100, = plt.plot(x0, ys100/cs100, alpha=0.7, label='s 100', linestyle='--', color= 'red')
ps400, = plt.plot(x0, ys400/cs400,alpha=0.7, label='s 400', linestyle='--', color= 'blue')

pv40, = plt.plot(x0, yv40/cv40, alpha=0.7, label='v 40', linestyle='-', color= 'green')
pv100, = plt.plot(x0, yv100/cv100, alpha=0.7, label='v 100', linestyle='-', color= 'red')
pv400, = plt.plot(x0, yv400/cv400,alpha=0.7, label='v 400', linestyle='-', color= 'blue')

legend = plt.legend(handles=[ps40, ps100, ps400, pv40 , pv100, pv400], loc="upper right", title="comparasion" ,ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('sv.pdf')
plt.show()
