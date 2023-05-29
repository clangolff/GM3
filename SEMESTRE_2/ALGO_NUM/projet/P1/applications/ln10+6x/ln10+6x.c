#include <stdio.h>
#include <stdlib.h>

#define NBBoucles 7

int main() {
	int i; 
	double x;
	 
	scanf("%lf",&x);

/*calcul des coeffcients bn de la somme*/
	double lambda[NBBoucles+1];
	int puiss3 = -1; 

	lambda[0] = 2.19722; //ln(9) à 10e-5

	for (i=1;i<NBBoucles+1;i++) {
		puiss3 = puiss3 * -3;
		lambda[i] = 2.0/(puiss3*i);
				    }

/*calcul de ln(10+6x) en appliquant l'algorithme de Clenshaw*/
	int n = NBBoucles;
	double c[n-1]; 
	double res, twox = 2 * x;
	 
	c[n-2]=lambda[n];
	c[n-3]=lambda[n-1]+ twox*c[n-2];
	for(i=n-2; i>=2 ;i=i-1){ 
		c[i-2]=lambda[i]+twox*c[i-1]-c[i];
	}
	res=(lambda[1]-c[1]+twox*c[0])*x+(lambda[0]-c[0]);

	printf("%lf \n", res);
}
