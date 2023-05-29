#include <stdio.h>

int main() {
	int n,i,doubleN,k;
	k = 0;
	do {
		scanf("%d",&n);
	}while (n < 0);
	doubleN = 2 * n;
	for (i = n; i <= doubleN; i++){
		printf("%d ",i);
		k++;
		if(k%10 == 0){
			printf("\n");
		}
	} 
}
