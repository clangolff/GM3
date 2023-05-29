#include "liste.h"
#include <stdlib.h>
#include <stdio.h>

liste *listeVide(){
	return NULL;
}

int estVide(liste *l){
	return (l == NULL);
}


void fixerSucc(liste **l, liste *q){
	if ( !(estVide(*l)) ) (**l).succ = q;
}

void ajouterEnTete(liste **l, int x, int y, int modeEcriture){
	liste *temp;
	temp = (liste*) malloc(sizeof(liste));
	if(temp == NULL) exit(EXIT_FAILURE);
	(*temp).coord.x = x;
	(*temp).coord.y = y;
	(*temp).modeEcriture = modeEcriture;
	fixerSucc(&temp,*l);
	*l = temp;
}

liste *obtenirSucc(liste *l){
	return (*l).succ;
}

void affiche(liste *l){
	while(!(estVide(l))) {
		printf("x : %d y : %d modeEcriture : %d \n",(*l).coord.x,(*l).coord.y,(*l).modeEcriture);
		l = obtenirSucc(l);
	}
}

TypeCoordonnée obtenirCoord(liste *l){
	return (*l).coord;
}

void liberer(liste *l){
	if( !(estVide(l)) ) {
		liberer((*l).succ);
		free(l);
	}
}
