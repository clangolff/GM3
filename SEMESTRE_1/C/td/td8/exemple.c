#include <stdio.h>

typedef char chaine[30];

int main(){
	chaine c;
	printf("entrez chaine\n");
	fgets(c,29,stdin);
	printf("%s",c);
}
