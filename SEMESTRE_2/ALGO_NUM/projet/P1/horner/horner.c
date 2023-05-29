#include <stdio.h>
#include <stdlib.h>


typedef struct {
	int deg;
	float *coeff;
	} Tpolynome;

int main() {
	Tpolynome p;
	float alpha;

/*initialisation*/
	scanf("%d",&p.deg);
	p.coeff = (float*) malloc ((p.deg+1) * sizeof(float));
	for(int i=0;i<=p.deg;i++){
		scanf("%f",&(p.coeff[i]));
		}
	scanf("%f",&alpha);
	

/*calcul */
	Tpolynome q;
	int n = p.deg;
	
	q.deg = n;
	q.coeff =(float*) malloc ((n+1) * sizeof(float));
	q.coeff[n] = p.coeff[n];
	
	for(int i=n-1;i>=0;i--){
		q.coeff[i] = p.coeff[i] + alpha * q.coeff[i+1];
		}

/*ecriture  resultat*/
	printf("alpha : %.16f P(alpha) = %.16f \n",alpha,q.coeff[0]);	
	}
