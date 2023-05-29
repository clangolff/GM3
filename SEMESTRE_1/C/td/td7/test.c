#include <stdio.h>

int main(){
	int *p,*q,a,b;
	a = 1; 
	b = 5;
	p = &a;
	q = &b;
	q = *&p;
	printf("%d \n",*q);
}
