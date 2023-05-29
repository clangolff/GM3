#include <stdio.h>
#include "tableau.h"

float moyenne(Tableau,int);
int traitement(Tableau,float,int n);
int superieurA18(Tableau,int);

int main(){
	Tableau note;
	int nbeleves = créer(note);
	float moy = moyenne(note,nbeleves);
	printf("la moyenne des notes est %.2f \n",moy);
	traitement(note,moy,nbeleves);
	if(!(superieurA18(note,nbeleves))) printf("il n'y a pas de note plus grande que 18 \n");
}

float moyenne(Tableau t,int n){
	float sum = 0.0;
	for(int i=0;i<n;i++){
		sum += t[i];
	}
	return sum/ (float) n;
}

int traitement(Tableau t, float moyenne, int n){
	Tableau nonMoyenne;
	int k =0, j=0;
	for(int i=0;i<n;i++){
		if(t[i]>10){
			k++;
		}	
		if(t[i]<moyenne){
			nonMoyenne[j] = i+1;
			j++;	
		}
	}
	affiche(nonMoyenne,j);
} 

int superieurA18(Tableau t, int n){
	int trouvé = 0;
	int i = 0;
	while(i<n && !(trouvé)){
		if(t[i]>=18) trouvé = 1;
		else i++;
	}
	if(trouvé){
		printf("premiere note supérieur à 18 : %.2f \n",t[i]);
		return 1;
	}
	else return 0;
}
