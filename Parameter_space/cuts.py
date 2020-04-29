# Excludes anomalous Relic Density points  
cut0=(omega>0)

########################
#Teoretical constraints#
########################

#--------Definition of parameters
pi=np.pi
EE=0.31343     
MZ=91.188
MW=80.385      
CW=MW/MZ 
SW=(1-CW**2)**0.5 
vv=2*MW/EE*SW
MH=125
alp=EE**2/(4*pi)
g=EE/SW

#-------Definition of lambda couplings as function of independet parameters
l2 = lamL + (2./vv**2)*(Mv1**2 - Mvp**2)
l3 = (1./vv**2)*(2*Mvp**2 - Mv1**2 - Mv2**2)
l4 = (1./vv**2)*(Mv2**2 - Mv1**2) 
MV2 = Mv1**2 + vv**2*lamL/2
lamR = l2 + l3 - l4

#########################
#Theoretical constraints#
#########################

#-------Perturbativity-------------
cut_pert=(abs(l2)<4*pi)&(abs(l3)<4*pi)&(abs(l4)<4*pi)&(alpha2<4*pi)&(alpha3<4*pi)
cut1 = cut_pert

##############################
#Experimantal LHC constraints#
##############################

#----- LEP limits
MZ=91.188 #(Z-boson mass)
MW=80.385 #(W-boson mass)

cut_LEPW = (Mv1+Mvp > MW)&(Mv2+Mvp > MW)
cut_LEPZ = (Mv1+Mv2 > MZ)&(2*Mvp > MZ)

cut_LEPa=(Mv1>100)|(Mv2>200)|(Mv2-Mv1<8)|(Mv2+Mv1>198-8)
cut_LEPb=(Mvp>93)

cut2 = cut_LEPW&cut_LEPZ&cut_LEPa&cut_LEPb 

## ----- Invisible Higgs decay limits (h->inv)

cut_invH = (Brv1 + Brv2 < 0.24)
cut3 = cut_invH

# ------ Diphoton limits (h->AA)

SMBrHAA=2.28E-03  # SM Branching of Higgs decay into diphoton
RAA=BrHAA/SMBrHAA  # Diphoton parameter
#cut_RAA = (RAA<1.16+0.40)&(RAA>1.16-0.36) 
#cut4 = cut_RAA 

cut_RAA = (RAA<0.99+0.14)&(RAA>0.99-0.14)
cut4 = cut_RAA

######################################
#Experimantal Dark Matter constraints#
######################################

#------- Relic Density limits (PLANCK experiment)
cut5=(omega<0.1196)
cut10=cut1&(omega>0.1172)

# Direct Detection limits
R_ome = omega/0.112  #Re-scale of Omega
Psi_hat = R_ome*prot

cut6=(Psi_hat<LUX) # (LUX experiment)
cut7=(Psi_hat<XENON) #(XENON experiment)

#-------Unitarity----------------

def fLAM_o(x):
    y = np.where(x<=200, 1000, x*5)
    return y

LAM_1 = fLAM_o(Mv1) 
LAM_2 = fLAM_o(Mv2) 
LAM_p = fLAM_o(Mvp) 

#CANAL h V1 -> h V1 (Checked)
num1 = -(lamL + 0.5*(lamL*vv/Mv1)**2)*(LAM_1)**2 #(qs)**2
den1 = 64*pi*Mv1**2
A01 = num1/den1
a01 = abs(A01)

#CANAL h V2 -> h V2 (Checked)
num2 = -(lamR + 0.5*(lamR*vv/Mv2)**2)*(LAM_2)**2
den2 = 64*pi*Mv2**2
A02 = num2/den2
a02 = abs(A02)

#CANAL h VC -> h VC (Checked)
num3 = -(l2 + 0.5*(l2*vv/Mvp)**2)*(LAM_p)**2
den3 = 64*pi*Mvp**2
A03 = num3/den3
a03 = abs(A03)


#CANAL Z V1 -> Z V1 (Checked)
num4 = (LAM_1)**2*(g**2*(CW**4*(-8*Mv1**4 + Mv1**2*(8*Mv2**2 + 5*MZ**2) - 18*Mv1*Mv2**2*MZ + 9*Mv2**4 - 14*Mv2**2*MZ**2) + CW**2*MW**2*(11*Mv1**2 + 12*Mv2**2 - 5*MZ**2) - 3*MW**4)/(CW**4*Mv2**2*MW**2) - 24*lamL)
den4 = 1536*pi*Mv1**2
A04 = num4/den4
a04 = abs(A04)
#print('a07 = ', a07)

#CANAL Z V2 -> Z V2 (Checked)
num5 = (LAM_2)**2*(g**2*( CW**4*(-9*Mv1**4 + 2*Mv1**2*(-4*Mv2**2 + 9*Mv2*MZ + 7*MZ**2) + 8*Mv2**4 -5*Mv2**2*MZ**2) + CW**2*MW**2*(-12*Mv1**2 - 11*Mv2**2 + 5*MZ**2) + 3*MW**4)/(CW**4*Mv1**2*MW**2) + 24*lamR)
den5 = 1536*pi*Mv2**2
A05 = num5/den5
a05 = abs(A05)
#print('a09 = ', a09)

#CANAL Z VC -> Z VC (Checked)
num6 =  (LAM_p)**2*( ((g**2-2*CW**2*g)**2*(9*CW**4**Mvp**2*(-Mvp**2 + 2*Mvp*MZ + MZ**2) + CW**2*MW**2*(5*MZ**2 - 23*Mvp**2) + 3*MW**4))/(CW**4*MW**2) + 24*l2*Mvp**2)
den6 = 1536*pi*Mvp**4
A06 = num6/den6
a06 = abs(A06)
#print('a11 = ', a11)

#CANAL W V1 -> W V1 (Checked)
num7 = (LAM_1)**2*(g**2*(8*Mv1**4 - 8*Mv1**2*(Mvp**2 + 2*MW**2) + 18*Mv1*Mvp**2*MW - 9*Mvp**4 + 2*Mvp**2*MW**2 + 8*MW**4) + 24*lamL*Mvp**2*MW**2)
den7 = 1536*pi*Mv1**2*Mvp**2*MW**2
A07 = num7/den7
a07 = abs(A07)
#print('a08 = ', a08)


#CANAL W V2 -> W V2 (Checked)
num8 = (LAM_2)**2*(g**2*(8*Mv2**4 - 8*Mv2**2*(Mvp**2 + 2*MW**2) + 18*Mv2*Mvp**2*MW - 9*Mvp**4 + 2*Mvp**2*MW**2 + 8*MW**4) + 24*lamR*Mvp**2*MW**2)
den8 = 1536*pi*Mv2**2*Mvp**2*MW**2
A08 = num8/den8
a08 = abs(A08)
#print('a10 = ', a10)


#CANAL W VC -> W VC (Checked)
num9 = (LAM_p)**2*g**2*( 9*MW**2/(CW**2) - 6*(Mvp**2 - MW**2)**2*(1/(Mv1**2) - 1/(Mv2**2)) + 2*(5*Mvp**2 - 8*MW**2) - 12*l2*MW**2/(g**2))
den9 = 768*pi*Mvp**2*MW**2
A09 = num9/den9
a09 = abs(A09)
#print('a12 = ', a12)


#CANAL VC VC -> VC VC (Checked)
num10 = (LAM_p)**2*((g**2*(9*(SW**2-CW**2)**2*MW**2 - 4*CW**2*(LAM_p)**2))/(CW**4*Mvp**2) + 16*(l2*vv/Mvp)**2)
den10 = 1536*pi*Mvp**2
A10 = num10/den10
a10 = abs(A10)
#print('a12 = ', a12)


CahV = (a01<0.5)&(a02<0.5)&(a03<0.5)
CAhV = (a01>0.5)|(a02>0.5)|(a03>0.5)

CaZV = (a04<0.5)&(a05<0.5)&(a06<0.5)
CAZV = (a04>0.5)|(a05>0.5)|(a06>0.5)

CaWV = (a07<0.5)&(a08<0.5)&(a09<0.5)
CAWV = (a07>0.5)|(a08>0.5)|(a09>0.5)

CaCC = (a10<0.5)
CACC = (a10>0.5)

CaGV = (a04<0.5)&(a05<0.5)&(a06<0.5)&(a07<0.5)&(a08<0.5)&(a09<0.5)
CAGV = (a04>0.5)|(a05>0.5)|(a06>0.5)|(a07>0.5)|(a08>0.5)|(a09>0.5)

cut_unit = (a01<0.5)&(a02<0.5)&(a03<0.5)&(a04<0.5)&(a05<0.5)&(a06<0.5)&(a07<0.5)&(a08<0.5)&(a09<0.5)
#TODO = (a01>0.5)|(a02>0.5)|(a03>0.5)|(a04>0.5)|(a05>0.5)|(a06>0.5)|(a07>0.5)|(a08>0.5)|(a09>0.5)







