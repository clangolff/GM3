#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"
#include <math.h>

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
	
	for(int j=0;j<n;j++){
		for(int i=j;i<n;i++){
			for(int k=0;k<j;k++){
				A.t[i][j] -= A.t[i][k] * A.t[j][k];
			}
			if(i==j) A.t[i][j] = sqrt(A.t[i][j]);
			else A.t[i][j] /= A.t[j][j];
		}
	}
	

/*affichage*/
	if(!Affiche(A)) Exit_erreur("affichage");

/*desallocation*/
	if(!Desallouer(&A)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&X)) Exit_erreur("desallocation");
	
}
