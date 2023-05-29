#include <stdio.h>
#include "tableau.h"

int main(){
	int n,indicerecherche;
	float e;
	Tableau t;
	n = créer(t);
	affiche(t,n);
	printf("entrez element à rechercher \n");
	scanf("%f",&e);
	indicerecherche = recherche(t,n,e);
	if(indicerecherche != -1) printf("l'indice de %.2f est %d \n",e,indicerecherche);
	else printf("%.2f n'est pas dans le tableau \n",e);
	
}
