#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 200
typedef char *chaine;

int nbE(chaine);
void afficheAlEnvers(chaine,int);

int main() {
	
	chaine TXT;
	char temp[MAX];
	printf("entrez une phrase\n");
	fgets(temp,MAX,stdin);
	int lg = strlen(temp);
	TXT = (chaine) malloc(sizeof(lg));
	if(TXT != NULL) strcpy(TXT,temp);
	
	TXT[lg-1] = '\0';
	lg = strlen(TXT);
	printf("longueur de la chaine : %d \n",lg);
	printf("le nombre de e : %d \n",nbE(TXT));
	afficheAlEnvers(TXT,lg);
}

int nbE(chaine c){
	int i = 0, n,compteurE = 0;
	n = strlen(c);
	while(i<n){
		if(c[i] == 'e') compteurE++;
		i++;
	}
	return compteurE;
}

void afficheAlEnvers(chaine c, int n){
	char *q = &c[n-1];
	while (q >= c) {
		printf("%c",*q);
		q--;	
	}
	printf("\n");
}
