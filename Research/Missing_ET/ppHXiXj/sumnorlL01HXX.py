import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate

#--------------- data input -----------------------#
#scalar 100 GeV
ys1, dys1 = np.genfromtxt('plot_iDM_laL01_100_HXX.txt',dtype=float, comments='#',unpack=True)
cs1 = 0.010598 #In fb#

#scalar 500 GeV
ys5, dys5 = np.genfromtxt('plot_iDM_laL01_500_HXX.txt',dtype=float, comments='#',unpack=True)
cs5 = 0.0000225 #In fb#

#scalar 800 GeV
ys8, dys8 = np.genfromtxt('plot_iDM_laL01_800_HXX.txt',dtype=float, comments='#',unpack=True)
cs8 = 0.0000020 #In fb#


#vector 100 GeV
yv1, dyv1 = np.genfromtxt('plot_VDDMM_laL01_100_HXX.tab',dtype=float, comments='#',unpack=True)
cv1 = 308.62 #In fb#

#vector 500 GeV
yv5, dyv5 = np.genfromtxt('plot_VDDMM_laL01_500_HXX.tab',dtype=float, comments='#',unpack=True)
cv5 = 0.00037484 #In fb#

#vector 800 GeV
yv8, dyv8 = np.genfromtxt('plot_VDDMM_laL01_800_HXX.tab',dtype=float, comments='#',unpack=True)
cv8 = 0.00000923  #In fb#

#--------------- writing plots -----------------#
fig1,ax2 = plt.subplots()

plt.title('Mono-H at LHC@13TeV')
plt.xlabel('E$_T^{miss}$ [GeV]',fontsize=16)
plt.ylabel('$\\frac{1}{\\sigma}\\frac{d\\sigma}{dE_T}$[GeV$^{-1}$]',fontsize=16)
plt.xscale('linear')
plt.yscale('log')
plt.ylim(3E-5,1E-2)
plt.xlim(150,1000)
xh=np.linspace(135,1000,84)
plt.grid()

#scalars
distns1, = plt.plot(xh, ys1/(cs1*10**(-3)),label= '$M_{h1}$ = 100 GeV',color='r',linestyle='--')
distns5, = plt.plot(xh, ys5/(cs5*10**(-3)),label= '$M_{h1}$ = 500 GeV',color='m',linestyle='--')
distns8, = plt.plot(xh, ys8/(cs8*10**(-3)),label= '$M_{h1}$ = 800 GeV',color='g',linestyle='--')


#vectors
distnv1, = plt.plot(xh, yv1/(cv1*10**(-3)),label= '$M_{V1}$ = 100 GeV',color='r',linestyle='-')
distnv5, = plt.plot(xh, yv5/(cv5*10**(-3)),label= '$M_{V1}$ = 500 GeV',color='m',linestyle='-')
distnv8, = plt.plot(xh, yv8/(cv8*10**(-3)),label= '$M_{V1}$ = 800 GeV',color='g',linestyle='-')


legend1 = plt.legend(handles=[distns1, distns5, distns8,distnv1, distnv5, distnv8], loc="upper right",title=" i2HDM                            DVDM", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 9, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

fig1.tight_layout()
plt.savefig('plot_iDM+VDDMM_nor_HXX_sum.pdf')
plt.show()
