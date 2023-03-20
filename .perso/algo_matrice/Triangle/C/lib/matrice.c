#include "matrice.h"
#include <stdio.h>
#include <stdlib.h>



typedef double **matrice;


int remplir(matrice a){
	int nbL,nbC;
	scanf("%d %d",&nbL,&nbC);
	a = (double **) malloc (nbL * sizeof(double *))
	if(a != NULL) {
		for(int i=0;i<nbL;i++){
			a[i] = (double *) malloc (nbC * sizeof(double));
			if(a[i] != NULL){
				for(int j=0;j<nbC;j++){
					scanf("%lf",&a[i][j]);
				}
			}
		}
	return 1;
	} else return 0;
}

