#include <stdio.h>
#include <stdlib.h>

#define NBBoucles 4

int main() {

/*calcul de ln(10)*/
	double res, puiss1 = 1, puiss9 = 1; 
	int p;
	
	res = 2.1972; //ln(9) 
	for (p=1;p<=NBBoucles;p++) {
		puiss1 = puiss1 * -1;
		puiss9 = puiss9 * 9;
		res -= (puiss1 * 1./(p * puiss9)); //Le 1. sert car sinon cela effectue une division entière
				   }

	printf("%lf \n", res);
}
