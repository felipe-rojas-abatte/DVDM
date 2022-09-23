#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main()
{   

 FILE *fdata = fopen("LEP_limit.dat","w");

fprintf(fdata,"%s %s %s \n"," Mv1 "," Mv2  ","   cs_(pb)  ");

char name[100];
char batch[100];

strcpy(name, "batch_LEP" );
strcpy(batch, "./calchep_batch batch_LEP" );
 
int energy;
float Mv1,Mv2;

energy = 103;

for(Mv1 = 1; Mv1 <= 101; Mv1=Mv1+5)  { //500
    for(Mv2 = 1; Mv2 <= 201; Mv2=Mv2+5)  { //500
       if(Mv1 + Mv2 <= 2*energy){

/* Genero el archivo BATCH con la información del proceso*/
 FILE *f10 = fopen(name,"w"); 

fprintf(f10,"Model: VDDMM \n");
fprintf(f10,"Model changed: False\n");
fprintf(f10,"Gauge: unitary\n");
fprintf(f10,"Process: e1,E1->~v1,~v2\n");
fprintf(f10,"S.F.1: ISR & Beamstralung \n");
fprintf(f10,"S.F.1: ISR & Beamstralung \n");
fprintf(f10,"p1: %i \n", energy);
fprintf(f10,"p2: %i \n", energy);
fprintf(f10,"Parameter: Mv1=%.1f \n", Mv1);
fprintf(f10,"Parameter: Mv2=%.1f \n", Mv2);
fprintf(f10,"Parameter: Mvp=500 \n");
fprintf(f10,"Parameter: lamL=1\n");
fprintf(f10,"Parameter: alpha2=1 \n");
fprintf(f10,"Parameter: alpha3=-1 \n");
fprintf(f10,"Number of events (per run step): 1\n");
fprintf(f10,"Filename: LEP_v1v2\n");
fprintf(f10,"NTuple: False\n");
fprintf(f10,"Cleanup: False\n");
fprintf(f10,"Parallelization method: local\n");
fprintf(f10,"Max number of nodes: 8\n");
fprintf(f10,"Max number of processes per node: 1\n");
fprintf(f10,"sleep time: 3\n");
fprintf(f10,"nice level: 19\n");
fprintf(f10,"nSess_1: 5\n");
fprintf(f10,"nCalls_1: 100000\n");
fprintf(f10,"nSess_2: 5\n");
fprintf(f10,"nCalls_2: 100000\n");
fclose(f10);

/* Ejecuto el archivo BATCH */

printf("\n ================================ \n Ejecutando archivo batch \n ================================ \n\n");
printf("  Mv1 = %.1f  Mv2 = %.1f \n",Mv1,Mv2);

system(batch);


/*** Elimino la parte que no me gusta del archivo numerical.txt ****/

FILE *oldFile = fopen("/home/felipe/Documents/Programas/micromegas_4.3.5/VDDMM/work/html/numerical.txt", "r");
FILE *newFile = fopen("/home/felipe/Documents/Programas/micromegas_4.3.5/VDDMM/work/html/new_numerical.txt", "w");

int lineNumber;
int len;
char line[4096],line1[4096];
int todoNumber;
lineNumber=0;

/*Debemos seleccionar la cantidad de líneas que deseamos eliminar del archivo numerical */
todoNumber=6;

if (oldFile != NULL) {
    while (fgets(line, sizeof line, oldFile)) {
        len = strlen(line);
        if (len && (line[len - 1] != '\n')) {} else {
            lineNumber++;
            if (lineNumber < todoNumber) {
                // Do nothing   
            } else {
                fputs(line, newFile);
            }
        }
    }
} else {
    printf("ERROR");
}
fclose(oldFile);
fclose(newFile);

/**** Extrae la sección eficaz del archivo numerical *****/
 
  FILE *f2 = fopen("/home/felipe/Documents/Programas/micromegas_4.3.5/VDDMM/work/html/new_numerical.txt","r");

    float sig;
      fscanf(f2,"%*s  %f  %*s  %*s  %*f  %*f",&sig);
      fprintf(fdata," %.1f    %.1f    %.4E \n",Mv1,Mv2,sig/1000);        

fclose(f2);

remove("/home/felipe/Documents/Programas/micromegas_4.3.5/VDDMM/work/html/new_numerical.txt");

}
else printf(" \n Not enough energy at LEP \n ");
}}


return 0; 
}

 
