#include <stdio.h>
#include <stdlib.h>


typedef struct {
	int deg;
	double *coeff;
	} Tpolynome;

int main() {
	Tpolynome p;
	double alpha;

/*initialisation*/
	scanf("%d",&p.deg);
	p.coeff = (double*) malloc ((p.deg+1) * sizeof(double));
	for(int i=0;i<=p.deg;i++){
		scanf("%lf",&(p.coeff[i]));
		}
	scanf("%lf",&alpha);
	

/*calcul */
	Tpolynome q;
	int n = p.deg;
	
	q.deg = n;
	q.coeff =(double*) malloc ((n+1) * sizeof(double));
	q.coeff[n] = p.coeff[n];
	
	for(int i=n-1;i>=0;i--){
		q.coeff[i] = p.coeff[i] + alpha * q.coeff[i+1];
		}

/*ecriture  resultat*/
	printf("alpha : %.16f P(aplha) =  %.16f \n",alpha,q.coeff[0]);	
	}
