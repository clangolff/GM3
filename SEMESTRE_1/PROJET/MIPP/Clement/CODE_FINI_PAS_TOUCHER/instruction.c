#include "instruction.h"
#include <stdio.h>
#include "liste.h"
#include <stdlib.h>
#define tailleTrait 30

int estUneDirection(char x)
{
	return(x == 'N' || x == 'S' || x == 'E' || x == 'O');
}
	
int estUnModeDecriture(char x)
{
	return(x == 'L' || x == 'B');
}	

int estUnChiffre(char x)
{
	return(x >= '0' && x <= '9');
}

int longueur( chaine c ) {
	int res = 0;
	while ( c[res] != '\0') res ++;
	return res;  
}

instruction LireChaine(chaine c, int *instructionEntreParentheses, int *chiffreAvant)
{
	const instruction instructionNulle = {0, "",0};
	instruction sous_instruction = instructionNulle;
	int i = 0;
	int k = 0;
	int n = longueur(c);
	char x = c[i];
	int nbrep = 0;
	int nbparenthese = 0;
	
	if(x != '\0')
	{
		if(estUneDirection(x) || estUnModeDecriture(x))
		{
			sous_instruction.lg = 1;
			sous_instruction.rep = 1;
			sous_instruction.c[0] = x;
		}
		else
		{
			while(estUnChiffre(x) && (i + k) < n)
			{
				*chiffreAvant = 1;
				nbrep = nbrep * 10 + (int)(x) - 48;	
				k++;
				x = c[i+k];
			}
			if((i + k) >= n)
			{
				printf("erreur aucune instruction\n");
				exit(EXIT_FAILURE);
			}
			else
			{
				sous_instruction.rep = nbrep;
				i += k;
				k = 0;
				if(estUneDirection(x) || estUnModeDecriture(x))
				{
					sous_instruction.lg = 1;
					sous_instruction.c[0] = x;
				}
				else
				{	
					if(x == '(' )
					{
						*instructionEntreParentheses = 1;
						nbparenthese = 1;
						while(nbparenthese != 0 && i < n)
						{
							i++;
							x = c[i];
							if(x == '(')
								nbparenthese++;
							if(x == ')')
								nbparenthese--;
							if(nbparenthese != 0)
							{
								sous_instruction.c[k] = x;
								sous_instruction.lg++;
								k++;
							}
						}
						if(i >= n)
						{
							printf("erreur il manque une parenthese\n");
							exit(EXIT_FAILURE);
						}
					}	
					else
					{
						printf("erreur caractère %c inconnu\n", x);
						exit(EXIT_FAILURE); 	
					}
				}
			}
		}
	}
	else
	{
		printf("erreur chaine vide\n");
		exit(EXIT_FAILURE);
	}
	return(sous_instruction);
}		

void remplirListe(liste **p,char x,int n){
	liste *l = *p;
	if ( !(estVide(l)) ) {
		TypeCoordonnée coord = obtenirCoord(l);
		switch(x){
			case 'E' : 	ajouterEnTete( &l , coord.x + n * tailleTrait, coord.y , (*l).modeEcriture ); break;
			case 'O' : 	ajouterEnTete( &l , coord.x - n * tailleTrait,  coord.y , (*l).modeEcriture ); break;
			case 'N' : 	ajouterEnTete( &l , coord.x , coord.y - n * tailleTrait, (*l).modeEcriture ); break;
			case 'S' : 		ajouterEnTete( &l , coord.x , coord.y + n * tailleTrait , (*l).modeEcriture ); break;  /*inversion de + et - pour nord et sud car repere  en haut a gauche  →   ↓*/
			case 'L' : 		ajouterEnTete( &l , coord.x , coord.y  , 0 ); break;
			case 'B' :		ajouterEnTete( &l , coord.x , coord.y  , 1 ); break; 
		}
	*p = l;	
	}
} 

void MaFonction(liste **l,chaine ch){
	liste *p = *l;
	char *ch_suiv;
	chaine chiffres;  /*pour stocker dans une chaine les chiffre et envoyer dans longeur*/
	int indiceChaine = 0; 
	int instructionEntreParentheses = 0; /*booleen our savoir si l'instruction etait entre parenthese*/
	int chiffresAvant = 0;  /*booleen pour savoir si il y avait des chiffres avant l'instruction*/
	
	
	if(ch != "") {
		instruction sous_instruction = LireChaine(ch,&instructionEntreParentheses,&chiffresAvant);
		if (sous_instruction.lg > 1) {
			for(int i=0;i<sous_instruction.rep;i++) {
				MaFonction(&p,sous_instruction.c);
				*l = p;
			}
		}
		else {
			remplirListe(&p,sous_instruction.c[0],sous_instruction.rep);
			*l = p;
			}
		indiceChaine = sous_instruction.lg;
			
		if(chiffresAvant) {
			sprintf(chiffres,"%d",sous_instruction.rep);   
			indiceChaine += longueur(chiffres);
		}
			
		if(instructionEntreParentheses) {
			indiceChaine += 2;
		}
			
		if (ch[indiceChaine] != '\0' ){
				ch_suiv =  &ch[indiceChaine];  
				MaFonction(&p,ch_suiv);
				*l = p;
		}			
	}
}
