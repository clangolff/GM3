#include <stdio.h>
#include "tableau.h"

int créer(Tableau t) {
	int i = 0,n;
	do {
	printf("entrez le nombre d'élément du tableau \n");
	scanf("%d",&n);
	} while (n > MAX);
	if(n !=0) {
		printf("entrez element du tableau \n");
		do {
			scanf("%f",&t[i]);
			i++;
		}while(i<n);
	}
	return n;
}

void affiche(Tableau t , int n){
	for(int i=0;i<n;i++){
		printf("%.2f ",t[i]);
	}
	printf("\n");
}

int EstDans(Tableau t, int inf, int sup, float e){
	int k = inf;
	int res = 0; /*element n'est pas dans le tableau*/
	if(inf<=sup){
		do{
			if(t[k] != e) k++;
			else res = 1;
		}while((k<=sup) && (res==0));
	}
	return res;
}

float maxTab(Tableau t, int n){
	float max = t[0];
	for(int i = 1;i<n;i++) {
		if(t[i] > max ) max = t[i]; 
	}
	return max;
}

int recherche(Tableau t,int n,float e){
	int indice,trouvé = 0,i = 0;
	do {
		if(t[i] == e) trouvé = 1;
		i++;
	} while(i<n && !(trouvé));
	if(i<n) indice = i;
	else indice = -1;
	return indice;
}

int copy(Tableau t1,Tableau t2,int n){
	for(int i=0;i<n;i++){
		t2[i] = t1[i];
	}
	return 1;
}
