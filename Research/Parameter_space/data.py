#Data micrOMEGAs information
current_dir = os.getcwd()
this_file = current_dir+'/data/'

#scan of the parameter space
t1 = np.genfromtxt(this_file+'scan_rand_2M.gz', dtype=float,unpack=True,skip_header=True)
t2 = np.genfromtxt(this_file+'scan_rand_5M.gz', dtype=float,unpack=True,skip_header=True)
#t3 = np.genfromtxt(this_file+'scan_rand_sat.dat',dtype=float,unpack=True,skip_header=True)
#t4 = np.genfromtxt(this_file+'sat_points.dat',dtype=float,unpack=True,skip_header=True)

#Put all the data together in one file
#tc = np.hstack((t1,t2,t3))
tc = np.hstack((t1,t2))

# save informatio in variables
(Mv1, Mv2, Mvp, lamL, alpha2, alpha3, omega, prot, Brv1, Brv2 , Brvpm, BrHAA, WH) = tc

#Data with Direct Detection limits (LUX experiment)
(MDM_L,SIG_L)=np.genfromtxt(this_file+'LUX.dat',dtype=float,unpack=True,skip_header=False)
LUX_SIG=interp1d(MDM_L, SIG_L, kind='linear')
LUX=LUX_SIG(Mv1)

#Data with Direct Detection limits (XENON1T experiment)
(MDM_X,SIG_X)=np.genfromtxt(this_file+'XENON1T.dat',dtype=float,unpack=True,skip_header=False)
XENON_SIG=interp1d(MDM_X, SIG_X, kind='linear')
XENON=XENON_SIG(Mv1)
