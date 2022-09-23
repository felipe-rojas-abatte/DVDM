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
this_file = current_dir+'/'

Mh1a, lamLa, csh1a = np.genfromtxt(this_file+"pp_h1h1j_ld345=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1a, lamLa, csv1a = np.genfromtxt(this_file+"pp_v1v1j_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1b, Mh2b, csh1b = np.genfromtxt(this_file+"pp_h1h2j_DeltaM=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1b, Mv2b, csv1b = np.genfromtxt(this_file+"pp_v1v2j_DeltaM=1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1c, Mh2c, ld345c, csh1c = np.genfromtxt(this_file+"pp_h1h1Z_DtM=1_ld345=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1c, Mv2c, lamLc, csv1c = np.genfromtxt(this_file+"pp_v1v1Z_DtM=1_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 
Mh1d, ld345d, csh1d = np.genfromtxt(this_file+"pp_h1h1H_ld345=1.dat", dtype=float, unpack=True, skip_header=True) 
Mv1d, lamLd, csv1d = np.genfromtxt(this_file+"pp_v1v1H_lamL=1.dat", dtype=float, unpack=True, skip_header=True) 

##############################################################
## comparison between cross sections for differente process ##
##############################################################

ax = plt.subplot(111)
#Name of axes
plt.xlabel("M$_{DM}$ (GeV)",fontsize=15)
plt.ylabel("$\\sigma$ (fb)",fontsize=15)
plt.title("Mono-X ($jet,Z,H$) total cross (fb) section at LHC@13TeV", fontsize=10) 
plt.xlim(65,1000)
plt.ylim(1E-5,1E5)
plt.yscale('log') 
#plt.xscale('log') 
plt.grid()

cs1, = plt.plot(Mv1a, csv1a, label='$pp\\rightarrow V_1V_1j$ $(\\lambda_L=1)$', color='r', linestyle='-')
cs2, = plt.plot(Mh1a, csh1a, label='$pp\\rightarrow h_1h_1j$ $(\\lambda_{345}=1)$', color='r', linestyle='-.')
cs3, = plt.plot(Mv1b, csv1b, label='$pp\\rightarrow V_1V_2j$ $(\\Delta M=1 GeV)$', color='b', linestyle='-')
cs4, = plt.plot(Mh1b, csh1b, label='$pp\\rightarrow h_1h_2j$ $(\\Delta M=1 GeV)$', color='b', linestyle='-.')
cs5, = plt.plot(Mv1c, csv1c, label='$pp\\rightarrow V_1V_1Z$ $(\\Delta M=1 GeV)$ \n $(\\lambda_L=1)$', color='g', linestyle='-')
cs6, = plt.plot(Mh1c, csh1c, label='$pp\\rightarrow h_1h_1Z$ $(\\Delta M=1 GeV)$ \n $(\\lambda_{345}=1)$', color='g', linestyle='-.')
cs7, = plt.plot(Mv1d, csv1d, label='$pp\\rightarrow V_1V_1H$ $(\\lambda_L=1)$', color='m', linestyle='-')
cs8, = plt.plot(Mh1d, csh1d, label='$pp\\rightarrow h_1h_1H$ $(\\lambda_{345}=1)$', color='m', linestyle='-.')

#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#ax.get_position(1,1,1,1)

#Creamos la primera leyenda
legend1b = plt.legend(handles=[cs2,cs4,cs6,cs8,cs1,cs3,cs5,cs7], loc="upper right",title=" i2HDM                            DVDM", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1)#,  bbox_to_anchor=(1.4, 0.5))

#legend2c = plt.legend(handles=[NDD1,NDD2,NDD3,NDD4,NDD5,NDD6,NDD7,NDD8,NDD9,NDD10], loc="upper right", ncol=2, handlelength=2.5, borderaxespad=0.1, fancybox=True, shadow=True, fontsize = 8, labelspacing=0.1, handletextpad=0.1) # bbox_to_anchor=(1.5, 1.2))

#Agregamos la primera leyenda
plt.gca().add_artist(legend1b)

plt.savefig('cross_sections.pdf')

plt.clf()
