#include <stdio.h>
#include "tableau.h"

void elimineDoublon(Tableau,int *);

int main(){
	int n;
	float e;
	Tableau t;
	n = créer(t);
	affiche(t,n);
	if (n!=0){
		elimineDoublon(t,&n);
		printf("le nouveau tableau \n");
		affiche(t,n);
	} else printf("aucun élement\n");
	
}

void elimineDoublon(Tableau t,int *n){
	int i=1;
	while(i<=*n){
		if(!(EstDans(t,0,i-1,t[i]))) i++;
		else{
			for(int j=i;j<*n;j++){
				t[j] = t[j+1];   /*decalage des élement*/
			}
			(*n)--;        /*decrement la taille du tableau*/
		}
	}
}
