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

##### Define functions  #####

def create_dir(dir_name):
    if not os.path.exists(dir_name):	
       os.mkdir(dir_name)	
       print 'Directory',dir_name,' created' 
    else: 	
       print 'Directory',dir_name,' already existe' 

def uncompress(file_name):
    if not os.path.exists(file_name):
	print 'file: ',file_name,' do not exist' 
	quit()	
    else: 	
	os.system('gunzip '+file_name)

##############################

################
### Programs ###
################

CalcHEP = True
CheckMATE = True

########################
###### Main loop #######
########################

fsig = open('Exclusion_limits_from_pp_v1v1j_more.dat','w')
fsig.write('Mv1      lamL      xs(fb)          r      Acc     SR         ds         Sobs      xs_lim(fb)\n')

for Mv1 in range(450,511,10):  
 for lamL in range(1,13,1):
  print
  print '\n ======== New point ========= \n'
  print 'Mv1 = {}   laml = {} '.format(Mv1, lamL)

  ## Parametros
  fold_name = 'pp_v1v1j'
  fold_dir  = fold_name+'/'
  programas = '/home/felipe/Documents/Programas/'
  cHEP_dir  = programas+'micromegas_4.3.5/VDDMM/work/'
  Check_dir = programas+'CheckMATE-2.0.26/'
  Check_work= Check_dir+'bin/'+fold_dir

## Initial data of the process
  energy = 6500
  n_events = 10000
  lum = 36.1

  if CalcHEP:
	## Generate the batch file with the information of the process
	name = 'batch_'+fold_name
	batch = './calchep_batch '+name

	## Creation of the batch file for CalcHEP
	f1 = open(name,'w')
	f1.write('Model: VDDM \n')
	f1.write('Model changed: False \n')
	f1.write('Gauge: unitary \n\n')

	f1.write('Process: p,p->~v1,~v1,jet \n')
	f1.write('Composite: p=u,U,d,D,c,C,s,S,b,B,G \n')
	f1.write('Composite: jet=u,U,d,D,c,C,s,S,b,B,G \n\n')

	f1.write('pdf1: PDT:NNPDF23_lo_as_0130_qed (proton)\n')
	f1.write('pdf2: PDT:NNPDF23_lo_as_0130_qed (proton)\n\n')

	f1.write('p1: {} \n'.format(energy))
	f1.write('p2: {} \n\n'.format(energy))

	f1.write('Parameter: Mv1={} \n'.format(Mv1)) 
	f1.write('Parameter: Mv2=1000 \n') 
	f1.write('Parameter: Mvp=1000 \n') 
	f1.write('Parameter: lamL={} \n'.format(lamL))
	f1.write('Parameter: alpha2=1 \n' ) 
	f1.write('Parameter: alpha3=-1 \n\n' ) 

	f1.write('alpha Q: sqrt(S34 + T5^2) + T5 \n\n')

	f1.write('Cut parameter: T(jet) \n')
	f1.write('Cut invert: False \n')
	f1.write('Cut min: 200 \n\n')

	f1.write('Number of events (per run step): {} \n'.format(n_events))
	f1.write('Filename: {} \n'.format(fold_name))
	f1.write('NTuple: False\n')
	f1.write('Cleanup: False\n')
	f1.write('Parallelization method: local\n')
	f1.write('Max number of nodes: 8\n')
	f1.write('Max number of processes per node: 1\n')
	f1.write('sleep time: 3\n')
	f1.write('nice level: 19\n')
	f1.write('nSess_1: 5\n')
	f1.write('nCalls_1: 100000\n')
	f1.write('nSess_2: 5\n')
	f1.write('nCalls_2: 100000\n')

	f1.close()

	print '\n====================== \n Executing batch file \n====================== \n'
	print 'Inputs: '
	print 'Energy =',2*energy, 'GeV'
	print 'N Events =',n_events
  
	os.system(batch)
      
	######### store the cross section #########
	cHEP_num = cHEP_dir+'html/numerical.txt'

	numFile = open(cHEP_num,'r')
	lines = numFile.readlines()
	for i,line in enumerate(lines):
		if i==5:	
		   read = line.split()
	sig = read[1]

	print 'Cross section = {} (fb)\n'.format(sig)
	numFile.close()

	######## Descomprime archivo .lhe #######
	cHEP_events = cHEP_dir+'batch_results/'+fold_name+'-single.lhe.gz'
	uncompress(cHEP_events)

  if CheckMATE:
	create_dir(Check_work)
	lhe = cHEP_dir+'batch_results/'+fold_name+'-single.lhe'
	cp_lhe = 'cp '+lhe+' '+Check_work+fold_name+'.lhe'
	Check_lhe = Check_work+fold_name+'.lhe'
	Check_pyt = Check_work+'pythia8card.in'

	os.system(cp_lhe)
	
	## create pythia8card.in
	fpyt = open(Check_work+'pythia8card.in','w')	
	fpyt.write('Main:numberOfEvents = {} \n'.format(n_events))
	fpyt.write('Main:timesAllowErrors = 3 \n\n')

	fpyt.write('Init:showChangedSettings = on \n')
	fpyt.write('Init:showAllSettings = off \n')
	fpyt.write('Init:showChangedParticleData = on \n')
	fpyt.write('Init:showAllParticleData = off \n')
	fpyt.write('Next:numberCount = 1000 \n')
	fpyt.write('Next:numberShowInfo = 2 \n')
	fpyt.write('Next:numberShowProcess = 100 \n')
	fpyt.write('Next:numberShowEvent = 2 \n\n')

	fpyt.write('Beams:frameType = 4 \n')
	fpyt.write('Beams:LHEF = {} \n'.format(Check_lhe))
	fpyt.close()


	## create file .dat
	fdat = open(Check_work+fold_name+'.dat','w') 

	fdat.write('## General Options \n')
	fdat.write('[Parameters] \n')
	fdat.write('Name: {} \n'.format(fold_name))
	fdat.write('Analyses: atlas_conf_2017_060 \n')
	fdat.write('SkipParamCheck: True \n')
	fdat.write('OutputExists: overwrite \n')
	fdat.write('WriteDelphesEvents: True \n\n')

	fdat.write('## Process Information (Each new process X must start with [X]) \n')
	fdat.write('['+fold_name+'@13TeV]  \n')
	fdat.write('Pythia8Card: {} \n'.format(Check_pyt))
	fdat.close()

	print '\n======================== \n Executing CheckMATE \n======================== \n\n'
	Check_exe = Check_dir+'bin/'+'CheckMATE '+Check_work+fold_name+'.dat'
	os.system(Check_exe)

	BSR_file = Check_dir+'results/'+fold_name+'/evaluation/best_signal_regions.txt'
	## Leyendo archivo best signal region
	BSR = open(BSR_file,'r')
	lines = BSR.readlines()
	for i,line in enumerate(lines):
		if i==1:	
		   read2 = line.split()

	sr = read2[1]
	ds = read2[6]
	sobs = read2[7]
	r = read2[9]

	Acc_file = Check_dir+'results/'+fold_name+'/analysis/pp_v1v1j@13TeV_atlas_conf_2017_060_signal.dat'
	ACC = open(Acc_file,'r')
	lines = ACC.readlines()
	for i,line in enumerate(lines):
		if i>=11:
		  read3 = line.split()
		  if(read3[0] == sr): Acc = read3[3]
		  else: continue

	ds = float(ds)
	sobs = float(sobs)
	r = float(r)
	Acc = float(Acc)
	lum = float(lum)

	xs_lim = (sobs + 1.64*ds)/(lum*Acc)

	##### guardo seccion eficaz en fsig	

	fsig.write('{:.1f}    {:.2f}    {}    {:.3e}     {:.2f}    {}      {:.3f}      {:.2f}      {:.2f}\n'.format(Mv1,lamL,sig,r,Acc,sr,ds,sobs,xs_lim))

	BSR.close()
	ACC.close()	

#  fsig.close()

