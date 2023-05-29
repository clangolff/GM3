#include <stdio.h>
#include "tableau.h"

int main(){
	int n;
	float max;
	Tableau t;
	n = créer(t);
	affiche(t,n);
	max = maxTab(t,n);
	printf("le max du tableau est %.2f \n",max);
}
