#include <stdio.h>
#include "matrice.h"

int main(){
	Matrice A,B,C;
	int n1,p1,n2,p2,n3,p3;
	do{
		printf("entrez dimension matrice A (ligne/colonne)\n");
		scanf("%d%d",&n1,&p1);
	}while(n1>MAX || p1>MAX);
	créerMatrice(A,n1,p1);
	remplir(A,n1,p1);
	do{
		printf("entrez dimension matrice B (ligne/colonne)\n");
		scanf("%d%d",&n2,&p2);
	}while(n2>MAX || p2>MAX);
	créerMatrice(B,n2,p2);
	remplir(B,n2,p2);
	if (multMatrice(A,n1,p1,B,n2,p2,C,&n3,&p3)){
		printf("produit de A et B\n");
		affiche(C,n3,p3);
	}
}	
