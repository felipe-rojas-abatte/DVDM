import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
import os

current_dir = os.getcwd()
this_file = current_dir+'/data/'

#Read the data file and save it in the variables
#Cross sections files
Mv1a, lamLa, xsa = np.genfromtxt (this_file+"pp_v1v1j_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b, lamLb, xsb = np.genfromtxt (this_file+"pp_v1v1j_lamL=5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1c, lamLc, xsc = np.genfromtxt (this_file+"pp_v1v1j_lamL=10.dat", dtype=float, unpack=True, skip_header=True) 


Mv1_CMa, lamL_CMa, xs_CMa, r_CMa, Acc_CMa, SR_CMa, ds_CMa, Sobs_CMa, xs_lim_CMa = np.genfromtxt (this_file+"CM_xs_pp_v1v1j_lamL=1.dat",dtype=float,unpack=True,skip_header=True) 

#Interpolation of the CheckMATE analysis
SIG_LIM_CMa = interp1d(Mv1_CMa, xs_lim_CMa, kind='linear')
SIGa = SIG_LIM_CMa(Mv1a) 

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=13)
#Name of axes 
plt.title("$\\sigma(pp\\rightarrow V_1V_1j)$ (fb) at 13 TeV",fontsize=14)
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow V_1V_1j)$ (fb) with $P_T^{jet} > 200$ GeV", fontsize=14)
#plt.title('$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(100,400)
#plt.ylim(0.0000001,4000)
plt.yscale('log')

plt.plot(Mv1a, xsa, linestyle='--',color='b',linewidth=2, label="$\\lambda_{L}=1$")
plt.plot(Mv1b, xsb, linestyle='--',color='g',linewidth=2, label="$\\lambda_{L}=5$")
plt.plot(Mv1c, xsc, linestyle='--',color='m',linewidth=2, label="$\\lambda_{L}=10$")
plt.plot(Mv1a, SIGa, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 36.1 fb^{-1} )$")

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True, fontsize = 10,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('CM_limit_v1v1j_13TeV.pdf')
plt.clf()


#Read the data file and save it in the variables
#Cross sections files
Mv1_a, Mv2_a, xs_a = np.genfromtxt (this_file+"xs_pp_v1v2j_Delta=1.dat",dtype=float,unpack=True,skip_header=True) 
Mv1_b, Mv2_b, xs_b = np.genfromtxt (this_file+"xs_pp_v1v2j_Delta=10.dat",dtype=float,unpack=True,skip_header=True) 
Mv1_c, Mv2_c, xs_c = np.genfromtxt (this_file+"xs_pp_v1v2j_Delta=100.dat",dtype=float,unpack=True,skip_header=True) 

Mv1_CM, Mv2_CM, xs_CM, r_CM, Acc_CM, SR_CM, ds_CM, Sobs_CM, xs_lim_CM = np.genfromtxt (this_file+"CM_xs_pp_v1v2j_delta=1.dat",dtype=float,unpack=True,skip_header=True) 


#Interpolation of the CheckMATE analysis
Mv = np.linspace(100,400,100)
SIG_LIM_CMb = interp1d(Mv1_CM, xs_lim_CM, kind='linear')
SIGb = SIG_LIM_CMb(Mv) 

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=13)
#Name of axes 
plt.title("$\\sigma(pp\\rightarrow V_1V_2j)$ (fb) at 13 TeV",fontsize=14)
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow V_1V_2j)$ (fb) with $P_T^{jet} > 200$ GeV", fontsize=14)
plt.xlim(100,400)
#plt.ylim(0.0000001,4000)
plt.yscale('log')

plt.plot(Mv1_a, xs_a, linestyle='--',color='b',linewidth=2, label="$\\Delta M = 1$ GeV")
plt.plot(Mv1_b, xs_b, linestyle='--',color='g',linewidth=2, label="$\\Delta M = 10$ GeV")
plt.plot(Mv1_c, xs_c, linestyle='--',color='m',linewidth=2, label="$\\Delta M = 100$ GeV")
plt.plot(Mv, SIGb, linestyle='-',color='r',linewidth=2, label="95% CL $ ( 36.1 fb^{-1} )$")

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True, fontsize = 10,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('CM_limit_v1v2j_13TeV.pdf')
plt.clf()


#Read the data file and save it in the variables
#Cross sections files
Mv1a_14, lamL_1, xsa_14 = np.genfromtxt (this_file+"pp_v1v1j_14TeV_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b_14, lamL_5, xsb_14 = np.genfromtxt (this_file+"pp_v1v1j_14TeV_lamL=5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1c_14, lamL_10, xsc_14 = np.genfromtxt (this_file+"pp_v1v1j_14TeV_lamL=10.dat", dtype=float, unpack=True, skip_header=True) 

## Recast cross section limit for high luminosities
xs_bkg13 = 49.32
xs_bkg14 = 57.230
lum = 36.1
lum_100 = 100
lum_3000 = 3000

XS_MJ14_36 = SIGa*np.sqrt(xs_bkg14/xs_bkg13)#*np.sqrt(lum/lum)
XS_MJ14_100 = SIGa*np.sqrt(xs_bkg14/xs_bkg13)*np.sqrt(lum/lum_100)
XS_MJ14_3000 = SIGa*np.sqrt(xs_bkg14/xs_bkg13)*np.sqrt(lum/lum_3000)

#print (XS_MJ14_36, SIGb)

fig = plt.subplots()
plt.tick_params(axis='both',labelsize=13)
#Name of axes 
plt.title("$\\sigma(pp\\rightarrow V_1V_1j)$ (fb) at 14 TeV",fontsize=14)
plt.xlabel("Mv$_1$ (GeV)", fontsize=15)
plt.ylabel("$\\sigma(pp\\rightarrow V_1V_1j)$ (fb) with $P_T^{jet} > 200$ GeV", fontsize=14)
#plt.title('$\\sigma(pp\\rightarrow h_1h_1j)$ (fb) at 8 TeV', fontsize=25,y=1.02)
plt.xlim(100,400)
#plt.ylim(0.0000001,4000)
plt.yscale('log')

plt.plot(Mv1a_14, xsa_14, linestyle='--',color='b',linewidth=2, label="$\\lambda_{L}=1$")
plt.plot(Mv1b_14, xsb_14, linestyle='--',color='g',linewidth=2, label="$\\lambda_{L}=5$")
plt.plot(Mv1c_14, xsc_14, linestyle='--',color='m',linewidth=2, label="$\\lambda_{L}=10$")
plt.plot(Mv1a, XS_MJ14_36, linestyle='-',color='r',linewidth=2, label="95% CL $( 36.1 fb^{-1} )$")
plt.plot(Mv1a, XS_MJ14_100, linestyle='-',color='m',linewidth=2, label="95% CL $( 100 fb^{-1} )$")
plt.plot(Mv1a, XS_MJ14_3000, linestyle='-',color='k',linewidth=2, label="95% CL $( 3000 fb^{-1} )$")

plt.legend(loc="lower left", handlelength=2,borderaxespad=0.1,fancybox=True, shadow=True, fontsize = 10,labelspacing=0.1,handletextpad=0.1)

plt.grid()
plt.tight_layout()
plt.savefig('CM_limit_v1v1j_14TeV.pdf')
plt.clf()


