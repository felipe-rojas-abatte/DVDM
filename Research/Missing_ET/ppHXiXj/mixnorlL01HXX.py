import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate

#--------------- data input -----------------------#


# scalar 500 GeV

ys511, dys511 = np.genfromtxt('plot_iDM_laL01_500_HX1X1.txt',dtype=float, comments='#',unpack=True)
cs511 = 0.0000065  #In fb#
ys512, dys512 = np.genfromtxt('plot_iDM_laL01_500_HX1X2.tab',dtype=float, comments='#',unpack=True)
cs512 = 0.000011 #In fb#
       

#scalar 800 GeV
ys811, dys811 = np.genfromtxt('plot_iDM_laL01_800_HX1X1.txt',dtype=float, comments='#',unpack=True)
cs811 = 0.0000005 #In fb#   
ys812, dys812 = np.genfromtxt('plot_iDM_laL01_800_HX1X2.tab',dtype=float, comments='#',unpack=True)
cs812 = 0.00000071 #In fb#


#vector 500 GeV
yv511, dyv511 = np.genfromtxt('plot_VDDMM_laL01_500_HX1X1.tab',dtype=float, comments='#',unpack=True)
cv511 = 0.000086 #In fb#
yv512, dyv512 = np.genfromtxt('plot_VDDMM_laL01_500_HX1X2.tab',dtype=float, comments='#',unpack=True)
cv512 = 0.00025192 #In fb#


#vector 800 GeV
yv811, dyv811 = np.genfromtxt('plot_VDDMM_laL01_800_HX1X1.tab',dtype=float, comments='#',unpack=True)
cv811 = 0.0000044#In fb#
yv812, dyv812 = np.genfromtxt('plot_VDDMM_laL01_800_HX1X2.tab',dtype=float, comments='#',unpack=True)
cv812 = 0.0000038  #In fb#


#--------------- writing plots -----------------#
fig1,ax2 = plt.subplots()

plt.title('Mono-H transverse missing energy \n in both i2HDM and VDDMM at $\\sqrt{s} = 13$ TeV')
plt.xlabel('E$_T^{miss}$ [GeV]',fontsize=16)
plt.ylabel('$\\frac{1}{\\sigma}\\frac{d\\sigma}{dE_T}$[GeV$^{-1}$]',fontsize=16)
plt.xscale('linear')
plt.yscale('log')
plt.ylim(3E-5,1E-2)
plt.xlim(150,1000)
xh=np.linspace(135,1000,84)

#scalars

ds512, = plt.plot(xh, ys512/(cs512*10**(-3)), label='Hh$_1$h$_2$, Mh1 = 500 GeV',color='black',linestyle='--')
ds511, = plt.plot(xh, ys511/(cs511*10**(-3)), label='Hh$_1$h$_1$, Mh1 = 500 GeV',color='r',linestyle='--')

ds811, = plt.plot(xh, ys811/(cs811*10**(-3)), label='Hh$_1$h$_1$, Mh1 = 800 GeV' ,color='m',linestyle='--')
ds812, = plt.plot(xh, ys812/(cs812*10**(-3)), label='Hh$_1$h$_2$, Mh1 = 800 GeV',color='g',linestyle='--')

#vectors

dv511, = plt.plot(xh, yv511/(cv511*10**(-3)), label='HV$^1$V$^1$, MV1 = 500 GeV',color='r',linestyle='-')
dv512, = plt.plot(xh, yv512/(cv512*10**(-3)), label='HV$^1$V$^2$, MV1 = 500 GeV',color='black',linestyle='-')

dv811, = plt.plot(xh, yv811/(cv811*10**(-3)),label= 'HV$^1$V$^1$, MV1 = 800 GeV',color='m',linestyle='-')
dv812, = plt.plot(xh, yv812/(cv812*10**(-3)), label='HV$^1$V$^2$, MV1 = 800 GeV',color='g',linestyle='-')



legend1 = plt.legend(handles=[ds511, ds512,ds811, ds812, dv511, dv512, dv811, dv812], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('plot_iDM+VDDMM_nor_HXX.pdf')
plt.show()
