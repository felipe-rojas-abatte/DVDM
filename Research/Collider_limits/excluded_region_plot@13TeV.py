import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp2d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import os

current_dir = os.getcwd()
this_file = current_dir+'/data/'

#Read data at 13 TeV
Mv1, lamL, xs, r, Acc, SR, ds, Sobs, xs_lim = np.genfromtxt(this_file+"Exclusion_limits_from_pp_v1v1j.dat", dtype=float, unpack=True, skip_header=True)
Mv1b, Mv2b, xsb, rb, Accb, SRb, dsb, Sobsb, xs_limb = np.genfromtxt(this_file+"Exclusion_limits_from_pp_v1v2j.dat", dtype=float, unpack=True, skip_header=True)

#Read data at 14 TeV
Mv1c, lamLc, xs_14, xs_lim36, xs_lim100, xs_lim3000 = np.genfromtxt('pp_v1v1j_14TeV_xslim.dat', dtype=float, unpack=True, skip_header=True)

M1 = np.linspace(10,2000,100)

N=200
def create_contour_data(x, y, z):
	Xi = np.linspace(float(min(x)), float(max(x)),N)
	Yi = np.linspace(float(min(y)), float(max(y)),N)
	Zi = scipy.interpolate.griddata((x,y), z, (Xi[None,:], Yi[:,None]), method='linear')
	return (Xi, Yi, Zi)

#### criterio para aceptar o rechazar un punto

# v1v1j at 13 TeV
accepted_v1v1j = (r<1)
rejected_v1v1j = (r>=1)
# v1v2j at 13 TeV
accepted_v1v2j = (rb<1)
rejected_v1v2j = (rb>=1)
# v1v1j at 14 TeV
rejected_36 = (xs_14>xs_lim36)
rejected_100 = (xs_14>xs_lim100)
rejected_3000 = (xs_14>xs_lim3000)

#### contorno rechazado
# v1v1j at 13 TeV
cs_rejected_v1v1j = create_contour_data(Mv1[rejected_v1v1j], lamL[rejected_v1v1j], xs[rejected_v1v1j])
# v1v2j at 13 TeV
cs_rejected_v1v2j = create_contour_data(Mv1b[rejected_v1v2j], Mv2b[rejected_v1v2j], xsb[rejected_v1v2j])
# v1v1j at 14 TeV
cs_rejected_36 = create_contour_data(Mv1c[rejected_36], lamLc[rejected_36], xs_14[rejected_36])
cs_rejected_100 = create_contour_data(Mv1c[rejected_100], lamLc[rejected_100], xs_14[rejected_100])
cs_rejected_3000 = create_contour_data(Mv1c[rejected_3000], lamLc[rejected_3000], xs_14[rejected_3000])


##### Mv1 - lamL exclusion region
fig,ax = plt.subplots(figsize=(6,4))

ax.text(0.52, 0.9, 'Excluded by \n $pp\\rightarrow v_1v_1j$', verticalalignment='top', horizontalalignment='center', transform=ax.transAxes, color='k', fontsize=13)

CS1 = plt.contourf(cs_rejected_v1v1j[0], cs_rejected_v1v1j[1], cs_rejected_v1v1j[2], 0, colors='r', alpha=1)
CS2 = plt.contourf(cs_rejected_36[0], cs_rejected_36[1], cs_rejected_36[2], 0, colors='r', alpha=0.5)
CS3 = plt.contourf(cs_rejected_100[0], cs_rejected_100[1], cs_rejected_100[2], 0, colors='r', alpha=0.3)
CS4 = plt.contourf(cs_rejected_3000[0], cs_rejected_3000[1], cs_rejected_3000[2], 0, colors='r', alpha=0.2)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("$\\lambda_L$ ",fontsize=15)
#plt.xscale('log')
plt.xlim(100,500)
plt.ylim(-12,12)

cs1,_ = CS1.legend_elements()
cs2,_ = CS2.legend_elements()
cs3,_ = CS3.legend_elements()
cs4,_ = CS4.legend_elements()
plt.legend([cs1[0], cs2[0], cs3[0], cs4[0]], ['13TeV, $\\mathscr{L}=36.1(fb^{-1})$', '14TeV, $\\mathscr{L}=36.1(fb^{-1})$','14TeV, $\\mathscr{L}=100(fb^{-1})$','14TeV, $\\mathscr{L}=3000(fb^{-1})$'],loc='lower left')

fig.tight_layout()
plt.savefig('Excluded_region_in_Mv1_lamL_plane.pdf')

##### Mv1 - Mv2 exclusion region
fig2,ax2 = plt.subplots(figsize=(6,4))

ax2.text(0.52, 0.9, 'Excluded by \n $pp\\rightarrow v_1v_2j$', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='r', fontsize=13)

plt.contourf(cs_rejected_v1v2j[0], cs_rejected_v1v2j[1], cs_rejected_v1v2j[2], 0, colors='r', alpha=0.4)
#CS = plt.contour(cs_cut[0], cs_cut[1], cs_cut[2],10, colors='black', alpha=0.9, linewidth=0.2, linestyle='--')

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=15)
plt.ylabel("Mv$_2$ (GeV)",fontsize=15)
plt.xscale('log')
plt.yscale('log')
plt.xlim(10,2000)
plt.ylim(10,2000)
#plt.grid()

plt.plot(M1,M1, color='k', linestyle='--')

fig2.tight_layout()
plt.savefig('Excluded_region_in_Mv1_Mv2_plane.pdf')

plt.clf()





