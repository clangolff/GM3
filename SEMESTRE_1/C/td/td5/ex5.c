#include <stdio.h>
#include "tableau.h"

void triSelection(Tableau,int);
void echanger(Tableau,int,int);

int main(){
	int n;
	Tableau t;
	n = créer(t);
	if (n!=0){
		triSelection(t,n);
		affiche(t,n);
	} else printf("aucun élement\n");
	
}

void triSelection(Tableau t, int n){
	int lepluspetit, indicedupluspetit;
	for(int i = 0;i<n-1;i++){
		lepluspetit = t[i];
		indicedupluspetit = i;
		for(int j = i +1;j<n;j++){
			if(t[j] < lepluspetit) {
				lepluspetit = t[j];
				indicedupluspetit = j;
			}
		}
		if(indicedupluspetit != i){
			echanger(t,i,indicedupluspetit);
		}	
	}
}

void echanger(Tableau t, int i, int j){
	int temp = t[j];
	t[j] = t[i];
	t[i] = temp; 
}

