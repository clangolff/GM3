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
			if(A.t[k][k] !=0.){
				A.t[i][k] /= A.t[k][k];
				for(int j=k+1;j<n;j++){
					A.t[i][j] -= A.t[i][k] * A.t[k][j];
				}
			}
			else {
				printf("erreur pivotnul\n");
				break;
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
