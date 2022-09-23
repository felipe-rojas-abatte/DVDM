/*====== Modules ===============
   Keys to switch on 
   various modules of micrOMEGAs  
================================*/
      
#define MASSES_INFO      
  /* Display information about mass spectrum  */
  
#define OMEGA            
  /* Calculate relic density and display contribution of  individual channels */
#define CDM_NUCLEON     
  /* Calculate amplitudes and cross-sections for  CDM-mucleon collisions */  


/*===== End of DEFINE  settings ===== */

#include"../include/micromegas.h"
#include"../include/micromegas_aux.h"
#include"lib/pmodel.h"

/*******START***********************/
int main(int argc,char** argv)
{  int err;
   char cdmName[10];
   int spin2, charge3,cdim;
   
  ForceUG=1;  /* to Force Unitary Gauge assign 1 */

  VZdecay=1; VWdecay=1; 
   
 int i;
 i=0;
  FILE *f1 = fopen("/home/felipe/Documents/Programas/micromegas_4.3.5/VHDMM/lam_M=1000_deltaM=20.dat","w");
   
   fprintf(f1,"%s %s %s %s %s %s %s %s %s %s %s \n", " Mv1  ", "   Mv2    ", "   Mvp    ", "    lamL    ","    Omega   ", "    protonSI  ", "  Br(H->v1v1) ", "   Br(H->v2v2) ", "   Br(H->v-v+)  ","   Br(H->AA)  ","   Width_H  ");
 
 double Mv1, Mv2, Mvp, lamL, alp2, alp3, alpha2, alpha3, massv1, massv2, massvp, ldL, ld2, ld3, ld4, protonSI, OME, lamS, mpar2, vv, cross, R, massW, massZ, DeltaM;
 int N;
 N=1;
 DeltaM=1;
 ldL=5;


  for(massv1 = 10; massv1 <= 2000; massv1 = massv1 + 1)
     {  for(massv2 = massv1+DeltaM; massv2 <= massv1+DeltaM; massv2 = massv2 + 1)  
           {   for(massvp = massv1+DeltaM; massvp <= massv1+DeltaM; massvp = massvp + 1)
	         {  /*for(ldL =-5; ldL <=5; ldL = ldL + 0.1)
	               {  

/******* New point *********/
printf("\n ****** New Point ******* \n ");
                                    
	/*printf("Mv1 = %.1f  Mv2 = %.1f   Mvp = %.1f  lamL = %.2E  alpha2 = %.2E  alpha3 = %.2E \n",massv1,massv2,massvp,ldL,alp2,alp3);*/
		
    if( massv1 < massv2 && massv1 < massvp )
   {			assignValW("Mv1",massv1);
			assignValW("Mv2",massv2);
			assignValW("Mvp",massvp);
			assignValW("lamL",ldL);
			assignValW("alpha2",1);      
			assignValW("alpha3",1); 
			
  			err=sortOddParticles(cdmName); }
   
   else{
      printf("Mass Dark Matter bigger than other 2 odd mass\n"); continue;
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
     
/*  if(err) { printf("Can't calculate %s\n",cdmName); return 1;}*/
  
 /* if(CDM1) 
  { 
     qNumbers(CDM1, &spin2, &charge3, &cdim);
     printf("\nDark matter candidate is '%s' with spin=%d/2 mass=%.2E\n",CDM1,  spin2,Mcdm1); 
     if(charge3) printf("Dark Matter has electric charge %d/3\n",charge3);
     if(cdim!=1) printf("Dark Matter is a color particle\n");
  }
  if(CDM2) 
  { 
     qNumbers(CDM2, &spin2, &charge3, &cdim);
     printf("\nDark matter candidate is '%s' with spin=%d/2 mass=%.2E\n",CDM2,spin2,Mcdm2); 
     if(charge3) printf("Dark Matter has electric charge %d/3\n",charge3);
     if(cdim!=1) printf("Dark Matter is a color particle\n");
  } */

 
 /*   printf("Mv1 = %.1f  Mv2 = %.1f   Mvp = %.1f  lamL = %.2E  alpha2 = %.2E  alpha3 = %.2E \n",Mv1,Mv2,Mvp,lamL,alpha2,alpha3);*/
   
txtList braH;
 double BraH_1,BraH_2,BraH_3,BraH_T,WH,BraHAA;

/*Mass and width decay of neutral higgs*/
   WH = pWidth("H",&braH);

/*Branching ratios of Neutral higgs without Standard Model equivalents */
  BraH_1 = findBr(braH,"~v1,~v1");
  BraH_2 = findBr(braH,"~v2,~v2");
  BraH_3 = findBr(braH,"~v+,~v-");
  BraHAA = findBr(braH,"A,A");
  
#ifdef MASSES_INFO
{
  printf("\n=== MASSES OF HIGGS AND ODD PARTICLES: ===\n");
  printHiggs(stdout);
  printMasses(stdout,1);
}
#endif


#ifdef OMEGA
{ int fast=1;
  double Beps=0.0001, cut=0.01;  
  double Omega;  
  int i,err; 
  /*printf("\n==== Calculation of relic density =====\n");   */

  if(CDM1 && CDM2) 
  {
  
    Omega= darkOmega2(fast,Beps);

    printf("Omega_1h^2=%.2E\n", Omega*(1-fracCDM2));
    printf("Omega_2h^2=%.2E\n", Omega*fracCDM2);
  } else
  {  double Xf;
     Omega=darkOmega(&Xf,fast,Beps);
     printf("Xf=%.2e Omega=%.2e\n",Xf,Omega);
     if(Omega>0)printChannels(Xf,cut,Beps,1,stdout);
  }
OME = Omega;
}

#endif


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
  

fprintf(f1,"%.2f    %.2f    %.2f     %.3E     %.3E     %.3E      %.3E      %.3E        %.3E       %.3E      %.3E\n", Mv1, Mv2, Mvp, lamL, OME, protonSI, BraH_1, BraH_2, BraH_3, BraHAA, WH);

}}}/*}*/
 
  killPlots();
  return 0;
 
}
