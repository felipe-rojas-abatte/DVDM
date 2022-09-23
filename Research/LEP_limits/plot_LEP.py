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
Mv, Mvp, csc = np.genfromtxt("LEP_charginos.dat", dtype=float, unpack=True, skip_header=True)  

N=200
def create_contour_data(x, y, z):
	Xi = np.linspace(float(min(x)), float(max(x)),N)
	Yi = np.linspace(float(min(y)), float(max(y)),N)
	Zi = scipy.interpolate.griddata((x,y), z, (Xi[None,:], Yi[:,None]), method='linear')
	return (Xi, Yi, Zi)

# ---------- Plot 2 Mv1-Mv2-Omega --------------------------
cut1 = (Mv1<Mv2)
cut2 = (Mv2-Mv1>8)
cutZ = (Mv1+Mv2>91)
cutE = (Mv1 + Mv2 < 206)
cut_cs = (cs > 0.35)
cut_ok = (cs < 0.35)
#cut_ok1 = (cs < 0.8)

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

cut = cut1&cut2&cutZ&cutE&cut_cs
ok = cut1&cut2&cutZ&cutE&cut_ok

fig2, ax2 = plt.subplots(figsize=(6,4))

cax2 = ax2.scatter(Mv2[ok], Mv1[ok], c='b', s=30, edgecolor='', rasterized=True )
cax2 = ax2.scatter(Mv2[cut], Mv1[cut], c='r', s=30, edgecolor='', rasterized=True, label='excluded')

cs_LEP = create_contour_data(Mv2, Mv1, np.log10(cs))
CS = plt.contour(cs_LEP[0], cs_LEP[1], cs_LEP[2], 10, colors='black', alpha=0.9, linewidth=0.2, linestyle='--')

#manual_locations = [ (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (8, 40),(10,70),(30,80),(60,80),(100,90)]

if plt.rcParams["text.usetex"]:
    fmt = r'10^{%.d} \%%'
else:
    fmt = '$10^{%.d}$ (pb)'
plt.clabel(CS, inline=1, fmt=fmt, fontsize=10)#, manual=manual_locations)

ax2.fill_between(x, y2,0, facecolor='red', alpha=0.5, interpolate=True)
ax2.fill_between(y1, x1 ,100, facecolor='white', alpha=1,interpolate=True)
ax2.text(0.21, 0.2, 'LEP I \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='r', fontsize=15)

plt.plot(M2, M1, linestyle='-', color='k',linewidth=1)
plt.plot(M2, M1S, linestyle='--', color='k',linewidth=1)
plt.plot(M2Z, M1Z, linestyle='-', color='k',linewidth=1)
plt.plot(x2, y3, linestyle='--', color='k',linewidth=1)

#plt.plot(M2, 206-8-M2, linestyle='-', color='m',linewidth=2)

#Name of axes
plt.xlabel("Mv$_2$ (GeV)",fontsize=15)
plt.ylabel("Mv$_1$ (GeV)",fontsize=15)
plt.xlim(0,210)
plt.ylim(0,100)

#plt.grid()
fig2.tight_layout()
plt.savefig('LEP_neutralinos.pdf')

######################################################

# ---------- Plot 2 Mv1-Mv2-Omega --------------------------

cut1 = (Mv<Mvp)
cutE = (Mv + Mvp < 198)
val_cs = 0.75
cut_cs = (csc > val_cs)
cut_ok = (csc < val_cs)


Mp = np.linspace(45, 100, 100)
M = Mp

cut = cut1&cutE&cut_cs
ok = cut1&cutE&cut_ok

fig, ax = plt.subplots(figsize=(6,4))
cax = ax.scatter(Mvp[ok], Mv[ok], c='b', s=30, edgecolor='', rasterized=True )
cax = ax.scatter(Mvp[cut], Mv[cut], c='r', s=30, edgecolor='', rasterized=True, label='excluded')

cs_LEPc = create_contour_data(Mvp, Mv, np.log10(csc))
CSC = plt.contour(cs_LEPc[0], cs_LEPc[1], cs_LEPc[2], 10, colors='black',  alpha=0.9, linewidth=0.2, linestyle='--')

#manual_locations = [ (-2, 0.5), (1.7, 1.2), (2.0, 1.4), (8, 40),(10,70),(30,80),(60,80),(100,90)]

if plt.rcParams["text.usetex"]:
    fmt = r'10^{%.d} \%%'
else:
    fmt = '$10^{%.d}$ (pb)'
plt.clabel(CSC, inline=1, fmt=fmt, fontsize=10)#, manual=manual_locations)

#ax2.fill_between(x, y2,0, facecolor='red', alpha=0.5, interpolate=True)
#ax2.fill_between(y1, x1 ,100, facecolor='white', alpha=1,interpolate=True)
#ax2.text(0.21, 0.2, 'LEP I \n excluded', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='r', fontsize=15)

plt.plot(Mp, M, linestyle='-', color='k',linewidth=1)
#plt.plot(M2, M1S, linestyle='--', color='k',linewidth=1)
#plt.plot(M2Z, M1Z, linestyle='-', color='k',linewidth=1)
#plt.plot(x2, y3, linestyle='--', color='k',linewidth=1)

#plt.plot(M2, 206-8-M2, linestyle='-', color='m',linewidth=2)

#Name of axes
plt.xlabel("M$_v^{\\pm}$ (GeV)",fontsize=15)
plt.ylabel("Mv$_1$ (GeV)",fontsize=15)
plt.xlim(45,100)
plt.ylim(0,95)


fig.tight_layout()
plt.savefig('LEP_charginos.pdf')

plt.clf()



