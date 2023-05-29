/*gcc -c instruction.h instruction.c*/
#ifndef instruction_h
#define instruction_h

#include "liste.h"

#define MAX 300


typedef char chaine[MAX];

typedef struct instruct
{
	int lg;
	chaine c;
	int rep;
} instruction;


int estUneDirection(char);
int estUnModeDecriture(char);
int estUnChiffre(char);
int longueur(chaine);
instruction LireChaine(chaine, int *, int *);

void remplirListe(liste **,char,int);  
void MaFonction(liste **,chaine);


#endif
