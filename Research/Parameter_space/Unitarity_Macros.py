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

# Abro archivo con base de datos
print('Reading data files')
exec(open('data.py').read())

# Abro archivo con cortes
print('Reading cuts file')
exec(open('Unitarity_cuts.py').read())

# Abro archivo con graficos

######################
# plot_set:
#   1 = Channel H V1 -> H V1
#   2 = Channel H V2 -> H V2
#   3 = Channel H VC -> H VC
#   4 = Channel WL WL -> v1 v2
#   5 = Channel H H -> v1 v1
#   6 = Channel H H -> v2 v2

plot_set=1

print('----------------------')
print('  Generating plots:')
print('---------------------- \n')

#########################
#### Ondas parciales ####
#########################

if plot_set==1:
	cut1=OK01
	cut2=EXC01
	cuts='HV1->HV1'
	print('	Channel H V1 -> H V1 \n')
	exec(open('Unitarity_plots.py').read())

if plot_set==1:
	cut1=OK02
	cut2=EXC02
	cuts='HV2->HV2'
	print(' Channel H V2 -> H V2 \n')
	exec(open('Unitarity_plots.py').read())

if plot_set==1:
	cut1=OK03
	cut2=EXC03
	cuts='HVC->HVC'
	print(' Channel H VC -> H VC \n')
	exec(open('Unitarity_plots.py').read())

#if plot_set==1:
#	cut1=Ca04
#	cut2=CA04
#	cuts='WW->V1V2'
#	print(' Channel WL WL -> V1 V2 \n')
#	exec(open('Unitarity_plots.py').read())

#if plot_set==1:
#	cut1=Ca05
#	cut2=CA05
#	cuts='HH->V1V1'
#	print(' Channel H H -> V1 V1 \n')
#	exec(open('Unitarity_plots.py').read())

#if plot_set==1:
#	cut1=Ca06
#	cut2=CA06
#	cuts='HH->V2V2'
#	print(' Channel H H -> V2 V2 \n')
#	exec(open('Unitarity_plots.py').read())

print('------------------------')
print('  Done !!!')
print('------------------------')
plt.clf()

