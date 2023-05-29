#include <stdio.h>
#include <stdlib.h>

#define NBBoucles 4

int main() {
	int i; 
	double x;
	 
	scanf("%lf",&x);

/*calcul des coeffcients bn de la somme*/
	double lambda[NBBoucles+1];
	int puiss10 = 1; 

	for (i=0;i<NBBoucles+1;i++) {
		lambda[i] = 1.0/(puiss10);
		puiss10 = puiss10 * -10;
				    }

/*calcul de (10+x)/(101+20x) en appliquant l'algorithme de Clenshaw*/
	int n = NBBoucles;
	double c[n-1]; 
	double res, twox = 2 * x;
	 
	c[n-2]=lambda[n];
	c[n-3]=lambda[n-1]+ twox*c[n-2];
	for(i=n-2; i>=2 ; i--){
		c[i-2]=lambda[i]+twox*c[i-1]-c[i];
	}
	res=(0.1)*((lambda[1]-c[1]+twox*c[0])*x+(lambda[0]-c[0]));

	printf("%.16lf \n", res);
}
