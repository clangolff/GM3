#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"
#include <math.h>

void Exit_erreur(const char *message){
	printf("erreur : %s",message);
	exit(EXIT_FAILURE);
}

void main(){
	Tmatrice A,b,x,r0,r1,Ap,p,ptemp;
	int n;
	scanf("%d",&n);

/*allocation*/
	if(!Allouer(&A,n,n)) Exit_erreur("allocation");

	if(!Allouer(&b,n,1)) Exit_erreur("allocation");
	if(!Allouer(&x,n,1)) Exit_erreur("allocation"); 

	if(!Allouer(&r0,n,1)) Exit_erreur("allocation");
 
	if(!Allouer(&r1,n,1)) Exit_erreur("allocation");
     	if(!Allouer(&Ap,n,1)) Exit_erreur("allocation");
     
    	if(!Allouer(&p,n,1)) Exit_erreur("allocation");
     	if(!Allouer(&ptemp,n,1)) Exit_erreur("allocation");
     
 

/*remplissage*/

	if(!Remplir(&A)) Exit_erreur("remplissage");
	if(!Remplir(&b)) Exit_erreur("remplissage");
	if(!Remplir(&x)) Exit_erreur("remplissage");

/*main*/
	int Nmax;
	double tol,normeR0,normeR1,alpha,beta;
	scanf("%d %lf",&Nmax,&tol);
	
	Matmul(A,x,&r0);
	Mult(-1.,&r0);
	Add(&r0,b);
	Add(&p,r0);
	Add(&ptemp,p);
	normeR0 = Dot_product(r0,r0);
	for(int i=0;i<Nmax;i++){
		
		printf("%d %e\n",i,normeR0);
		if(normeR0 < tol)
			 break;
		Matmul(A,p,&Ap);
		/*alpha = (r,r)/(Ar,r)*/
		alpha = normeR0 / Dot_product(Ap,p);
		/*x = x + alpha*p */
		Mult(alpha,&ptemp);
		Add(&x,ptemp);
		/*r1 = r0 - alpha*Ap*/
		Mult(0,&r1);
		Add(&r1,Ap);
		Mult(-1.*alpha,&r1);
		Add(&r1,r0);
		/*beta = (r1,r1)/(r0,r0)*/
		normeR1 = Dot_product(r1,r1);
		beta = normeR1/normeR0;
		/*p = r1 + beta*p */
		Mult(beta,&p);
		Add(&p,r1);

		normeR0 = normeR1;
		Mult(0,&r0);
		Add(&r0,r1);
		Mult(0,&ptemp);
		Add(&ptemp,p);
	}
	printf("soltion :\n");
	Affiche(x);

/*desallocation*/
	if(!Desallouer(&A)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&x)) Exit_erreur("desallocation");
	if(!Desallouer(&r0)) Exit_erreur("desallocation");
	if(!Desallouer(&r1)) Exit_erreur("desallocation");
	if(!Desallouer(&Ap)) Exit_erreur("desallocation");
	if(!Desallouer(&p)) Exit_erreur("desallocation");
	if(!Desallouer(&ptemp)) Exit_erreur("desallocation");
	
}
