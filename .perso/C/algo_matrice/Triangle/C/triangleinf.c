#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"

void Exit_erreur(const char *message){
	printf("erreur : %s",message);
	exit(EXIT_FAILURE);
}

void main(){
	Tmatrice T,b,X;
	int n;
	scanf("%d",&n);

/*allocation*/
	if(!Allouer(&T,n,n)) Exit_erreur("allocation");

	if(!Allouer(&b,n,1)) Exit_erreur("allocation");
	if(!Allouer(&X,n,1)) Exit_erreur("allocation");

/*remplissage*/
	if(!Remplir(&T)) Exit_erreur("remplissage");
	if(!Remplir(&b)) Exit_erreur("remplissage");


/*main*/
	for(int i=0;i<n;i++){
		X.t[i][0] = b.t[i][0];
		for(int k=0;k<i;k++){
			X.t[i][0] -= T.t[i][k] * X.t[k][0];
		}
		X.t[i][0] /= T.t[i][i];
	}
/*affichage*/
	if(!Affiche(X)) Exit_erreur("affichage");

/*desallocation*/
	if(!Desallouer(&T)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&X)) Exit_erreur("desallocation");
	
}
