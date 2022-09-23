# Program that generate plots for Relic density, Rescaled Direct Detection and Rescaled Indirect Detection limits as a function of Dark Matter mass considering different values of lambda_L parameter. The program read the information contained on the folder "data" and generate plots for 2 scenarios: quasi-degenerate when Mv2 = Mvp = Mv1 + 1 GeV and non-degenerate when Mv2 = Mvp = Mv1 + 100 GeV

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import interp1d
import sys
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter
import os

current_dir = os.getcwd()
this_file = current_dir+'/data/'

#Data with Direct Detection limits (LUX experiment)
(MDM,SIG)=np.genfromtxt(this_file+'LUX.dat', dtype=float,unpack=True,skip_header=False) 
LUX_SIG=interp1d(MDM, SIG, kind='linear')

#Data with Direct Detection limits (XENON1T experiment)
(MDM2,SIG2)=np.genfromtxt(this_file+'XENON1T.dat', dtype=float,unpack=True,skip_header=False) 
XENON_SIG=interp1d(MDM2, SIG2, kind='linear')

#Data with Indirect Detection limits (HESS experiment)
(MDM3,SIGV)=np.genfromtxt(this_file+'HESS_Einasto.dat', dtype=float,unpack=True,skip_header=True) 
HESS_Ei=interp1d(MDM3, SIGV, kind='linear')
(MDM4,SIGV2)=np.genfromtxt(this_file+'HESS_Einasto2.dat', dtype=float,unpack=True,skip_header=True) 
HESS_Ei2=interp1d(MDM4, SIGV2, kind='linear')

#Data with Indirect Detection limits (Fermi-Lat experiment)
(MDM5,SIG5)=np.genfromtxt(this_file+'Fermi-LAT.dat', dtype=float,unpack=True,skip_header=True) 
Fermi_Ei=interp1d(MDM5, SIG5, kind='linear')

#Data with Indirect Detection limits (PlanckCMB experiment)
(MDM6,SIG6)=np.genfromtxt(this_file+'PlanckCMB.dat', dtype=float,unpack=True,skip_header=True) 
PlanckCMB=interp1d(MDM6, SIG6, kind='linear')

#Data with Indirect Detection limits (AMS02 experiment)
(MDM7,SIG7)=np.genfromtxt(this_file+'AMS02.dat', dtype=float,unpack=True,skip_header=True) 
AMS02=interp1d(MDM7, SIG7, kind='linear')

#PLANCK measurements
Mv = np.linspace(10, 2000, 1000)
#lim_inf = np.linspace(0.1172,0.1172,100)
omega = np.linspace(0.1184,0.1184,1000)
#lim_sup = np.linspace(0.1196,0.1196,100)

Mv_LEP = np.linspace(45, 45, 1000)
omega_LEP = np.linspace(1E-7,1E3,1000)
omega_LEP_DD = np.linspace(1E-15,1E-3,1000)

Mv_HESS = np.linspace(200, 2000, 1000)
Mv_rest = np.linspace(80, 2000, 1000)
#Read data for quasi-degenerate values of Masses
Mv1a, Mv2a, Mvpa, lamLa, Omegaa, prota, sva, Brv1a, Brv2a, Brvpa, BrhAAa, WHa = np.genfromtxt(this_file+"deg_lamL=5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b, Mv2b, Mvpb, lamLb, Omegab, protb, svb, Brv1b, Brv2b, Brvcb, BrhAAb, WHb = np.genfromtxt(this_file+"deg_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1c, Mv2c, Mvpc, lamLc, Omegac, protc, svc, Brv1c, Brv2c, Brvcc, BrhAAc, WHc = np.genfromtxt(this_file+"deg_lamL=0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1d, Mv2d, Mvpd, lamLd, Omegad, protd, svd, Brv1d, Brv2d, Brvcd, BrhAAd, WHd = np.genfromtxt(this_file+"deg_lamL=0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mv1e, Mv2e, Mvpe, lamLe, Omegae, prote, sve, Brv1e, Brv2e, Brvpe, BrhAAe, WHe = np.genfromtxt(this_file+"deg_lamL=0.001.dat", dtype=float, unpack=True, skip_header=True) 
Mv1f, Mv2f, Mvpf, lamLf, Omegaf, protf, svf, Brv1f, Brv2f, Brvcf, BrhAAf, WHf = np.genfromtxt(this_file+"deg_lamL=-5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1g, Mv2g, Mvpg, lamLg, Omegag, protg, svg, Brv1g, Brv2g, Brvcg, BrhAAg, WHg = np.genfromtxt(this_file+"deg_lamL=-1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1h, Mv2h, Mvph, lamLh, Omegah, proth, svh, Brv1h, Brv2h, Brvch, BrhAAh, WHh = np.genfromtxt(this_file+"deg_lamL=-0.1.dat", dtype=float, unpack=True, skip_header=True)
Mv1ha, Mv2ha, Mvpha, lamLha, Omegaha, protha, svha, Brv1ha, Brv2ha, Brvcha, BrhAAha, WHha = np.genfromtxt(this_file+"deg_lamL=-0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mv1hb, Mv2hb, Mvphb, lamLhb, Omegahb, prothb, svhb, Brv1hb, Brv2hb, Brvchb, BrhAAhb, WHhb = np.genfromtxt(this_file+"deg_lamL=-0.001.dat", dtype=float, unpack=True, skip_header=True)  

#Read data for no-degenerate values of Masses
Mv1i, Mv2i, Mvpi, lamLi, Omegai, proti, svi, Brv1i, Brv2i, Brvpi, BrhAAi, WHi = np.genfromtxt(this_file+"nodeg_lamL=5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1j, Mv2j, Mvpj, lamLj, Omegaj, protj, svj, Brv1j, Brv2j, Brvcj, BrhAAj, WHj = np.genfromtxt(this_file+"nodeg_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1k, Mv2k, Mvpk, lamLk, Omegak, protk, svk, Brv1k, Brv2k, Brvck, BrhAAk, WHk  = np.genfromtxt(this_file+"nodeg_lamL=0.1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1l, Mv2l, Mvpl, lamLl, Omegal, protl, svl, Brv1l, Brv2l, Brvcl, BrhAAl, WHl  = np.genfromtxt(this_file+"nodeg_lamL=0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mv1m, Mv2m, Mvpm, lamLm, Omegam, protm, svm, Brv1m, Brv2m, Brvpm, BrhAAm, WHm  = np.genfromtxt(this_file+"nodeg_lamL=0.001.dat", dtype=float, unpack=True, skip_header=True) 
Mv1n, Mv2n, Mvpn, lamLn, Omegan, protn, svn, Brv1n, Brv2n, Brvcn, BrhAAn, WHn  = np.genfromtxt(this_file+"nodeg_lamL=-5.dat", dtype=float, unpack=True, skip_header=True) 
Mv1o, Mv2o, Mvpo, lamLo, Omegao, proto, svo, Brv1o, Brv2o, Brvco, BrhAAo, WHo = np.genfromtxt(this_file+"nodeg_lamL=-1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1p, Mv2p, Mvpp, lamLp, Omegap, protp, svp, Brv1p, Brv2p, Brvcp, BrhAAp, WHp = np.genfromtxt(this_file+"nodeg_lamL=-0.1.dat", dtype=float, unpack=True, skip_header=True)
Mv1q, Mv2q, Mvpq, lamLq, Omegaq, protq, svq, Brv1q, Brv2q, Brvcq, BrhAAq, WHq = np.genfromtxt(this_file+"nodeg_lamL=-0.01.dat", dtype=float, unpack=True, skip_header=True) 
Mv1r, Mv2r, Mvpr, lamLr, Omegar, protr, svr, Brv1r, Brv2r, Brvcr, BrhAAr, WHr = np.genfromtxt(this_file+"nodeg_lamL=-0.001.dat", dtype=float, unpack=True, skip_header=True) 

# Rescaling of the spin independent cross section
LUX=LUX_SIG(Mv)
XENON=XENON_SIG(Mv)

prot_a = ((Omegaa/0.112)*prota)
prot_b = ((Omegab/0.112)*protb)
prot_c = ((Omegac/0.112)*protc)
prot_d = ((Omegad/0.112)*protd)
prot_e = ((Omegae/0.112)*prote)
prot_f = ((Omegaf/0.112)*protf)
prot_g = ((Omegag/0.112)*protg)
prot_h = ((Omegah/0.112)*proth)
prot_ha = ((Omegaha/0.112)*protha)
prot_hb = ((Omegahb/0.112)*prothb)
prot_i = ((Omegai/0.112)*proti)
prot_j = ((Omegaj/0.112)*protj)
prot_k = ((Omegak/0.112)*protk)
prot_l = ((Omegal/0.112)*protl)
prot_m = ((Omegam/0.112)*protm)
prot_n = ((Omegan/0.112)*protn)
prot_o = ((Omegao/0.112)*proto)
prot_p = ((Omegap/0.112)*protp)
prot_q = ((Omegaq/0.112)*protq)
prot_r = ((Omegar/0.112)*protr)

N_LUX = LUX
N_XENON = XENON

# Rescaling the Indirect Detection signal
HESSE1=HESS_Ei(Mv_HESS)
HESSE2=HESS_Ei2(Mv_HESS)
Fermi=Fermi_Ei(Mv_HESS)
Planck=PlanckCMB(Mv_HESS)
AMS=AMS02(Mv_rest)

sv_a = ((Omegaa/0.112)*sva)
sv_b = ((Omegab/0.112)*svb)
sv_c = ((Omegac/0.112)*svc)
sv_d = ((Omegad/0.112)*svd)
sv_e = ((Omegae/0.112)*sve)
sv_f = ((Omegaf/0.112)*svf)
sv_g = ((Omegag/0.112)*svg)
sv_h = ((Omegah/0.112)*svh)
sv_ha = ((Omegaha/0.112)*svha)
sv_hb = ((Omegahb/0.112)*svhb)
sv_i = ((Omegai/0.112)*svi)
sv_j = ((Omegaj/0.112)*svj)
sv_k = ((Omegak/0.112)*svk)
sv_l = ((Omegal/0.112)*svl)
sv_m = ((Omegam/0.112)*svm)
sv_n = ((Omegan/0.112)*svn)
sv_o = ((Omegao/0.112)*svo)
sv_p = ((Omegap/0.112)*svp)
sv_q = ((Omegaq/0.112)*svq)
sv_r = ((Omegar/0.112)*svr)

N_HESS_Ei1 = HESSE1
N_HESS_Ei2 = HESSE2
Fermi1=Fermi
Planck1=Planck
AMS1=AMS

##################################################################################################
## LUX limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for quasi-degenerate case
##################################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv, N_LUX, 10 ,facecolor='palegreen', interpolate=True)
ax1.text(0.7, 0.75, 'LUX 85.3 live-days', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\hat{\\sigma}_{SI}$ (pb)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 1$ GeV", fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-15,1E-3)
plt.yscale('log') 
plt.xscale('log') 

DD1, = plt.plot(Mv1a, prot_a, label='$\lambda_L=5$',color='b', linestyle='-')
DD2, = plt.plot(Mv1b, prot_b, label='$\lambda_L=1$',color='k', linestyle='-')
DD3, = plt.plot(Mv1c, prot_c, label='$\lambda_L=0.1$',color='r', linestyle='-')
DD4, = plt.plot(Mv1d, prot_d, label='$\lambda_L=0.01$',color='m', linestyle='-')
DD5, = plt.plot(Mv1e, prot_e, label='$\lambda_L=0.001$',color='g', linestyle='-')
DD6, = plt.plot(Mv1f, prot_f, label='$\lambda_L=-5$',color='b', linestyle='--')
DD7, = plt.plot(Mv1g, prot_g, label='$\lambda_L=-1$',color='k', linestyle='--')
DD8, = plt.plot(Mv1h, prot_h, label='$\lambda_L=-0.1$',color='r', linestyle='--')
DD9, = plt.plot(Mv1ha, prot_ha, label='$\lambda_L=-0.01$',color='m', linestyle='--')
DD10, = plt.plot(Mv1hb, prot_hb, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_LUX, label='LUX',color='green',linewidth=2)

#Creamos la primera leyenda
legend1b = plt.legend(handles=[DD1,DD2,DD3,DD4,DD5,DD6,DD7,DD8,DD9,DD10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

plt.savefig('Omega_LUX_deg.pdf')

###################################################################
## Planck limits for Relic Density vs Mh1 for quasi-degenerate case
###################################################################
fig1,ax2 = plt.subplots()
ax2.axvspan(10, 44.5, alpha=0.7, color='palegreen')
ax2.text(0.15, 0.25, 'Excluded \n by LEP', verticalalignment='top', horizontalalignment='center',
        transform=ax2.transAxes, color='g', fontsize=12)

ax2.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax2.text(0.78, 0.85, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax2.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=18)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 1$ GeV',fontsize=18)
plt.yscale('log')  
plt.xscale('log')
plt.xlim(10,2000)
plt.ylim(1E-7,1E3)

DEG1, = plt.plot(Mv1a, Omegaa, label='$\lambda_L=5$',color='b',linestyle='-')
DEG2, = plt.plot(Mv1b, Omegab, label='$\lambda_L=1$',color='k',linestyle='-')
DEG3, = plt.plot(Mv1c, Omegac, label='$\lambda_L=0.1$',color='r',linestyle='-')
DEG4, = plt.plot(Mv1d, Omegad, label='$\lambda_L=0.01$',color='m',linestyle='-')
DEG5, = plt.plot(Mv1e, Omegae, label='$\lambda_L=0.001$',color='g',linestyle='--')
DEG6, = plt.plot(Mv1f, Omegaf, label='$\lambda_L=-5$',color='b',linestyle='--')
DEG7, = plt.plot(Mv1g, Omegag, label='$\lambda_L=-1$',color='k',linestyle='--')
DEG8, = plt.plot(Mv1h, Omegah, label='$\lambda_L=-0.1$',color='r',linestyle='--')
DEG9, = plt.plot(Mv1ha, Omegaha, label='$\lambda_L=-0.01$',color='m',linestyle='--')
DEG10, = plt.plot(Mv1hb, Omegahb, label='$\lambda_L=-0.001$',color='g',linestyle='--')

PLANCK, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

plt.plot(Mv_LEP, omega_LEP, linestyle='-', color='g',linewidth=2)

#Creamos la primera leyenda
legend1 = plt.legend(handles=[DEG1,DEG2,DEG3,DEG4,DEG5,DEG6,DEG7,DEG8,DEG9,DEG10], loc="upper left", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))


#Agregamos segunda leyenda
plt.legend(handles=[PLANCK], loc="lower right", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#Agregamos la primera leyenda
plt.gca().add_artist(legend1)

plt.savefig('Omega_Mv1_deg.pdf')

###############################################################################################
## LUX limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for no-degenerate case
###############################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv, N_LUX, 100000 ,facecolor='palegreen', interpolate=True)
ax1.text(0.65, 0.75, 'LUX 85.3 live-days', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\hat{\\sigma}_{SI} (pb)$",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV",fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-17,1E1)
plt.yscale('log') 
plt.xscale('log') 

NDD1, = plt.plot(Mv1i, prot_i, label='$\lambda_L=5$',color='b', linestyle='-')
NDD2, = plt.plot(Mv1j, prot_j, label='$\lambda_L=1$',color='k', linestyle='-')
NDD3, = plt.plot(Mv1k, prot_k, label='$\lambda_L=0.1$',color='r', linestyle='-')
NDD4, = plt.plot(Mv1l, prot_l, label='$\lambda_L=0.01$',color='m', linestyle='-')
NDD5, = plt.plot(Mv1m, prot_m, label='$\lambda_L=0.001$',color='g', linestyle='-')
NDD6, = plt.plot(Mv1n, prot_n, label='$\lambda_L=-5$',color='b', linestyle='--')
NDD7, = plt.plot(Mv1o, prot_o, label='$\lambda_L=-1$',color='k', linestyle='--')
NDD8, = plt.plot(Mv1p, prot_p, label='$\lambda_L=-0.1$',color='r', linestyle='--')
NDD9, = plt.plot(Mv1q, prot_q, label='$\lambda_L=-0.01$',color='m', linestyle='--')
NDD10, = plt.plot(Mv1r, prot_r, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_LUX, label='LUX',color='green',linewidth=2)

#Creamos la primera leyenda
legend2b = plt.legend(handles=[NDD1,NDD2,NDD3,NDD4,NDD5,NDD6,NDD7,NDD8,NDD9,NDD10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend2b)
plt.savefig('Omega_LUX_nodeg.pdf')

################################################################
## Planck limits for Relic Density vs Mh1 for no-degenerate case
################################################################
fig1, ax1 = plt.subplots()

ax1.fill_between(Mv, omega, 1000 ,facecolor='red', alpha=0.25,  interpolate=True)
ax1.text(0.7, 0.72, 'overabundance \n non physical', verticalalignment='top', horizontalalignment='center', transform=ax1.transAxes, color='red', fontsize=12)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("Relic Density $\\Omega h^2$",fontsize=18)
plt.title('M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV',fontsize=18)
plt.yscale('log')  #Escala logaritmica para el eje y
plt.xscale('log')
plt.xlim(10,2000)
plt.ylim(1E-7,1E3)

NDEG1, = plt.plot(Mv1i, Omegai, label='$\lambda_L=5$',color='b',linestyle='-')
NDEG2, = plt.plot(Mv1j, Omegaj, label='$\lambda_L=1$',color='k',linestyle='-')
NDEG3, = plt.plot(Mv1k, Omegak, label='$\lambda_L=0.1$',color='r',linestyle='-')
NDEG4, = plt.plot(Mv1l, Omegal, label='$\lambda_L=0.01$',color='m',linestyle='-')
NDEG5, = plt.plot(Mv1m, Omegam, label='$\lambda_L=0.001$',color='g',linestyle='-')
NDEG6, = plt.plot(Mv1n, Omegan, label='$\lambda_L=-5$',color='b',linestyle='--')
NDEG7, = plt.plot(Mv1o, Omegao, label='$\lambda_L=-1$',color='k',linestyle='--')
NDEG8, = plt.plot(Mv1p, Omegap, label='$\lambda_L=-0.1$',color='r',linestyle='--')
NDEG9, = plt.plot(Mv1q, Omegaq, label='$\lambda_L=-0.01$',color='m',linestyle='--')
NDEG10, = plt.plot(Mv1r, Omegar, label='$\lambda_L=-0.001$',color='g',linestyle='--')

PLANCK2, = plt.plot(Mv, omega, linestyle='-.', color='red', linewidth=2, label=' $\\Omega h^2$ PLANCK measurement')

#Creamos la primera leyenda
legend2 = plt.legend(handles=[NDEG1,NDEG2,NDEG3,NDEG4,NDEG5,NDEG6,NDEG7,NDEG8,NDEG9,NDEG10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend2)

#Agregamos segunda leyenda
plt.legend(handles=[PLANCK2], loc="lower left", ncol=1, handlelength=3, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 10, labelspacing=0.1, handletextpad=0.1)

#plt.legend(loc="upper right", borderaxespad=0.1)
plt.savefig('Omega_Mv1_nodeg.pdf')

##################################################################################################
#XENON limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for quasi-degenerate case
##################################################################################################
fig, ax1 = plt.subplots()
ax1.axvspan(10, 44.5, alpha=0.3, color='r')
ax1.text(0.13, 0.15, 'Excluded \n by LEP', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='r', fontsize=12)
ax1.fill_between(Mv, N_XENON, 1E-3 ,facecolor='palegreen', interpolate=True)
ax1.text(0.7, 0.7, 'XENON1T', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\hat{\\sigma}_{SI}$ (pb)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 1$ GeV",fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-15,1E-3)
plt.yscale('log') 
plt.xscale('log') 

DDX1, = plt.plot(Mv1a, prot_a, label='$\lambda_L=5$',color='b', linestyle='-')
DDX2, = plt.plot(Mv1b, prot_b, label='$\lambda_L=1$',color='k', linestyle='-')
DDX3, = plt.plot(Mv1c, prot_c, label='$\lambda_L=0.1$',color='r', linestyle='-')
DDX4, = plt.plot(Mv1d, prot_d, label='$\lambda_L=0.01$',color='m', linestyle='-')
DDX5, = plt.plot(Mv1e, prot_e, label='$\lambda_L=0.001$',color='g', linestyle='-')
DDX6, = plt.plot(Mv1f, prot_f, label='$\lambda_L=-5$',color='b', linestyle='--')
DDX7, = plt.plot(Mv1g, prot_g, label='$\lambda_L=-1$',color='k', linestyle='--')
DDX8, = plt.plot(Mv1h, prot_h, label='$\lambda_L=-0.1$',color='r', linestyle='--')
DDX9, = plt.plot(Mv1ha, prot_ha, label='$\lambda_L=-0.01$',color='m', linestyle='--')
DDX10, = plt.plot(Mv1hb, prot_hb, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_XENON, label='XENON',color='green',linewidth=2)

plt.plot(Mv_LEP, omega_LEP_DD, linestyle='-', color='r',linewidth=2)

#Creamos la primera leyenda
legend1b = plt.legend(handles=[DDX1,DDX2,DDX3,DDX4,DDX5,DDX6,DDX7,DDX8,DDX9,DDX10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

plt.savefig('Omega_XENON_deg.pdf')

###############################################################################################
##XENON limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for no-degenerate case
###############################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv, N_XENON, 100000 ,facecolor='palegreen', interpolate=True)
ax1.text(0.65, 0.7, 'XENON1T', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\hat{\\sigma}_{SI}$ (pb)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV",fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-17,1E1)
plt.yscale('log') 
plt.xscale('log') 

NDD1, = plt.plot(Mv1i, prot_i, label='$\lambda_L=5$',color='b', linestyle='-')
NDD2, = plt.plot(Mv1j, prot_j, label='$\lambda_L=1$',color='k', linestyle='-')
NDD3, = plt.plot(Mv1k, prot_k, label='$\lambda_L=0.1$',color='r', linestyle='-')
NDD4, = plt.plot(Mv1l, prot_l, label='$\lambda_L=0.01$',color='m', linestyle='-')
NDD5, = plt.plot(Mv1m, prot_m, label='$\lambda_L=0.001$',color='g', linestyle='-')
NDD6, = plt.plot(Mv1n, prot_n, label='$\lambda_L=-5$',color='b', linestyle='--')
NDD7, = plt.plot(Mv1o, prot_o, label='$\lambda_L=-1$',color='k', linestyle='--')
NDD8, = plt.plot(Mv1p, prot_p, label='$\lambda_L=-0.1$',color='r', linestyle='--')
NDD9, = plt.plot(Mv1q, prot_q, label='$\lambda_L=-0.01$',color='m', linestyle='--')
NDD10, = plt.plot(Mv1r, prot_r, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_XENON, label='XENON',color='green',linewidth=2)

#Creamos la primera leyenda
legend2c = plt.legend(handles=[NDD1,NDD2,NDD3,NDD4,NDD5,NDD6,NDD7,NDD8,NDD9,NDD10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend2c)
plt.savefig('Omega_XENON_nodeg.pdf')

##################################################################################################
#XENON limits on Direct Detection cross section Sigma_SI vs Mh1 for quasi-degenerate case
##################################################################################################
fig, ax1 = plt.subplots()
ax1.axvspan(10, 44.5, alpha=0.3, color='r')
ax1.text(0.13, 0.15, 'Excluded \n by LEP', verticalalignment='top', horizontalalignment='center',  transform=ax1.transAxes, color='r', fontsize=12)
ax1.fill_between(Mv, N_XENON, 1E-2 ,facecolor='palegreen', interpolate=True)
ax1.text(0.7, 0.7, 'XENON1T', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\sigma_{SI}$ (pb)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 1$ GeV",fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-15,1E-2)
plt.yscale('log') 
plt.xscale('log') 

DDX1, = plt.plot(Mv1a, prota, label='$\lambda_L=5$',color='b', linestyle='-')
DDX2, = plt.plot(Mv1b, protb, label='$\lambda_L=1$',color='k', linestyle='-')
DDX3, = plt.plot(Mv1c, protc, label='$\lambda_L=0.1$',color='r', linestyle='-')
DDX4, = plt.plot(Mv1d, protd, label='$\lambda_L=0.01$',color='m', linestyle='-')
DDX5, = plt.plot(Mv1e, prote, label='$\lambda_L=0.001$',color='g', linestyle='-')
DDX6, = plt.plot(Mv1f, protf, label='$\lambda_L=-5$',color='b', linestyle='--')
DDX7, = plt.plot(Mv1g, protg, label='$\lambda_L=-1$',color='k', linestyle='--')
DDX8, = plt.plot(Mv1h, proth, label='$\lambda_L=-0.1$',color='r', linestyle='--')
DDX9, = plt.plot(Mv1ha, protha, label='$\lambda_L=-0.01$',color='m', linestyle='--')
DDX10, = plt.plot(Mv1hb, prothb, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_XENON, label='XENON',color='green',linewidth=2)

#plt.plot(Mv_LEP, omega_LEP_DD, linestyle='-', color='r',linewidth=2)

#Creamos la primera leyenda
legend1b = plt.legend(handles=[DDX1,DDX2,DDX3,DDX4,DDX5,DDX6,DDX7,DDX8,DDX9,DDX10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

plt.savefig('sigma_XENON_deg.pdf')

###############################################################################################
##XENON limits on rescaled Direct Detection cross section Sigma_SI vs Mh1 for no-degenerate case
###############################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv, N_XENON, 1E-2 ,facecolor='palegreen', interpolate=True)
ax1.text(0.65, 0.7, 'XENON1T', verticalalignment='top', horizontalalignment='center',
        transform=ax1.transAxes, color='green', fontsize=18)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\sigma_{SI}$ (pb)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV",fontsize=18) 
plt.xlim(10,2000)
plt.ylim(1E-15,1E-2)
plt.yscale('log') 
plt.xscale('log') 

NDD1, = plt.plot(Mv1i, proti, label='$\lambda_L=5$',color='b', linestyle='-')
NDD2, = plt.plot(Mv1j, protj, label='$\lambda_L=1$',color='k', linestyle='-')
NDD3, = plt.plot(Mv1k, protk, label='$\lambda_L=0.1$',color='r', linestyle='-')
NDD4, = plt.plot(Mv1l, protl, label='$\lambda_L=0.01$',color='m', linestyle='-')
NDD5, = plt.plot(Mv1m, protm, label='$\lambda_L=0.001$',color='g', linestyle='-')
NDD6, = plt.plot(Mv1n, protn, label='$\lambda_L=-5$',color='b', linestyle='--')
NDD7, = plt.plot(Mv1o, proto, label='$\lambda_L=-1$',color='k', linestyle='--')
NDD8, = plt.plot(Mv1p, protp, label='$\lambda_L=-0.1$',color='r', linestyle='--')
NDD9, = plt.plot(Mv1q, protq, label='$\lambda_L=-0.01$',color='m', linestyle='--')
NDD10, = plt.plot(Mv1r, protr, label='$\lambda_L=-0.001$',color='g', linestyle='--')

plt.plot(Mv, N_XENON, label='XENON',color='green',linewidth=2)

#Creamos la primera leyenda
legend2c = plt.legend(handles=[NDD1,NDD2,NDD3,NDD4,NDD5,NDD6,NDD7,NDD8,NDD9,NDD10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend2c)
plt.savefig('sigma_XENON_nodeg.pdf')

#####################################################################################
# ID limits on rescaled Indirect Detection Sigma_V vs Mh1 for quasi-degenerate case #
#####################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv_HESS, N_HESS_Ei1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_HESS, N_HESS_Ei2, 1E-22 ,facecolor='darkgrey', interpolate=True)
ax1.fill_between(Mv_rest, Fermi1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_rest, Planck1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_rest, AMS1, 1E-22 ,facecolor='lightgrey', interpolate=True)
#ax1.text(0.8, 0.78, '$v_1v_1\\rightarrow W^+W^-$', verticalalignment='top', horizontalalignment='center',  transform=ax1.transAxes, color='k', fontsize=15)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\langle\\hat{\\sigma v}\\rangle $ (cm$^3$/s)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 1$ GeV",fontsize=18) 
plt.xlim(80,2000)
plt.ylim(1E-28,1E-23)
plt.yscale('log') 
plt.xscale('log') 

IDX1, = plt.plot(Mv1a, sv_a, label='$\lambda_L=5$',color='b', linestyle='-')
IDX2, = plt.plot(Mv1b, sv_b, label='$\lambda_L=1$',color='k', linestyle='-')
IDX3, = plt.plot(Mv1c, sv_c, label='$\lambda_L=0.1$',color='r', linestyle='-')
IDX4, = plt.plot(Mv1d, sv_d, label='$\lambda_L=0.01$',color='m', linestyle='-')
IDX5, = plt.plot(Mv1e, sv_e, label='$\lambda_L=0.001$',color='g', linestyle='-')
IDX6, = plt.plot(Mv1f, sv_f, label='$\lambda_L=-5$',color='b', linestyle='--')
IDX7, = plt.plot(Mv1g, sv_g, label='$\lambda_L=-1$',color='k', linestyle='--')
IDX8, = plt.plot(Mv1h, sv_h, label='$\lambda_L=-0.1$',color='r', linestyle='--')
IDX9, = plt.plot(Mv1ha, sv_ha, label='$\lambda_L=-0.01$',color='m', linestyle='--')
IDX10, = plt.plot(Mv1hb, sv_hb, label='$\lambda_L=-0.001$',color='g', linestyle='--')

HESS1, = plt.plot(Mv_HESS, N_HESS_Ei1, label='Einasto',color='grey',linewidth=2)
HESS2, = plt.plot(Mv_HESS, N_HESS_Ei2, label='Einasto2',color='grey',linewidth=2, linestyle='--')
Fermi, = plt.plot(Mv_rest, Fermi1, label='Fermi-LAT',color='green',linewidth=2, linestyle='-.')
Planck, = plt.plot(Mv_rest, Planck1, label='Planck CMB',color='purple',linewidth=2, linestyle='-.')
AMS, = plt.plot(Mv_rest, AMS1, label='AMS-02',color='yellow',linewidth=2, linestyle='-.')

#Creamos la primera leyenda
legend1b = plt.legend(handles=[IDX1,IDX2,IDX3,IDX4,IDX5,IDX6,IDX7,IDX8,IDX9,IDX10], loc="lower right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

legend2b = plt.legend(handles=[HESS1, HESS2, Fermi, Planck, AMS], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)
plt.gca().add_artist(legend2b)

plt.savefig('Omega_ID_deg.pdf')

###############################################################################################
##HESS limits on rescaled Indirect Detection Sigma_SI vs Mh1 for no-degenerate case
###############################################################################################
fig, ax1 = plt.subplots()
ax1.fill_between(Mv_HESS, N_HESS_Ei1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_HESS, N_HESS_Ei2, 1E-22 ,facecolor='darkgrey', interpolate=True)
ax1.fill_between(Mv_rest, Fermi1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_rest, Planck1, 1E-22 ,facecolor='lightgrey', interpolate=True)
ax1.fill_between(Mv_rest, AMS1, 1E-22 ,facecolor='lightgrey', interpolate=True)
#ax1.text(0.8, 0.78, '$v_1v_1\\rightarrow W^+W^-$', verticalalignment='top', horizontalalignment='center',  transform=ax1.transAxes, color='k', fontsize=15)

#Name of axes
plt.xlabel("Mv$_1$ (GeV)",fontsize=18)
plt.ylabel("$\\langle\\hat{\\sigma v}\\rangle$ (cm$^3$/s)",fontsize=15.5)
plt.title("M$_{V_2}$ = M$_{V^{\pm}}$ = M$_{V_1} + 100$ GeV",fontsize=18) 
plt.xlim(80,2000)
plt.ylim(1E-28,1E-23)
plt.yscale('log') 
plt.xscale('log') 

NID1, = plt.plot(Mv1i, sv_i, label='$\lambda_L=5$',color='b', linestyle='-')
NID2, = plt.plot(Mv1j, sv_j, label='$\lambda_L=1$',color='k', linestyle='-')
NID3, = plt.plot(Mv1k, sv_k, label='$\lambda_L=0.1$',color='r', linestyle='-')
NID4, = plt.plot(Mv1l, sv_l, label='$\lambda_L=0.01$',color='m', linestyle='-')
NID5, = plt.plot(Mv1m, sv_m, label='$\lambda_L=0.001$',color='g', linestyle='-')
NID6, = plt.plot(Mv1n, sv_n, label='$\lambda_L=-5$',color='b', linestyle='--')
NID7, = plt.plot(Mv1o, sv_o, label='$\lambda_L=-1$',color='k', linestyle='--')
NID8, = plt.plot(Mv1p, sv_p, label='$\lambda_L=-0.1$',color='r', linestyle='--')
NID9, = plt.plot(Mv1q, sv_q, label='$\lambda_L=-0.01$',color='m', linestyle='--')
NID10, = plt.plot(Mv1r, sv_r, label='$\lambda_L=-0.001$',color='g', linestyle='--')

HESS1, = plt.plot(Mv_HESS, N_HESS_Ei1, label='Einasto',color='grey',linewidth=2)
HESS2, = plt.plot(Mv_HESS, N_HESS_Ei2, label='Einasto2',color='grey',linewidth=2, linestyle='--')
Fermi, = plt.plot(Mv_rest, Fermi1, label='Fermi-LAT',color='green',linewidth=2, linestyle='-.')
Planck, = plt.plot(Mv_rest, Planck1, label='Planck CMB',color='purple',linewidth=2, linestyle='-.')
AMS, = plt.plot(Mv_rest, AMS1, label='AMS-02',color='yellow',linewidth=2, linestyle='-.')

#Creamos la primera leyenda
legend2c = plt.legend(handles=[NID1,NID2,NID3,NID4,NID5,NID6,NID7,NID8,NID9,NID10], loc="lower right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

legend3c = plt.legend(handles=[HESS1, HESS2, Fermi, Planck, AMS], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend2c)
plt.gca().add_artist(legend3c)
plt.savefig('Omega_ID_nodeg.pdf')

plt.clf()
