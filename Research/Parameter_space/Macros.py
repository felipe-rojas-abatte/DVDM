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
exec(open('cuts.py').read())

# Abro archivo con graficos

######################
# plot_set:
#   0 = No cuts
#   1 = 0 + Perturbativity
#   2 = 1 + LEP limits 
#   3 = 2 + Invisible Braching
#   4 = 3 + Diphoton Higgs decay 13 TeV
#   5 = 4 + Upper PLANCK limit
#   6 = 5 + LUX limits
#   7 = 6 + XENON limits
#   8 = 7 + Unitarity constraints
#   10 = 8 + Lower PLANCK limit    


plot_set=2

print('----------------------')
print('  Generating plots:')
print('----------------------')

if plot_set==0:
	cut=cut0
	excluded_region=1
	cuts='no_cuts'
	print('	Generating plots with no cuts \n')
	exec(open('plots.py').read())

#########################
#Theoretical constraints#
#########################

if plot_set==0:
	cut=cut0&cut1 
	excluded_region=0
	cuts='cut1'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity\n')
	exec(open('plots.py').read())

##############################
#Experimantal LHC constraints#
##############################

if plot_set==0:
	cut=cut0&cut1&cut2
	excluded_region=0
	cuts='cut12'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3
	excluded_region=0
	cuts='cut123'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4
	excluded_region=0
	cuts='cut1234'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV\n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5
	excluded_region=0
	cuts='cut12345'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV\n')
	print('	   - Upper PLANCK limit \n')
	exec(open('plots.py').read())

######################################
#Experimantal Dark Matter constraints#
######################################

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6
	excluded_region=0
	cuts='cut123456'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit ')
	print('	   - LUX limits \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7
	excluded_region=0
	cuts='cut1234567'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&CahV
	excluded_region=0
	cuts='cut12345678a'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	print('	   - Unitarity constraints:')
	print('	   	a) Channel HV->HV: \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&CahV&CaCC
	excluded_region=0
	cuts='cut12345678ab'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	print('	   - Unitarity constraints:')
	print('	   	a) Channel HV->HV: ')
	print('	   	b) Channel VCVC->VCVC: \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&cut_unit
	excluded_region=0
	cuts='cut12345678abc'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	print('	   - Unitarity constraints:')
	print('	   	a) Channel HV->HV: ')
	print('	   	b) Channel VCVC->VCVC: ')
	print('	   	c) Channel GV->GV: \n')
	exec(open('plots.py').read())

if plot_set==0:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&cut10    
        #excluded_region=0 
	cut='cut123456710'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	#print('	   - Unitarity constraints: ')
	#print('	   	a) Channel HV->HV: ')
	#print('	   	b) Channel VCVC->VCVC: ')
	print('	   - Lower PLANCK limit    \n')
	exec(open('plots_sat.py').read())

if plot_set==0:
	cut=cut0&cut4 
	excluded_region=0
	cuts='estudio'
	print('	Generating plots with '+cuts+': ')
	exec(open('plots_region.py').read())

################################################
############ Zone of Saturation ################
################################################

if plot_set==1:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut5&cut10
	cuts='sat_cut12510'
	print('	Generating plots with '+cuts+': ')
	print('	   - PLANCK ')
	print('	   - Perturbativity')
	print('	   - LEP limits \n ')
	exec(open('plots_sat.py').read())

if plot_set==1:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut3&cut5&cut10
	cuts='sat_cut123510'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching \n')
	exec(open('plots_sat.py').read())

if plot_set==1:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut3&cut4&cut5&cut10
	cuts='sat_cut1234510'
	print('	Generating plots with '+cuts+': ')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV\n')
	exec(open('plots_sat.py').read())

if plot_set==1:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut5&cut7&cut10
	cuts='sat_cut15710'
	print('	Generating plots with '+cuts+': ')
	print('	   - PLANCK ')
	print('	   - Perturbativity')
	print('	   - DD \n ')
	exec(open('plots_sat.py').read())

if plot_set==2:
	cut_A=cut0&cut5&cut10 #PLANCK
	cut_B=cut0&cut1&cut2&cut5&cut10 #Pert, LEP, PLANCK
	cut_C=cut0&cut1&cut2&cut3&cut5&cut10 #Pert, LEP, PLANCK, Inv Higgs
	cut_D=cut0&cut1&cut2&cut3&cut5&cut7&cut10 #Pert, LEP, PLANCK, Inv Higgs, DD
	cut_E=cut0&cut1&cut2&cut3&cut4&cut5&cut7&cut10 #Pert, LEP, PLANCK, Inv Higgs, DD, HAA
	cuts='sat_color'
	print('	Generating plots with '+cuts+': ')
	exec(open('plot_sat_color.py').read())


######################################
#Experimantal Dark Matter constraints#
######################################

if plot_set==0:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut10
	cuts='sat_cut12345610'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit ')
	print('	   - LUX limits \n')
	exec(open('plots_sat.py').read())

if plot_set==0:
	cut_planck=cut0&cut5&cut10
	cut_todo=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&cut10
	cuts='sat_cut123456710'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits \n')
	exec(open('plots_sat.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&CahV
	excluded_region=0
	cuts='sat_cut12345678a'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	print('	   - Unitarity constraints:')
	print('	   	a) Channel HV->HV: \n')
	exec(open('plots_sat.py').read())

if plot_set==0:
	cut=cut0&cut1&cut2&cut3&cut4&cut5&cut6&cut7&CahV&CaCC
	excluded_region=0
	cuts='sat_cut12345678ab'
	print('	Generating plots with '+cuts+': ')
	print('	   - Neutral Dark Matter')
	print('	   - Perturbativity')
	print('	   - LEP limits  ')
	print('	   - Higgs Invisible Braching')
	print('	   - Diphoton Higgs decay 13 TeV ')
	print('	   - Upper PLANCK limit')
	print('	   - LUX limits')
	print('	   - XENON limits')
	print('	   - Unitarity constraints:')
	print('	   	a) Channel HV->HV: ')
	print('	   	b) Channel VCVC->VCVC: \n')
	exec(open('plots_sat.py').read())



print('------------------------')
print('  Done !!!')
print('------------------------')
plt.clf()

