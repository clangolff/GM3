#include "fonction4et5.h"
#include <stdio.h>
void divisiblepar7(){
	int a,b,i;
	printf("entrez 2 entiers \n");
	scanf("%d%d",&a,&b);
	for(i=a;i<=b;i++){
		if (i%7 == 0) {
		printf("%d \n",i);
		}
	}
}

void nombreConsecutif(){
	int n,i,doubleN,k;
	k = 0;
	do {
		scanf("%d",&n);
	}while(n<0);
	doubleN = 2*n;
	for(i=n;i<=doubleN;i++){
		printf("%d ",i);
		k++;
		if (k%10==0){
			printf("\n");
		}
	}
}
