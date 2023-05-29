#include <stdio.h>

int echange(int *,int *);

int main(){
	int i,j;
	printf("entrez valeur à echanger \n");
	scanf("%d%d",&i,&j);
	if(echange(&i,&j)) printf("échanger en %d et %d \n", i,j);
	else printf("erreur echange");
}

int echange(int *p1,int *p2){
	int temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
	return 1;
}
