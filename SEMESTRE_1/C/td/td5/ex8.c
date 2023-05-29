#include <stdio.h>
#include "matrice.h"

int main(){
	Matrice mat;
	int n,p;
	do{
	printf("entrez dimension matrice (ligne/colonne)\n");
	scanf("%d%d",&n,&p);
	}while(n>MAX || p>MAX);
	remplir(mat,n,p);
	printf("la somme des élements de la matrice est %.2f \n",sumElement(mat,n,p));
}
