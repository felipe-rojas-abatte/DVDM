import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate
#--------------- data input -----------------------#
ys100 = np.genfromtxt('s100.tab',dtype=float, comments='#',unpack=True)
cs100 = 7.6E-05 #(pb)#
ys500 = np.genfromtxt('s500.tab',dtype=float, comments='#',unpack=True)
cs500 =  7.5E-05 #(pb)#
ys1000 = np.genfromtxt('s1000.tab',dtype=float, comments='#',unpack=True)
cs1000 = 7.3E-05 #(pb)#

yv100 = np.genfromtxt('v100.tab',dtype=float, comments='#',unpack=True)
cv100 = 5443.29 #(pb)#
yv500 = np.genfromtxt('v500.tab',dtype=float, comments='#',unpack=True)
cv500 = 9.022 #(pb)#
yv1000 = np.genfromtxt('v1000.tab',dtype=float, comments='#',unpack=True)
cv1000 = 0.5975 #(pb)#

#fig, ax = plt.subplots(figsize=(6,3.8))
#plt.subplots_adjust(bottom=0.20,right=0.75,left=0.15)
plt.title('e,E ->~x1,~x2 at 13 TeV')
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

ps100, = plt.plot(x0, ys100/cs100, alpha=0.7, label='scalars', linestyle='--', color= 'red')
ps500, = plt.plot(x0, ys500/cs500,alpha=0.7, label='scalars', linestyle='--', color= 'blue')
ps1000, = plt.plot(x0, ys1000/cs1000,alpha=0.7, label='scalars', linestyle='--', color= 'green')

pv100, = plt.plot(x0, yv100/cv100, alpha=0.7, label='vec', linestyle='-', color= 'red')
pv500, = plt.plot(x0, yv500/cv500,alpha=0.7, label='vec', linestyle='-', color= 'blue')
pv1000, = plt.plot(x0, yv1000/cv1000,alpha=0.7, label='vec', linestyle='-', color= 'green')

legend = plt.legend(handles=[pv100, pv500, pv1000, ps100, ps500, ps1000], loc="upper right", title="comparasion" ,ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('sv.pdf')
plt.show()
