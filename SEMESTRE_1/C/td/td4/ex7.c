#include <stdio.h>
#define Taille 100
int main(){
	int i,max,t[Taille],k;
	k=0;
	do {
		printf("donnez le nombre d'entier à traiter\n");
		scanf("%d",&max);
	} while (max>Taille);
	for(i=0;i<max;i++){
		scanf("%d",&t[i]);
		if(t[i]%9==0) k++; 
	}
	printf("il y a %d nombre divisible par 9\n",k);
}
