from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
import shutil as sh
import math
import os
from scipy.optimize import fsolve

# Abro archivo con base de datos
print('Reading data files')
exec(open('data.py').read())


#size of the dots in scatter plot
dots=5

bounds_lamL=np.linspace(-12,12,21,endpoint=True)
lim_inf_lamL = -12
lim_sup_lamL = 12

bounds_LAM=np.linspace(0,6,7,endpoint=True)
lim_inf_LAM = np.log10(1)
lim_sup_LAM = np.log10(10E6)

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

Mv = np.linspace(10, 2000, 1000)
def fLAM_o(x):
    y = np.where(x<=200, 1000, x*5)
    return y

LAM_o = fLAM_o(Mv) 

#--------Definition of parameters
pi=np.pi
EE=0.31343     
MZ=91.188
MW=80.385      
CW=MW/MZ 
SW=(1-CW**2)**0.5 
vv=2*MW/EE*SW
MH=125
alp=EE**2/(4*pi)
g=EE/SW

#-------Definition of lambda couplings as function of independet parameters
l2 = lamL + (2./vv**2)*(Mv1**2 - Mvp**2)
l3 = (1./vv**2)*(2*Mvp**2 - Mv1**2 - Mv2**2)
l4 = (1./vv**2)*(Mv2**2 - Mv1**2) 
MV2 = Mv1**2 + vv**2*lamL/2
lamR = l2 + l3 - l4

LAM_num = (32*pi)*Mv1**2
LAM_den = lamL+0.5*(lamL*vv/Mv1)**2
LAM = (abs(LAM_num/LAM_den))**0.5

LAM_num2 = (32*pi)*Mv2**2
LAM_den2 = lamR+0.5*(lamR*vv/Mv2)**2
LAM2 = (abs(LAM_num2/LAM_den2))**0.5

LAM_num3 = (32*pi)*Mvp**2
LAM_den3 = l2+0.5*(l2*vv/Mvp)**2
LAM3 = (abs(LAM_num3/LAM_den3))**0.5

LAM_num4 = 192*pi*(Mv1*vv*Mv2*CW**2)**2
f1_4 = -8*Mv1**4 + (Mv1**2)*(8*Mv2**2+5*MZ**2)-18*Mv1*MZ*Mv2**2 + 9*Mv2**4-14*(Mv2*MZ)**2
f2_4 = 11*Mv1**2 + 12*Mv2**2-5*MZ**2
LAM_den4 = CW**4*f1_4 + CW**2*MW**2*f2_4-3*MW**4-6*lamL*(vv*Mv2*CW**2)**2
LAM4 = (abs(LAM_num4/LAM_den4))**0.5

LAM_num5 = 192*pi*(Mv1*vv*Mv2*CW**2)**2
f1_5 = -9*Mv1**4 + (2*Mv1**2)*(-4*Mv2**2+9*Mv2*MZ+7*MZ**2)+8*Mv2**4 -5*(Mv2*MZ)**2
f2_5 = -12*Mv1**2 - 11*Mv2**2 + 5*MZ**2
LAM_den5 = CW**4*f1_5 + CW**2*MW**2*f2_5+3*MW**4+6*lamR*(vv*Mv1*CW**2)**2
LAM5 = (abs(LAM_num5/LAM_den5))**0.5

########################################
#def f(LAM_vc):
# num10 = (LAM_vc)**2*((g**2*(9*(SW**2-CW**2)**2*MW**2 - 4*CW**2*(LAM_vc)**2))/(CW**4*Mvp**2) + 16*(l2*vv/Mvp)**2)
# den10 = 1536*pi*Mvp**2
# A10 = num10/den10
# a10 = abs(A10)
# return a10

#x = fsolve(f,0.5)

#print('LAM = ', x)
##################################################################################

# ----------------- Lambda-Mv1-lamL ----------------------

fig, ax = plt.subplots(figsize=(6,4))
cax = ax.scatter(Mv1, LAM, c=lamL, cmap=cmap, vmin=lim_inf_lamL, vmax=lim_sup_lamL, s=dots, edgecolor='', rasterized=True)
ax.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
ax.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax.transAxes, alpha=0.8, color='k', fontsize=14)
cbar = fig.colorbar(cax,ticks=bounds_lamL, format="$%.d$")
cbar.set_label('$\\lambda_L$', rotation=90, fontsize=15)

#selecciono los primeros 10 puntos del scan de parametros

#Mv1_points = [Mv1[i] for i in range (0,10)]
#LAM_points = [LAM[i] for i in range (0,10)]

#ax.scatter(Mv1_points,LAM_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\Lambda$ (GeV) ",fontsize=15)
plt.title("Process $hV^1\\rightarrow hV^1$")
plt.xlim(10,2000)
plt.ylim(1,1E6)
plt.xscale('log')
plt.yscale('log')

cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')
#LMD2, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle=':', label='$\\Lambda_o = 5000$ (GeV)')

legend1b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

plt.gca().add_artist(legend1b)
plt.grid()
fig.tight_layout()
plt.savefig('LAM_Mv1_lamL_hV1.pdf')


# ----------------- Lambda-Mv2-lamR

fig2, ax2 = plt.subplots(figsize=(6,4))
cax2 = ax2.scatter(Mv2, LAM2, c=lamR, cmap=cmap, vmin=lim_inf_lamL, vmax=lim_sup_lamL, s=dots, edgecolor='', rasterized=True)
ax2.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
ax2.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, alpha=0.8, color='k', fontsize=14)
cbar2 = fig2.colorbar(cax2,ticks=bounds_lamL, format="$%.d$")
cbar2.set_label('$\\lambda_R$', rotation=90, fontsize=15)

#Mv2_points = [Mv2[i] for i in range (0,10)]
#LAM2_points = [LAM2[i] for i in range (0,10)]

#ax2.scatter(Mv2_points,LAM2_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("$\\Lambda$ (GeV) ",fontsize=15)
plt.title("Process $hV^2\\rightarrow hV^2$")
plt.xlim(10,2000)
plt.ylim(1,1E6)
plt.xscale('log')
plt.yscale('log')

cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')

legend2b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

plt.gca().add_artist(legend2b)
plt.grid()
fig2.tight_layout()
plt.savefig('LAM_Mv2_lamR_hV2.pdf')

# ----------------- Lambda-Mv2-lamR

fig3, ax3 = plt.subplots(figsize=(6,4))
cax3 = ax3.scatter(Mvp, LAM3, c=l2, cmap=cmap, vmin=lim_inf_lamL, vmax=lim_sup_lamL, s=dots, edgecolor='', rasterized=True)
ax3.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
ax3.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax3.transAxes, alpha=0.8, color='k', fontsize=14)
cbar3 = fig3.colorbar(cax3,ticks=bounds_lamL, format="$%.d$")
cbar3.set_label('$\\lambda_2$', rotation=90, fontsize=15)

#Mvp_points = [Mvp[i] for i in range (0,10)]
#LAM3_points = [LAM3[i] for i in range (0,10)]

#ax3.scatter(Mvp_points,LAM3_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$^{\\pm}$ (GeV)",fontsize=15)
plt.ylabel("$\\Lambda$ (GeV) ",fontsize=15)
plt.title("Process $hV^{\\pm}\\rightarrow hV^{\\pm}$")
plt.xlim(10,2000)
plt.ylim(1,1E6)
plt.xscale('log')
plt.yscale('log')

cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')

legend3b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

plt.gca().add_artist(legend3b)
plt.grid()
fig3.tight_layout()
plt.savefig('LAM_Mvp_l2_hVC.pdf')


# ----------------- Lambda-Mv1-lamL -------------

fig4, ax4 = plt.subplots(figsize=(6,4))
cax4 = ax4.scatter(Mv1, LAM4, c=lamL, cmap=cmap, vmin=lim_inf_lamL, vmax=lim_sup_lamL, s=dots, edgecolor='', rasterized=True)
ax4.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
ax4.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax4.transAxes, alpha=0.8, color='k', fontsize=14)
cbar4 = fig4.colorbar(cax4,ticks=bounds_lamL, format="$%.d$")
cbar4.set_label('$\\lambda_L$', rotation=90, fontsize=15)

#Mvp_points = [Mvp[i] for i in range (0,10)]
#LAM3_points = [LAM3[i] for i in range (0,10)]

#ax3.scatter(Mvp_points,LAM3_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\Lambda$ (GeV) ",fontsize=15)
plt.title("Process $ZV^1\\rightarrow ZV^1$")
plt.xlim(10,2000)
plt.ylim(1,1E6)
plt.xscale('log')
plt.yscale('log')

cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')

legend4b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

plt.gca().add_artist(legend4b)
plt.grid()
fig4.tight_layout()
plt.savefig('LAM_Mv1_lamL_ZV1.pdf')

# ----------------- Lambda-Mv1-lamR -------------

fig5, ax5 = plt.subplots(figsize=(6,4))
cax5 = ax5.scatter(Mv1, LAM5, c=lamR, cmap=cmap, vmin=lim_inf_lamL, vmax=lim_sup_lamL, s=dots, edgecolor='', rasterized=True)
ax5.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
ax5.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax5.transAxes, alpha=0.8, color='k', fontsize=14)
cbar5 = fig5.colorbar(cax5,ticks=bounds_lamL, format="$%.d$")
cbar5.set_label('$\\lambda_R$', rotation=90, fontsize=15)

#Mvp_points = [Mvp[i] for i in range (0,10)]
#LAM3_points = [LAM3[i] for i in range (0,10)]

#ax3.scatter(Mvp_points,LAM3_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\Lambda$ (GeV) ",fontsize=15)
plt.title("Process $ZV^2\\rightarrow ZV^2$")
plt.xlim(10,2000)
plt.ylim(1,1E6)
plt.xscale('log')
plt.yscale('log')

cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')

legend5b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

plt.gca().add_artist(legend5b)
plt.grid()
fig5.tight_layout()
plt.savefig('LAM_Mv1_lamR_ZV2.pdf')

# ----------------- Mv1-lamL-Lambda ----------------------

fig6, ax6 = plt.subplots(figsize=(6,4))
cax6 = ax6.scatter(Mv1, lamL, c=np.log10(LAM), cmap=cmap, vmin=lim_inf_LAM, vmax=lim_sup_LAM, s=dots, edgecolor='', rasterized=True)
#ax.fill_between(Mv, LAM_o, facecolor='gray', alpha = 0.45, interpolate=True)  #, hatch="//" linewidth=0.2, 
#ax.text(0.8, 0.3, 'Excluded by \n Unitarity', verticalalignment='top', horizontalalignment='center', transform=ax.transAxes, alpha=0.8, color='k', fontsize=14)
cbar6 = fig6.colorbar(cax6,ticks=bounds_LAM, format="$10^{%.d}$")
cbar6.set_label('$\\Lambda$ (GeV)', rotation=90, fontsize=15)

#selecciono los primeros 10 puntos del scan de parametros

#Mv1_points = [Mv1[i] for i in range (0,10)]
#LAM_points = [LAM[i] for i in range (0,10)]

#ax.scatter(Mv1_points,LAM_points, s=30, c="r", marker='^')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\lambda_L$ ",fontsize=15)
plt.title("Process $hV^1\\rightarrow hV^1$")
plt.xlim(10,2000)
plt.ylim(-12,12)
plt.xscale('log')

#cutoff, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle='--', label='$\\Lambda_o^{cut-off}$')
#LMD2, = plt.plot(Mv, LAM_o, color='r',linewidth=2, linestyle=':', label='$\\Lambda_o = 5000$ (GeV)')

#legend1b = plt.legend(handles=[cutoff], loc="upper left", ncol=1, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

#plt.gca().add_artist(legend1b)
plt.grid()
fig6.tight_layout()
plt.savefig('Mv1_lamL_LAM_hV1.pdf')


