#include <stdio.h>
#define MAX 200

typedef char chaine[MAX];
typedef  chaine tabMot[5];
	
void inverser(tabMot, int);
void affiche(tabMot,int);

int main() {
	
	chaine c,M1, M2, M3, M4, M5;
	tabMot t;
	int n = 5;
	printf("entrez les mots\n");
	fgets(c,MAX-1,stdin);
	int i = 0;
	int k = 0;
	int j = 0;
	while((k<MAX) && (j<MAX) && (c[k] != '\0') && (c[k] != '\n') && (i<n)){
		if(c[k] == ' '){
			t[i][j] = '\0';
			i++;
			j=0;
		}
		t[i][j] = c[k];
		k++;
		j++;
	}
	affiche(t,i+1);	

	inverser(t,i);

	affiche(t,i+1);
}

void affiche(tabMot t, int n){
	for(int i=0;i<n;i++){
		printf("%s",t[i]);
	} 
	printf("\n");
}

void inverser(tabMot t , int n){
	chaine *p = t, *q = &t[n-1];
	chaine temp;
	while (p < q) {
		temp = *p;
		*p++ = *q;
		*q-- = temp;
	}
}
/*
 on peut pas faire ca car c'est des tableaux statiques, on ne peut pas toucher aux adresse just au element stocké
 */
/*for(int i=0;i<n;i++){
		temp = &t[i];
		t[i] = &t[n-i];
		t[n-i] = &temp;
	}*/
