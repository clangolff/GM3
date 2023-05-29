#include "matrice.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int Remplir(Tmatrice *a){
	int res;
	if((*a).t != NULL){
		for(int i=0;i<(*a).nbL;i++){
			for(int j=0;j<(*a).nbC;j++){
				scanf("%lf",&(*a).t[i][j]);
			}
		}
		res = 1;
	} else res = 0;
	return res;
}


int Allouer(Tmatrice *a,int nbL,int nbC){
	(*a).nbL = nbL;
	(*a).nbC = nbC;
	int res = 1;        /*variable pour savoir si l'allocation s'est bien faite*/
	(*a).t = (double **) malloc (nbL * sizeof(double *));
	if((*a).t != NULL){
		for(int i=0;i<nbL;i++){
			(*a).t[i] = (double *) malloc (nbC * sizeof(double));
			if((*a).t[i] == NULL){
				res = 0;
				} else {
				  for(int j=0;j<nbC;j++){
				          (*a).t[i][j] = 0;
				          }
				}
			}
	}else res = 0;
	return res;		
}

int Desallouer(Tmatrice *a){
	for(int i=0;i<(*a).nbL;i++){
		free((*a).t[i]);
	}
	free((*a).t);
	(*a).t = NULL;
	return 1;
}

int Affiche(Tmatrice a){
	int res;
	if(a.t != NULL ){
		for(int i=0;i<a.nbL;i++){
			for(int j=0;j<a.nbC;j++){
				printf("%e ",a.t[i][j]);
			}
    		printf("\n");
		}
		res = 1;
	} else res = 0;
	return res;
}

int Matmul(Tmatrice a,Tmatrice b,Tmatrice *c){
	int res;
	if (a.nbC == b.nbL){
		(*c).nbL = a.nbL;
		(*c).nbC = b.nbC;
   	 	for(int i=0;i<a.nbL;i++){
			for(int j=0;j<b.nbC;j++){
				double sum = 0.;
				for(int k=0;k<a.nbC;k++){
					sum += a.t[i][k] * b.t[k][j];
				}
				(*c).t[i][j] = sum;
			}	
		}
	res = 1;
	}else{
		res = 0;
		(*c).nbL = 0;
		(*c).nbC = 0;
		(*c).t = NULL;
	}
	return res;
}

double Dot_product(Tmatrice a, Tmatrice b){
	double res = 0.;
	if(a.nbC == 1 && b.nbC == 1){
		for(int i=0;i<a.nbL;i++){
			res += a.t[i][0] * b.t[i][0];
		}
	} 
	return res;
}

double Norm2(Tmatrice a,Tmatrice b){
	double res;
	res = sqrt(Dot_product(a,b));
	return res;
}

int Add(Tmatrice *a, Tmatrice b){
	int res = 0;
	if((*a).nbL == b.nbL && (*a).nbC == b.nbC){
		res = 1;
		for(int i=0;i<b.nbL;i++){
			for(int j=0;j<b.nbC;j++){
				(*a).t[i][j] += b.t[i][j];
			}
		}
	}
	return res;
}

int Mult(double k, Tmatrice *a){
	int res = 0;
	if(a != NULL){
		for(int i=0;i<(*a).nbL;i++){
			for(int j=0;j<(*a).nbC;j++){
				(*a).t[i][j] *= k;
			}
		}
		res = 1;
	}
	return res;
}
