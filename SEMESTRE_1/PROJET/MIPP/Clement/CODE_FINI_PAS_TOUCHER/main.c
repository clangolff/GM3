/* gcc -c main.c   $(sdl2-config --cflags --libs)

gcc main.o liste.o instruction.o mysdl.o -o main $(sdl2-config --cflags --libs)


*/

#include <stdio.h>
#include <stdlib.h>
#include <SDL.h>

#include "liste.h"
#include "instruction.h"
#include "mysdl.h"


int main (int argc, char **argv){
	liste *l = listeVide();
	chaine ch;
	ajouterEnTete(&l,largeur / 2, hauteur  / 2, 1);
	printf("entrez les instructions\n");
	scanf("%s",ch);
	
	MaFonction(&l,ch);

	SDL_Affichage(l);
	liberer(l);
	return EXIT_SUCCESS;
}
