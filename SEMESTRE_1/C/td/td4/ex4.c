#include <stdio.h>

int main() {
	int a,b,i;
	printf("entrez 2 entiers\n");
	scanf("%d%d",&a,&b);
	for(i=a;i<=b;i++) {
		if(i%7 == 0) {
		printf("%d \n",i);
		}
	}		
}
