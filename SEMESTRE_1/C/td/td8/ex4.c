#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 200
typedef char *chaine;

int nbE(chaine);
void enleveE(chaine,int);

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
	enleveE(TXT,lg);
	puts(TXT);
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

/*
void enleveE(chaine c,int n){
	chaine p = c,q;
	while(p[0] != '\0'){
		if(p[0] == 'e'){
			q = p + 1;
			p[0] = '\0';
			p = q;
			if (q[0] != '\0') {
			strcat(c,q);
			}
		}
		else {
		p++;
		}
	}
}

*/
void enleveE(chaine c,int n){
	chaine p = c;
	chaine q;
	while(p[0] != '\0'){
		if(p[0] == 'e'){
			p[0] = '\0';
			p++;
			int lg = strlen(p);
			q = (chaine) malloc(sizeof(lg+1));
			if (q != NULL) {
				strcpy(q,p);
				strcat(c,q);
				free(q);
			}
			p--;
		}
		else {
		p++;
		}
	}
}

