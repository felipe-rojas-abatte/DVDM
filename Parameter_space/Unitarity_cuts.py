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

#-------Unitarity----------------
qs = 8000 #(GeV)
energy = '8'

# canal hV1->hV1
Rwv1 = MW/Mv1
num1 = (qs**2)*lamL*(1+2*(lamL/g**2)*(Rwv1**2))
den1 = 64*pi*Mv1**2
a01 = abs(num1/den1)

# canal hV2->hV2
Rwv2 = MW/Mv2
num2 = (qs**2)*lamR*(1+2*(lamR/g**2)*(Rwv2**2))
den2 = 64*pi*Mv2**2
a02 = abs(num2/den2)

# canal hVc->hVc
Rwvp = MW/Mvp
num3 = (qs**2)*l2*(1+2*(l2/g**2)*(Rwvp**2))
den3 = 64*pi*Mvp**2
a03 = abs(num3/den3)

# canal WL WL -> v1 v1  (lineal en s) 
#num4 = (qs**2)*((g**2)*(Mv1**4 + 2*(Mv1**2)*(Mvp**2) - 3*Mvp**4) + 8*lamL*(Mvp**2)*MW**2)
#den4 = 256*pi*(Mv1**2)*(Mvp**2)*(MW**2)
#a04 = abs(num4/den4)

#CANAL WL WL -> v2 v2  (lineal en s)  (fuerte en el plano Mv2 - Mvp)
#num2 = (qs**2)*((g**2)*(Mv2**4 + 2*(Mv2**2)*(Mvp**2) - 3*Mvp**4) + 8*lamR*(Mvp**2)*MW**2)
#den2 = 256*pi*(Mv2**2)*(Mvp**2)*(MW**2)
#A02 = num2/den2
#a02 = abs(A02)

#CANAL WL WL -> v+ v- (lineal en s)
#num3 = (qs**2)*((g**2)*(4 - 3*(Mv1**2 + Mv2**2)/Mvp**2 + (1/Mv1**2 + 1/Mv2**2)*Mvp**2) +16*l2*MW**2/Mvp**2)
#den3 = 512*pi*(MW**2)
#A03 = num3/den3
#a03 = abs(A03)

#CANAL WL WL -> v1 v2  (lineal en s)
#num4 = (g**2)*(qs**2)*(Mv2**2 - Mv1**2)*(Mv1**2 - Mvp**2)
#den4 = 512*pi*Mv1*Mv2*(Mvp**2)*(MW**2)
#A04 = num4/den4
#a04 = abs(A04)

#CANAL H H -> v1 v1  (lineal en s)  (fuerte en el plano Mv1-lamL)
#num5 = (qs**2)*lamL*((g**2)*(Mv1**2) + 2*lamL*MW**2)
#den5 = 32*pi*(g**2)*Mv1**4
#A05 = num5/den5
#a05 = abs(A05)

#CANAL H H -> v2 v2  (lineal en s)
#num6 = lamR*(qs**2)*((g**2)*(Mv2**2) + 2*lamR*MW**2)
#den6 = 32*pi*(g**2)*Mv2**4
#A06 = num6/den6
#a06 = abs(A06)

OK01 = (a01<0.5)
EXC01 = (a01>0.5)

OK02 = (a02<0.5)
EXC02 = (a02>0.5)

OK03 = (a03<0.5)
EXC03 = (a03>0.5)

#Ca04 = (a04<0.5)
#CA04 = (a04>0.5)

#Ca05 = (a05<0.5)
#CA05 = (a05>0.5)

#Ca06 = (a06<0.5)
#CA06 = (a06>0.5)


