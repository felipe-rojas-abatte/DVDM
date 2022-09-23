/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
#define OMEGA            
  /* Calculate relic density and display contribution of  individual channels */
#define CDM_NUCLEON     
  /* Calculate amplitudes and cross-sections for  CDM-mucleon collisions */  

/*===== End of DEFINE  settings ===== */

#include"../include/micromegas.h"
#include"../include/micromegas_aux.h"
#include"lib/pmodel.h"
#include <time.h>

/*******START***********************/
int main(int argc,char** argv)
{  int err;
   char cdmName[10];
   int spin2, charge3,cdim;
   
  ForceUG=1;  /* to Force Unitary Gauge assign 1 */

  VZdecay=1; VWdecay=1;  

 int npoints=30000,i;
 int seed = time(NULL);
 srand(seed);
 printf("seed= %i \n",seed); 

 FILE *f1 = fopen("/home/felipe/Documents/Programas/micromegas_4.3.5/VHDMM/scan_rand.dat","w"); 
  fprintf(f1,"%s %s %s %s %s %s %s %s %s %s %s %s %s \n", " Mv1   ", "   Mv2    ", "   Mvp    ", "    lamL    ","  alpha2  ","   alpha3   ","    Omega   ", "    protonSI  ", "   Br(H->v1v1) ", "   Br(H->v2v2) ", "   Br(H->v-v+) ","   Br(H->AA)  ","   Width_H  ");
 
 double Mv1, Mv2, Mvp, lamL, alp2, alp3, alpha2, alpha3, massv1, massv2, massvp, ldL, ld2, ld3, ld4, protonSI, OME, lamS, mpar2, vv, cross, R, massW, massZ;
 int N;
 N=1;
 
 float PI = 3.14159265359;
 
 double massv1_min=100,        massv1_max=2000;
 double massv2_min=10,        massv2_max=2000;
 double massvp_min=10,        massvp_max=2000;
 double ldL_min=-1.5,       ldL_max=1.5;
 double alp2_min=-1,      alp2_max=1; 
/* double alp3_min=-1,      alp3_max=1;*/


  if(argc==1)
  { 
      printf(" Correct usage:  ./main  <file with parameters> \n");
      printf("Example: ./main data1.par\n");
      exit(1);
  }
                               
  err=readVar(argv[1]);
  
  if(err==-1)     {printf("Can not open the file\n"); exit(1);}
  else if(err>0)  { printf("Wrong file contents at line %d\n",err);exit(1);}
           
  
while(N <= npoints){
  
  massv1     = massv1_min+(double) random()/RAND_MAX*(massv1_max-massv1_min);
  massv2     = massv2_min+(double) random()/RAND_MAX*(massv2_max-massv2_min);
  massvp     = massvp_min+(double) random()/RAND_MAX*(massvp_max-massvp_min);
  ldL        = ldL_min+(double) random()/RAND_MAX*(ldL_max-ldL_min);  
  alp2       = alp2_min+(double) random()/RAND_MAX*(alp2_max-alp2_min); 
 /* alp3       = alp3_min+(double) random()/RAND_MAX*(alp3_max-alp3_min);  */

  /**********************************************/


   if( massv1<massv2 && massv1<massvp )
   {			assignValW("Mv1",massv1);
			assignValW("Mv2",massv2);
			assignValW("Mvp",massvp);
			assignValW("lamL",ldL);
			assignValW("alpha2",alp2);      
			assignValW("alpha3",-alp2);
			
  			err=sortOddParticles(cdmName); }
   
   else{
     /* printf("Mass Dark Matter bigger than other 2 odd mass\n");*/ continue;
      			}

   if(err) { printf("Can't calculate %s\n",cdmName); continue;}
    			
    			findVal("Mv1",&Mv1);
			findVal("Mv2",&Mv2);
			findVal("Mvp",&Mvp);
			findVal("lamL",&lamL);
			findVal("alpha2",&alpha2);
			findVal("alpha3",&alpha3);
			findVal("lam2",&ld2);
			findVal("lam3",&ld3);
			findVal("lam4",&ld4);
			findVal("Mpar2",&mpar2);
			findVal("vv",&vv);
			findVal("lam",&lamS);
			findVal("MZ",&massZ);
			findVal("MW",&massW);

txtList braH;
 double BraH_1,BraH_2,BraH_3,WH,BraHAA;

/*Mass and width decay of neutral higgs*/
   WH = pWidth("H",&braH);

/*Branching ratios of Neutral higgs without Standard Model equivalents */
  BraH_1 = findBr(braH,"~v1,~v1");
  BraH_2 = findBr(braH,"~v2,~v2");
  BraH_3 = findBr(braH,"~v+,~v-");
  BraHAA = findBr(braH,"A,A");
 

#ifdef OMEGA
{ int fast=1;
  double Beps=1.E-4, cut=0.01;
  double Omega;  
  int i,err; 
  /*printf("\n==== Calculation of relic density =====\n");   */

  if(CDM1 && CDM2) 
  {
  
    Omega= darkOmega2(fast,Beps);
  /*
    displayFunc(vs1120F, Tend, Tstart,"vs1120F");
    displayFunc(vs2200F, Tend, Tstart,"vs2200F");
    displayFunc(vs1100F, Tend, Tstart,"vs1100F");
    displayFunc(vs1210F, Tend, Tstart,"vs1210F");
    displayFunc(vs1122F, Tend, Tstart,"vs1122F");
    displayFunc(vs2211F, Tend, Tstart,"vs2211F");
  
    displayFunc(vs1110F, Tend, Tstart,"vs1110F");
    displayFunc(vs2220F, Tend, Tstart,"vs2220F");
    displayFunc(vs1112F, Tend, Tstart,"vs1110F");
    displayFunc(vs1222F, Tend, Tstart,"vs1222F");
    displayFunc(vs1220F, Tend, Tstart,"vs1220F");
    displayFunc(vs2210F, Tend, Tstart,"vs2210F");
    displayFunc(vs2221F, Tend, Tstart,"vs2221F");
    displayFunc(vs1211F, Tend, Tstart,"vs1211F");
  */
  
    printf("Omega_1h^2=%.2E\n", Omega*(1-fracCDM2));
    printf("Omega_2h^2=%.2E\n", Omega*fracCDM2);
  } else
  {  double Xf;
     Omega=darkOmega(&Xf,fast,Beps);
    /* printf("Xf=%.2e Omega=%.2e\n",Xf,Omega);*/
    /* printf("Omega=%.2e\n",Omega);*/
  /*   if(Omega>0)printChannels(Xf,cut,Beps,1,stdout);*/
  }
OME = Omega;
}

#endif

/*if(OME < 0.1196 && OME > 0.1172){*/
 printf("N = %i    Omega=%.2e\n",N,OME);

#ifdef CDM_NUCLEON
{ double pA0[2],pA5[2],nA0[2],nA5[2];
  double Nmass=0.939; /*nucleon mass*/
  double SCcoeff;        

/*printf("\n==== Calculation of CDM-nucleons amplitudes  =====\n");   */

  if(CDM1)
  {  
    nucleonAmplitudes(CDM1, pA0,pA5,nA0,nA5);
   /* printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM1);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); */

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
 /*   printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]);
  /*  printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);*/
  }
  if(CDM2)
  {
    nucleonAmplitudes(CDM2, pA0,pA5,nA0,nA5);
  /*  printf("CDM[antiCDM]-nucleon micrOMEGAs amplitudes for %s \n",CDM2);
    printf("proton:  SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",pA0[0], pA0[1],  pA5[0], pA5[1] );
    printf("neutron: SI  %.3E [%.3E]  SD  %.3E [%.3E]\n",nA0[0], nA0[1],  nA5[0], nA5[1] ); */

  SCcoeff=4/M_PI*3.8937966E8*pow(Nmass*Mcdm/(Nmass+ Mcdm),2.);
 /*   printf("CDM[antiCDM]-nucleon cross sections[pb]:\n");
    printf(" proton  SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*pA0[0]*pA0[0],SCcoeff*pA0[1]*pA0[1],3*SCcoeff*pA5[0]*pA5[0],3*SCcoeff*pA5[1]*pA5[1]); 
     printf(" neutron SI %.3E [%.3E] SD %.3E [%.3E]\n",
       SCcoeff*nA0[0]*nA0[0],SCcoeff*nA0[1]*nA0[1],3*SCcoeff*nA5[0]*nA5[0],3*SCcoeff*nA5[1]*nA5[1]);*/
  } 
protonSI= SCcoeff*pA0[0]*pA0[0];    
}
#endif
  
fprintf(f1,"%.2f   %.2f    %.2f   %.3E   %.3E   %.3E     %.3E     %.3E      %.3E       %.3E       %.3E      %.3E      %.3E \n", Mv1, Mv2, Mvp, lamL, alpha2, alpha3, OME, protonSI, BraH_1, BraH_2, BraH_3, BraHAA, WH);

N = N+1;
/* end of the main loop*/
  }

  killPlots();
  return 0;
}
