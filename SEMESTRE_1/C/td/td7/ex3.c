#include <stdio.h>
#include "tableau.h"
#define TAILLE 100 


float *max(Tableau,int);

int main(){
	Tableau t;
	int n;
	float *p;
	n = créer(t);
	affiche(t,n);
	p = max(t,n);
	printf("le max du tableau est %.2f \n",*p);
}

float *max(Tableau t, int n){
	float *p = &t[0];
	float max = t[0];
	for(int i=1;i<n;i++){
		if(t[i]>max) {
			max = t[i];
			p = &t[i];
		}
	}
	return p;
}
