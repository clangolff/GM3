#include <stdio.h>
#include <stdlib.h>
#include "matrice.h"

void Exit_erreur(const char *message){
	printf("erreur : %s",message);
	exit(EXIT_FAILURE);
}

void main(){
	Tmatrice a,b,c;
	int nbL,nbC;
	scanf("%d %d",&nbL,&nbC);

/*allocation*/
	if(!Allouer(&a,nbL,nbC)) Exit_erreur("allocation");
	if(!Allouer(&b,nbL,nbC)) Exit_erreur("allocation");
	if(!Allouer(&c,nbL,nbC)) Exit_erreur("allocation");

/*remplissage matrice a et b*/
	if(!Remplir(&a)) Exit_erreur("remplissage");
/*	if(!Remplir(&b)) Exit_erreur("remplissage");
*/
	double k;
	scanf("%lf",&k);
	if(!Mult(k,&a)) Exit_erreur("matrice non alloué");

/*multiplication*/
/*	if(!Matmul(a,b,&c)) Exit_erreur("dimension");
*/

/*addition*/
/*	if(!Add(&a,b)) Exit_erreur("dimension");
*/
/*produit scalaire*/
/*	float ps =Norm2(a,b);
	printf("resultat norme2 : %f",ps);	
*/

/*affichage*/
/*	if(!Affiche(c)) Exit_erreur("affichage");
*/	if(!Affiche(a)) Exit_erreur("affichage");


/*desallocation*/
	if(!Desallouer(&a)) Exit_erreur("desallocation");
	if(!Desallouer(&b)) Exit_erreur("desallocation");
	if(!Desallouer(&c)) Exit_erreur("desallocation");
	
}
