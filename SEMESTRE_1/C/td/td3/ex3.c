#include <stdio.h> 

int main(){
char c;
printf("entrez votre caractère \n");
scanf("%c",&c);
if (!(c >= 'A' && c <= 'Z')) {
	printf("le caractère n'est pas une majuscule \n");
	printf("voici la conversion en majuscule %c \n",c + 'A' - 'a');
	}
	else {
	printf("le caractère est une majuscule \n");
	}
}
