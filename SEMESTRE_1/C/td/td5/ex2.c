#include <stdio.h>
#include "tableau.h"

void inverserV1(Tableau,int);
void inverserV2(Tableau,int);

int main(){
	int n;
	Tableau t;
	n = créer(t);
	if (n!=0){
		inverserV1(t,n);
		printf("inverser version 2 tableaux ");
		affiche(t,n);
		inverserV1(t,n);
		inverserV2(t,n);
		printf("inverser version 1 tableau ");
		affiche(t,n);
	} else printf("aucun élement à inverser\n");
	
}

void inverserV1(Tableau t, int n){
	Tableau temp;
	for(int i = 0; i<n;i++){
		temp[i] = t[n - i -1];
	}
	for(int i = 0; i<n;i++){
		t[i] = temp[i];
	}
}

void inverserV2(Tableau t, int n){
	float temp;
	for(int i =0 ; i <= (n%2);i++) {
		temp = t[i];
		t[i] = t[n-1-i];
		t[n-1-i] = temp; 
	}
}
