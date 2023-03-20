#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"
#include <math.h>

void Exit_erreur(const char *message){
	printf("erreur : %s",message);
	exit(EXIT_FAILURE);
}

void main(){
	Tmatrice A,b,x,r,temp;
	int n;
	scanf("%d",&n);

/*allocation*/
	if(!Allouer(&A,n,n)) Exit_erreur("allocation");

	if(!Allouer(&b,n,1)) Exit_erreur("allocation");
	if(!Allouer(&x,n,1)) Exit_erreur("allocation"); 

	if(!Allouer(&r,n,1)) Exit_erreur("allocation");
     	if(!Allouer(&temp,n,1)) Exit_erreur("allocation");
     

/*remplissage*/

	if(!Remplir(&A)) Exit_erreur("remplissage");
	if(!Remplir(&b)) Exit_erreur("remplissage");
	if(!Remplir(&x)) Exit_erreur("remplissage");

/*main*/
	int Nmax;
	double tol,normeR,alpha;
	scanf("%d %lf",&Nmax,&tol);
	
	Matmul(A,x,&r);
	Mult(-1.,&r);
	Add(&r,b);
	for(int i=0;i<Nmax;i++){
		normeR = Dot_product(r,r);
		printf("%d %e\n",i,normeR);
		if(normeR < tol)
			 break;
		Matmul(A,r,&temp);
		alpha = normeR / Dot_product(temp,r);
		Mult(alpha,&r);
		Add(&x,r);
		Matmul(A,x,&r);
		Mult(-1.,&r);
		Add(&r,b);
	}
	printf("soltion :\n");
	Affiche(x);

/*desallocation*/
	if(!Desallouer(&A)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&x)) Exit_erreur("desallocation");
	if(!Desallouer(&r)) Exit_erreur("desallocation");
	if(!Desallouer(&temp)) Exit_erreur("desallocation");
	
}
