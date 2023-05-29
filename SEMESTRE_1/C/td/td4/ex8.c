#include <stdio.h>

int factorielle(int);

int main(){
	long int n,res;
	printf("entrez nombre pour factorielle\n");
	scanf("%d",&n);
	res = factorielle(n);
	printf("la factorielle de %d = %d \n",n,res);
}

int factorielle(int n){
	if((n==1) || (n==0)) return 1;
	else return n*factorielle(n-1);
}
