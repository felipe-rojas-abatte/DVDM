from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
import shutil as sh
import math
import os
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# Abro archivo con base de datos
print('Reading data files')
exec(open('data.py').read())

# Abro archivo con cortes
print('Reading cuts file')
exec(open('cuts.py').read())


cut_planck=cut0&cut5&cut10 #PLANCK
cut_A=cut0&cut1&cut2&cut5&cut10 #Pert, LEP, PLANCK
cut_B=cut0&cut1&cut2&cut3&cut5&cut10 #Pert, LEP, PLANCK, Inv Higgs
cut_C=cut0&cut1&cut2&cut3&cut5&cut7&cut10 #Pert, LEP, PLANCK, Inv Higgs, DD
cut_D=cut0&cut1&cut2&cut3&cut4&cut5&cut7&cut10 #Pert, LEP, PLANCK, Inv Higgs, DD, HAA
cuts='sat_color'
print('	Generating plots with '+cuts+': ')

#size of the dots in scatter plot
dots=6
#Create the features of the colorbar
bounds=np.linspace(-7,5,13,endpoint=True)
lim_inf = np.log10(0.0000001)
lim_sup = np.log10(100)

Mvchar = np.linspace(10, 2000, 1000) 
mu_sup_new = np.linspace(0.99+0.14,0.99+0.14,1000) 
mu_inf_new = np.linspace(0.99-0.14,0.99-0.14,1000)

bounds_l2=np.linspace(-10,10,21,endpoint=True)
lim_inf_l2 = -10
lim_sup_l2 = 10

#Define the quantity of colors in colorbar
cmap = plt.get_cmap('jet') 

fig, ax = plt.subplots(figsize=(6,4))
#fig = plt.subplots(figsize=(6,4))
#fig.set_size_inches(6, 10, forward=True)

A1 = ax.scatter(Mv1[cut_A], lamL[cut_A], c='k', s=dots, edgecolor='', rasterized=True)
A2 = ax.scatter(Mv1[cut_B], lamL[cut_B], c='darkgrey', s=dots, edgecolor='', rasterized=True)
A3 = ax.scatter(Mv1[cut_C], lamL[cut_C], c='dimgrey', s=dots, edgecolor='', rasterized=True)
A4 = ax.scatter(Mv1[cut_D], lamL[cut_D], c='r', s=dots, edgecolor='', rasterized=True)

#Name of axes 
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\lambda_L$", fontsize=20)
plt.xlim(10,2000)
#plt.xlim(10,2000)
plt.xscale('log')
plt.ylim(-3,4)

plt.legend((A1,A2,A3,A4), ('$H\\rightarrow $ inv', 'XENON1T', '$H\\rightarrow \\gamma \\gamma$', 'allowed',), scatterpoints=1, loc='upper right', ncol=2, fontsize=9)

## Zoom area
axins = zoomed_inset_axes(ax, 2.2, loc='upper left', bbox_to_anchor=(200, 200))
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

dots_z = 10
axins.scatter(Mv1[cut_A], lamL[cut_A], c='k', s=dots_z, edgecolor='', rasterized=True)
axins.scatter(Mv1[cut_B], lamL[cut_B], c='darkgrey', s=dots_z, edgecolor='', rasterized=True)
axins.scatter(Mv1[cut_C], lamL[cut_C], c='dimgrey', s=dots_z, edgecolor='', rasterized=True)
axins.set_xlim(40, 80)
axins.set_ylim(-0.3, 0.3)
axins.yaxis.set_visible('False')


#fig.tight_layout()
plt.savefig('prueba.pdf')
