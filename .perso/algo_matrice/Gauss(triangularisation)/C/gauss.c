#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"

void Exit_erreur(const char *message){
	printf("erreur : %s",message);
	exit(EXIT_FAILURE);
}

void main(){
	Tmatrice A,b,X;
	int n;
	scanf("%d",&n);

/*allocation*/
	if(!Allouer(&A,n,n)) Exit_erreur("allocation");

	if(!Allouer(&b,n,1)) Exit_erreur("allocation");
	if(!Allouer(&X,n,1)) Exit_erreur("allocation");
     
/*remplissage*/

	if(!Remplir(&A)) Exit_erreur("remplissage");
	if(!Remplir(&b)) Exit_erreur("remplissage");


/*main*/
	double pivot;
	
	for(int k=0;k<n-1;k++){
	
		for(int i=k+1;i<n;i++){
			pivot = A.t[i][k]/A.t[k][k];
			b.t[i][0] -= pivot * b.t[k][0];
			for(int j=k;j<n;j++){
				A.t[i][j] -= pivot * A.t[k][j];
			}
		}
	}

/*affichage*/
	if(!Affiche(A)) Exit_erreur("affichage");

/*desallocation*/
	if(!Desallouer(&A)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&X)) Exit_erreur("desallocation");
	
}
