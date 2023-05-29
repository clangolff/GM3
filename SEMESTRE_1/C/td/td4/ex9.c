#include <stdio.h>
#define MAX 50
int main(){
	char c,chaine[MAX];
	int i = 0;
	printf("entrez des caractères \n");
	do {
		c = getchar();
		chaine[i] = c;
		i++;
		getchar();
	}while (!(c == '.' || i>=MAX));
	chaine[i] = '\0';
	printf("la longueur de %s est %d \n",chaine,i);
}
