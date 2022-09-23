import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate

#--------------- data input -----------------------#

#scalar 100 GeV
ys1, dys1 = np.genfromtxt('plot_IDM_laL01_100_ZXX.txt',dtype=float, comments='#',unpack=True)
css1 = 0.37  #In fb#

#scalar 500 GeV
ys5, dys5 = np.genfromtxt('plot_IDM_laL01_500_ZXX.txt',dtype=float, comments='#',unpack=True)
css5 = 0.0029 #In fb#

#scalar 800 GeV
ys8, dys8 = np.genfromtxt('plot_IDM_laL01_800_ZXX.txt',dtype=float, comments='#',unpack=True)
css8 =  0.00031 #In fb#



#vector 100 GeV
yv1, dyv1 = np.genfromtxt('plot_VDDMM_laL01_100_ZXX.tab',dtype=float, comments='#',unpack=True)
csv1 = 	730  #In fb#

#vector 500 GeV
yv5, dyv5 = np.genfromtxt('plot_VDDMM_laL01_500_ZXX.tab',dtype=float, comments='#',unpack=True)
csv5 = 0.41  #In fb#

#vector 800 GeV
yv8, dyv8 = np.genfromtxt('plot_VDDMM_laL01_800_ZXX.tab',dtype=float, comments='#',unpack=True)
csv8 =  0.028 #In fb#


#--------------- writing plots -----------------#
fig1,ax2 = plt.subplots()

plt.title('Mono-Z at LHC@13TeV')
plt.xlabel('E$_T^{miss}$ [GeV]',fontsize=16)
plt.ylabel('$\\frac{1}{\\sigma}\\frac{d\\sigma}{dE_T}$[GeV$^{-1}$]',fontsize=16)
plt.xscale('linear')
plt.yscale('log')
plt.ylim(3E-5,1E-2)
plt.xlim(150,1000)
x0=np.linspace(100,1000,90)
xz=np.linspace(135,1000,87)
plt.grid()

#scalars
distsn1, = plt.plot(xz, ys1/(css1*10**(-3)), label='$M_{h1}$ = 100 GeV',color='r',linestyle='--')
distsn5, = plt.plot(xz, ys5/(css5*10**(-3)), label='$M_{h1}$ = 500 GeV',color='m',linestyle='--')
distsn8, = plt.plot(xz, ys8/(css8*10**(-3)), label='$M_{h1}$ = 800 GeV',color='g',linestyle='--')

#vectors

distvn1, = plt.plot(xz, yv1/(csv1*10**(-3)), label='$M_{V1}$ = 100 GeV',color='r',linestyle='-')
distvn5, = plt.plot(xz, yv5/(csv5*10**(-3)), label='$M_{V1}$ = 500 GeV',color='m',linestyle='-')
distvn8, = plt.plot(xz, yv8/(csv8*10**(-3)), label='$M_{V1}$ = 800 GeV',color='g',linestyle='-')


legend1 = plt.legend(handles=[distsn1, distsn5, distsn8,distvn1, distvn5, distvn8], loc="upper right",title=" i2HDM                            DVDM", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 9, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

fig1.tight_layout()
plt.savefig('plot_iDM+VDDMM_nor_ZXX_sum.pdf')
plt.show()
