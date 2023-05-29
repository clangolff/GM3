/*gcc -c liste.c liste.h*/
#ifndef liste_h
#define liste_h


typedef struct coordonnée {
	int x;
	int y;
} TypeCoordonnée;

typedef struct noeud {
	TypeCoordonnée coord;
	int modeEcriture;
	struct noeud *succ;
} liste;


liste *listeVide();

int estVide(liste *);

void fixerSucc(liste **, liste *);

void ajouterEnTete(liste **,int,int,int);

liste *obtenirSucc(liste *);

void affiche(liste *);

TypeCoordonnée obtenirCoord(liste *);

void liberer( liste *);

#endif 
