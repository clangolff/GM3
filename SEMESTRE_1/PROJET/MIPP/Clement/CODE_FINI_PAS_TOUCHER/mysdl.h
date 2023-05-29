/* gcc -c mysdl.c mysdl.h $(sdl2-config --cflags --libs) */


#ifndef mysdl_h
#define mysdl_h

#include <SDL.h>
#include "liste.h"


#define largeur 800
#define hauteur 600


void SDL_ExitWithError(const char *message);

void SDL_Initialisation(SDL_Window **, SDL_Renderer **, int , int);

void SDL_Destruction(SDL_Window ** , SDL_Renderer **);

void SDL_MiseAJourRendu(SDL_Renderer **);

void SDL_EffaceRendu(SDL_Renderer **);

void SDL_Ligne(SDL_Renderer **, int ,int, int, int);

void SDL_SetColor(SDL_Renderer **, int, int, int, int);

void SDL_Affichage(liste *);


#endif
