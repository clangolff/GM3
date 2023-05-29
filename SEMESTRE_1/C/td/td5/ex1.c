#include <stdio.h>
#include "tableau.h"

float somme(Tableau,int,int);

int main(){
	int n;
	float sum;
	Tableau t;
	n = créer(t);
	if(n!=0){	
		sum = somme(t,0,n);
		printf("la somme du tableau vaut %.3f \n",sum); 
	}
	else printf("aucun élément dans le tableau \n");
}

float somme(Tableau t, int i,int n){
	if(i>=n) return 0;
	else return t[i] + somme(t,i+1,n);	
}
