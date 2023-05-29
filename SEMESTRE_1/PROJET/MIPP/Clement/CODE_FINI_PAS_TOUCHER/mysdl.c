#include <SDL.h>
#include "mysdl.h"
#include "liste.h"



void SDL_ExitWithError(const char *message){
	SDL_Log("erreur : %s > %s \n", message, SDL_GetError());
	exit(EXIT_FAILURE);
}


void SDL_Initialisation(SDL_Window **window , SDL_Renderer **renderer, int width, int height) {
	
	if(SDL_Init(SDL_INIT_VIDEO)!=0) SDL_ExitWithError("Initialisation SDL");

	*window = SDL_CreateWindow("fenetre 1", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width , height ,0);
	if(*window == NULL) SDL_ExitWithError("création fenêtre échouée");
	
	*renderer = SDL_CreateRenderer(*window,-1,SDL_RENDERER_SOFTWARE);
	if(*renderer == NULL) SDL_ExitWithError("création rendu échouée");
	

}


void SDL_Destruction(SDL_Window **window , SDL_Renderer **renderer){
	SDL_DestroyRenderer(*renderer);
	SDL_DestroyWindow(*window);
	SDL_Quit();
	}
	
	
void SDL_MiseAJourRendu(SDL_Renderer **renderer){
	SDL_RenderPresent(*renderer); 
}

void SDL_EffaceRendu(SDL_Renderer **renderer){
	if(SDL_RenderClear(*renderer) !=0) SDL_ExitWithError("effacement rendu échouée");
}

void SDL_Ligne(SDL_Renderer **renderer , int xa , int ya , int xb , int yb){

	if(SDL_RenderDrawLine(*renderer , xa , ya, xb, yb) != 0 ) SDL_ExitWithError("impossible de dessiner la ligne");
}

void SDL_SetColor(SDL_Renderer **renderer, int r, int g ,int b, int transparence){
	if(SDL_SetRenderDrawColor(*renderer , r , g , b , transparence) != 0 ) SDL_ExitWithError("impossible de changer la couleur du rendu");
}

void SDL_Affichage(liste *l){
	/*int tailleTrait = 5;*/
	liste *succ;
	SDL_Window *window = NULL;	
	SDL_Renderer *renderer= NULL;
	
	SDL_Initialisation( &window , &renderer, largeur , hauteur);
	
	/*_______________________________*/
	
	SDL_SetColor(&renderer,220,50,23,255);  /*  R,G,B,transparence  */
	
	
	while(!(estVide(l))){
		succ = (*l).succ;
		if ((*l).modeEcriture){
			if(!(estVide(succ))){
				SDL_Ligne(&renderer,(*l).coord.x ,(*l).coord.y,(*succ).coord.x ,(*succ).coord.y);
			}
		}
		l = succ;
	}	
	
	
	SDL_MiseAJourRendu(&renderer);
	
	SDL_EffaceRendu(&renderer);
	
	SDL_Delay(6000);
	/*_______________________________*/
	
	SDL_Destruction( &window , &renderer );
}
