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

#Read data for quasi-degenerate values of Masses
Mv1, Mv2, cs = np.genfromtxt("LEP_neutralinos.dat", dtype=float, unpack=True, skip_header=True)
Mv, Mvp, csc = np.genfromtxt("LEP_vcvc.dat", dtype=float, unpack=True, skip_header=True)  

N=200
def create_contour_data(x, y, z):
	Xi = np.linspace(float(min(x)), float(max(x)),N)
	Yi = np.linspace(float(min(y)), float(max(y)),N)
	Zi = scipy.interpolate.griddata((x,y), z, (Xi[None,:], Yi[:,None]), method='linear')
	return (Xi, Yi, Zi)

# ---------- Plot 1 Mv1-Mv2-cs --------------------------
cut1 = (Mv1<Mv2)
cut2 = (Mv2-Mv1>5)
cutZ = (Mv1+Mv2>91)
cutE = (Mv1 + Mv2 < 206)
cut_cs = (cs > 0.35)
cut_cs2 = (cs < 0.35)

M2 = np.linspace(0, 210, 100)
M2Z= np.linspace(45.5, 91, 100)
M1 = M2
M1S = 206 - M2
M1Z = 91 - M2Z

x = [0,45.5,91]
x1 = [0,45.5,100]
x2 = [41+8,100+8]
y1= [0,45.5,100]
y2= [91,45.5,0]
y3= [41,100] 

cut = cut1&cut2&cutE#&cut_cs
ok = cut1&cut2&cutE&cut_cs2

fig2, ax2 = plt.subplots(figsize=(6,4))

cs_LEP = create_contour_data(Mv2, Mv1, np.log10(cs))
cs_LEPok = create_contour_data(Mv2[ok], Mv1[ok], np.log10(cs[ok]))
cs_LEPcut = create_contour_data(Mv2[cut], Mv1[cut], np.log10(cs[cut]))

CS = plt.contour(cs_LEP[0], cs_LEP[1], cs_LEP[2],10, colors='black', alpha=0.9, linewidth=0.2, linestyle='--')

plt.contourf(cs_LEPcut[0], cs_LEPcut[1], cs_LEPcut[2], 0, colors='r',  alpha=0.4)
plt.contourf(cs_LEPok[0], cs_LEPok[1], cs_LEPok[2], 0, colors='b', alpha=0.5)

manual_locations = [   (8, 40),(10,70),(30,80),(60,80),(100,90)]

if plt.rcParams["text.usetex"]:
    fmt = r'10^{%.d} \%%'
else:
    fmt = '$10^{%.d}$ (pb)'
plt.clabel(CS, inline=1, fmt=fmt, fontsize=8, manual=manual_locations)

ax2.fill_between(x, y2,0, facecolor='red', alpha=1, interpolate=True)
ax2.fill_between(y1, x1 ,100, facecolor='white', alpha=1,interpolate=True)
ax2.fill_between(y1, x1 ,100, facecolor='white', alpha=1,interpolate=True)
ax2.text(0.21, 0.25, 'LEP I \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='k', fontsize=15)
ax2.text(0.5, 0.5, 'LEP II \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='k', fontsize=15)


plt.plot(M2, M1, linestyle='-', color='k',linewidth=1)
plt.plot(M2, M1S, linestyle='--', color='k',linewidth=1)
plt.plot(M2Z, M1Z, linestyle='-', color='k',linewidth=1)
plt.plot(x2, y3, linestyle='--', color='k',linewidth=1)


#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("Mv$_1$ (GeV)",fontsize=15)
plt.xlim(0,210)
plt.ylim(0,100)

#plt.grid()
fig2.tight_layout()
plt.savefig('LEP_neutralinos_v2.pdf')

######################################################

# ---------- Plot 2 Mv1-Mvp-cs --------------------------

cut1 = (Mv<Mvp)
cutE = (2*Mvp < 190)
val_cs1 = 0.75
val_cs2 = 0.4
val_cs3 = 0.2
val_cs4 = 0.09
val_cs5 = 0.075
cut_ok1 = (csc <= val_cs1)
cut_ok2 = (csc <= val_cs2)
cut_ok3 = (csc <= val_cs3)
cut_ok4 = (csc <= val_cs4)
cut_ok5 = (csc <= val_cs5)
cut_Mass1 = (Mv<14)
cut_Mass2 = (Mv>=14)&(Mv<24)
cut_Mass3 = (Mv>=24)&(Mv<48)
cut_Mass4 = (Mv>=48)&(Mv<60)
cut_Mass5 = (Mv>=60)&(Mv<100)

Mp = np.linspace(1, 95, 100)
M = Mp
Mv1W = 80 - Mp


cut = cut1&cutE#&cut_cs
ok1 = cut1&cutE&cut_ok1&cut_Mass1
ok2= cut1&cutE&cut_ok2&cut_Mass2
ok3= cut1&cutE&cut_ok3&cut_Mass3
ok4= cut1&cutE&cut_ok4&cut_Mass4
ok5= cut1&cutE&cut_ok5&cut_Mass5

fig, ax = plt.subplots(figsize=(6,4))

cs_LEPc = create_contour_data(Mvp, Mv, np.log10(csc))
cs_LEPcok1 = create_contour_data(Mvp[ok1], Mv[ok1], np.log10(csc[ok1]))
cs_LEPcok2 = create_contour_data(Mvp[ok2], Mv[ok2], np.log10(csc[ok2]))
cs_LEPcok3 = create_contour_data(Mvp[ok3], Mv[ok3], np.log10(csc[ok3]))
cs_LEPcok4 = create_contour_data(Mvp[ok4], Mv[ok4], np.log10(csc[ok4]))
cs_LEPcok5 = create_contour_data(Mvp[ok5], Mv[ok5], np.log10(csc[ok5]))
cs_LEPccut = create_contour_data(Mvp[cut], Mv[cut], np.log10(csc[cut]))

CSC = plt.contour(cs_LEPc[0], cs_LEPc[1], cs_LEPc[2],4, colors='black',  alpha=0.9, linewidth=0.2, linestyle='--')

plt.contourf(cs_LEPccut[0], cs_LEPccut[1], cs_LEPccut[2], 0, colors='r', alpha=0.4)
plt.contourf(cs_LEPcok1[0], cs_LEPcok1[1], cs_LEPcok1[2], 0, colors='b', alpha=0.5)
plt.contourf(cs_LEPcok2[0], cs_LEPcok2[1], cs_LEPcok2[2], 0, colors='b', alpha=0.5)
plt.contourf(cs_LEPcok3[0], cs_LEPcok3[1], cs_LEPcok3[2], 0, colors='b', alpha=0.5)
plt.contourf(cs_LEPcok4[0], cs_LEPcok4[1], cs_LEPcok4[2], 0, colors='b', alpha=0.5)
plt.contourf(cs_LEPcok5[0], cs_LEPcok5[1], cs_LEPcok5[2], 0, colors='b', alpha=0.5)

if plt.rcParams["text.usetex"]:
    fmt = r'10^{%.d} \%%'
else:
    fmt = '$10^{%.d}$ (pb)'
manual_locations = [ (46,65),(75,60),(90,60),(95,60)]
plt.clabel(CSC, inline=1, fmt=fmt, fontsize=10, manual=manual_locations)

ax.fill_between(Mp, Mv1W,0, facecolor='red', alpha=1, interpolate=True)

ax.text(0.3, 0.3, 'LEP II \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='k', fontsize=15)
ax.text(0.08, 0.1, 'LEP I \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='k', fontsize=15)

plt.plot(Mp, M, linestyle='-', color='k',linewidth=1)

#Name of axes
plt.xlabel("M$_{v^{\\pm}}$ (GeV)",fontsize=15)
plt.ylabel("Mv$_1$ (GeV)",fontsize=15)
plt.xlim(45,95)
plt.ylim(0,95)

plt.plot(Mp, Mv1W, linestyle='-', color='k',linewidth=1)

fig.tight_layout()
plt.savefig('LEP_charginos_v2.pdf')

plt.clf()



