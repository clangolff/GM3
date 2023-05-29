#include <stdio.h>
#include "tableau.h"

int estSymetrique(Tableau,int);

int main(){
	int n;
	Tableau t;
	n = créer(t);
	if (n!=0){
		if(estSymetrique(t,n)) printf("le tableau est symetrique\n");
		else printf("le tableau n'est pas symetrique\n");
	} else printf("aucun élement\n");
	
}

int estSymetrique(Tableau t,int n){
	int estSym = 1;
	for(int i = 0 ; i <= n%2;i++){
		if (t[i] != t[n-1-i]) {
			estSym = 0;
			break;
		}
	}
	return estSym;
}
