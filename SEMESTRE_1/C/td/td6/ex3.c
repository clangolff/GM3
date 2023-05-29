#include <stdio.h>
#include "tableau.h"

int main(){
	int n;
	Tableau t1,t2;
	n = créer(t1);
	affiche(t1,n);
	if(copy(t1,t2,n)) affiche(t2,n);
	else printf("erreur copie tableau");
}
