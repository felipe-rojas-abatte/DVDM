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
from itertools import izip

current_dir = os.getcwd()
this_file = current_dir+'/data/'

f14 = open('pp_v1v1j_14TeV_xslim.dat','w')
f14.write('Mv1      lamL   xs_14TeV    xs_lim_36.1(fb)    xs_lim_100(fb)    xs_lim_3000(fb)\n')

## Recast cross section limit for high luminosities
xs_bkg13 = 49.32
xs_bkg14 = 57.230
lum = 36.1
lum_100 = 100
lum_3000 = 3000

EX_lim_CM = this_file+'Exclusion_limits_from_pp_v1v1j.dat'
sig14 = this_file+'pp_v1v1j_14TeV.dat'

EXCM = open(EX_lim_CM,'r')
SIG14 = open(sig14,'r')

lines1 = EXCM.readlines()[1:]
lines2 = SIG14.readlines()[1:]

for i,j in zip(lines1,lines2):
   read1 = i.split()
   read2 = j.split()

   Mv1 = float(read1[0])
   lamL = float(read1[1])
   xs_lim13 = float(read1[8]) #xs lim at 13 TeV
   xs_14 = float(read2[2])

  # print Mv1, lamL, xs_lim13, xs_14
## recast of Cross section limit at 14 TeV for different luminosities
   XS_MJ14_36 = xs_lim13*np.sqrt(xs_bkg14/xs_bkg13)*np.sqrt(lum/lum)
   XS_MJ14_100 = xs_lim13*np.sqrt(xs_bkg14/xs_bkg13)*np.sqrt(lum/lum_100)
   XS_MJ14_3000 = xs_lim13*np.sqrt(xs_bkg14/xs_bkg13)*np.sqrt(lum/lum_3000)
   
   f14.write('{:.1f}    {:.2f}       {:.2f}          {:.2f}             {:.2f}             {:.2f}\n'.format(Mv1,lamL,xs_14,XS_MJ14_36,XS_MJ14_100,XS_MJ14_3000))

EXCM.close()
SIG14.close()
f14.close()

