import os
import matplotlib.pyplot as plt
import numpy as np
from math import exp, log, sqrt
from scipy import interpolate

#--------------- data input -----------------------#
#scalar 800 GeV
ys0, dys0 = np.genfromtxt('plot_iDM_laL01_ZX1X1.tab',dtype=float, comments='#',unpack=True)
css0 = 0.0000543 #In fb#
ys1, dys1 = np.genfromtxt('plot_iDM_laL01_ZX1X2.tab',dtype=float, comments='#',unpack=True)
css1 = 0.00019022 #In fb#

# scalar 500 GeV
ys500, dys500 = np.genfromtxt('plot_iDM_laL01_500_ZX1X2.tab',dtype=float, comments='#',unpack=True)
css500 = 0.0016988 #In fb#
ys5002, dys5002 = np.genfromtxt('plot_iDM_laL01_500_ZX1X1.tab',dtype=float, comments='#',unpack=True)
css5002 =  0.00054739 #In fb#


#vector 800 GeV
yv0, dyv0 = np.genfromtxt('plot_VDDMM_laL01_ZX1X1.tab',dtype=float, comments='#',unpack=True)
csv0 = 0.0067368 #In fb#
yv1, dys1 = np.genfromtxt('plot_VDDMM_laL01_ZX1X2.tab',dtype=float, comments='#',unpack=True)
csv1 = 0.014135 #In fb#

#vector 500 GeV
yv500, dyv500 = np.genfromtxt('plot_VDDMM_laL01_500_ZX1X1.tab',dtype=float, comments='#',unpack=True)
csv500 = 0.11147  #In fb#
yv5002, dys5005 = np.genfromtxt('plot_VDDMM_laL01_500_ZX1X2.tab',dtype=float, comments='#',unpack=True)
csv5002 = 0.17758 #In fb#



#--------------- writing plots -----------------#
fig1,ax2 = plt.subplots()

plt.title('Mono-Z transverse missing energy \n in both i2HDM and VDDMM')
plt.xlabel('E$_T^{miss}$ [GeV]',fontsize=16)
plt.ylabel('$\\frac{1}{\\sigma}\\frac{d\\sigma}{dE_T}$[GeV$^{-1}$]',fontsize=16)
plt.xscale('linear')
plt.yscale('log')
plt.ylim(3E-5,1E-2)
plt.xlim(150,1000)
x0=np.linspace(100,1000,90)
xz=np.linspace(135,1000,87)

#scalars

distsn0, = plt.plot(xz, ys0/(css0*10**(-3)), label='Zh$_1$h$_1$, Mh1 = 800 GeV' ,color='m',linestyle='--')
distsn1, = plt.plot(xz, ys1/(css1*10**(-3)), label='Zh$_1$h$_2$, Mh1 = 800 GeV',color='g',linestyle='--')

dists500, = plt.plot(xz, ys500/(css500*10**(-3)), label='Zh$_1$h$_2$, Mh1 = 500 GeV',color='black',linestyle='--')
dists5002, = plt.plot(xz, ys5002/(css5002*10**(-3)), label='Zh$_1$h$_1$, Mh1 = 500 GeV',color='r',linestyle='--')

#vectors

distvn0, = plt.plot(xz, yv0/(csv0*10**(-3)),label= 'ZV$^1$V$^1$, MV1 = 800 GeV',color='m',linestyle='-')
distvn1, = plt.plot(xz, yv1/(csv1*10**(-3)), label='ZV$^1$V$^2$, MV1 = 800 GeV',color='g',linestyle='-')

distv500, = plt.plot(xz, yv500/(csv500*10**(-3)), label='ZV$^1$V$^1$, MV1 = 500 GeV',color='r',linestyle='-')
distv5002, = plt.plot(xz, yv5002/(csv5002*10**(-3)), label='ZV$^1$V$^2$, MV1 = 500 GeV',color='black',linestyle='-')



legend1 = plt.legend(handles=[dists500, dists5002,distsn1, distsn0, distv5002, distv500, distvn1, distvn0], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

plt.savefig('plot_iDM+VDDMM_nor_ZXX.pdf')
plt.show()
