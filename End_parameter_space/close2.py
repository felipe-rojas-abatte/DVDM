import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import os


current_dir = os.getcwd()
this_file = current_dir+'/'

#PLANCK measurements
Mv = np.linspace(350, 40000, 2000)
omega = np.linspace(0.1184,0.1184,2000)

#Read data for quasi-degenerate values of Masses
Mv1a, Mv2a, Mvpa, lamLa, Omegaa, prota, Brv1a, Brv2a, Brvpa, BrhAAa, WHa = np.genfromtxt(this_file+"close_lamL=4pi,DltM=5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b, Mv2b, Mvpb, lamLb, Omegab, protb, Brv1b, Brv2b, Brvcb, BrhAAb, WHb = np.genfromtxt(this_file+"close_lamL=4pi,DltM=10.dat", dtype=float, unpack=True, skip_header=True) 
Mv1c, Mv2c, Mvpc, lamLc, Omegac, protc, Brv1c, Brv2c, Brvcc, BrhAAc, WHc = np.genfromtxt(this_file+"close_lamL=4pi,DltM=20.dat", dtype=float, unpack=True, skip_header=True) 
Mv1d, Mv2d, Mvpd, lamLd, Omegad, protd, Brv1d, Brv2d, Brvcd, BrhAAd, WHd = np.genfromtxt(this_file+"close_lamL=4pi,DltM=50.dat", dtype=float, unpack=True, skip_header=True) 

###################################################################################
## Planck limits for Relic Density vs Mh1 for quasi-degenerate case fixing lamL=4pi
###################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv1c, Omegac, 1E-7 ,facecolor='palegreen', interpolate=True)
ax1.text(0.7, 0.4, '$\\Delta M$ too large ', verticalalignment='top', horizontalalignment='center', transform=ax1.transAxes, color='green', fontsize=12)

ax1.fill_between(Mv, omega, 1E3 ,facecolor='cyan', interpolate=True)
ax1.text(0.5, 0.8, 'Excluded by \n over-abundance ', verticalalignment='top', horizontalalignment='center', transform=ax1.transAxes, color='b', fontsize=12)

ax1.text(0.2, 0.58, 'Allowed parameter \n space ', verticalalignment='top', horizontalalignment='center', transform=ax1.transAxes, color='k', fontsize=12)


#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=17)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=15)
plt.title('$\\lambda_{L} = 4\\pi$',fontsize=15)
plt.yscale('log')  
plt.xscale('log')
plt.xlim(350,40000)
plt.ylim(1E-7,1E3)

DEG1, = plt.plot(Mv1a, Omegaa, label='$\\Delta M = 5$',color='b',linestyle='--')
DEG2, = plt.plot(Mv1b, Omegab, label='$\\Delta M = 10$',color='r',linestyle='--')
DEG3, = plt.plot(Mv1c, Omegac, label='$\\Delta M = 20$',color='g',linestyle='-')
DEG4, = plt.plot(Mv1d, Omegad, label='$\\Delta M = 50$',color='k',linestyle='--')
#DEG5, = plt.plot(Mv1e, Omegae, label='$\lambda_L=4\\pi$',color='g',linestyle='-')
#DEG6, = plt.plot(Mv1f, Omegaf, label='$\lambda_L=4\\pi$',color='k',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend1 = plt.legend(handles=[DEG1,DEG2,DEG3,DEG4], loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower right", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#Agregamos la primera leyenda
plt.gca().add_artist(legend1)

plt.savefig('close_parameter_space2.pdf')
