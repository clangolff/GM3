#include <stdio.h> 

int main(){
char c;
printf("entrez votre caractère \n");
scanf("%c",&c);
if (!(c >= 'a' && c <= 'z')) {
	printf("le caractère n'est pas une minuscule \n");
	printf("voici la conversion en minuscule %c \n",c + 'a' - 'A');
	}
	else {
	printf("le caractère est une minuscule \n");
	}
}
