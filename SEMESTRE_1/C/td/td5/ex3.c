#include <stdio.h>
#include "tableau.h"

int decaler(Tableau,int);

int main(){
	int n;
	Tableau t;
	n = créer(t);
	if (n!=0){
		if(decaler(t,n)) affiche(t,n);
	} else printf("aucun élement\n");
	
}

int decaler(Tableau t, int n){
	int temp = t[n-1];
	for(int i = n-1;i>0;i--){
		t[i] = t[i-1];
	}
	t[0] = temp;
	return 1;
}
