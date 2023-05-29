#include <stdio.h>
#include "tableau.h"

int clé_presente1(Tableau,int,float);
int clé_presente2(Tableau,int,float);
int main(){
	Tableau t;
	int n;
	float clé;
	n = créer(t);
	affiche(t,n);
	printf("entrez la clé \n");
	scanf("%f",&clé);
	if (clé_presente1(t,n,clé)) printf("V1 %.2f est present \n",clé);
	else printf("V1 %.2f non présent \n",clé);

	if (clé_presente2(t,n,clé)) printf("V2 %.2f est present \n",clé);
	else printf("V2 %.2f non présent \n",clé);

}

int clé_presente1(Tableau t, int n,float clé){
	int trouvé = 0;
	int i = 0;
	do{
		if(t[i] == clé) trouvé = 1;
		i++;
	}while(i<n && !(trouvé));
	if (trouvé) return 1;
	else return 0;
}

int clé_presente2(Tableau t, int n,float clé){
	int trouvé = 0;
	float *p = &t[0];  /*   p = a   */
	do{
		if(*p == clé) trouvé = 1;
		p++;
	}while(p<&t[n]  && !(trouvé));   /*   p < t + n   */
	if (trouvé) return 1;
	else return 0;
}
