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
	if(p.coeff != NULL){
		for(int i=0;i<=p.deg;i++){
			scanf("%lf",&(p.coeff[i]));
			}
		}	 
	scanf("%lf",&alpha);

/*calcul*/
	Tpolynome q;
	double *res;
	long int fact = 1;
	int n = p.deg;

	q.deg = n;
	q.coeff = (double*) malloc ((n+1) * sizeof(double));
	if(q.coeff != NULL) {
	
		res = (double*) malloc ((n+1) * sizeof(double));
	 	/*rajouter manip EXIT_FAILURE plus tard*/
		
		q.coeff[n] =  p.coeff[n];
	
		for(int i=n-1;i>=0;i--){
			q.coeff[i] = p.coeff[i] + alpha * q.coeff[i+1];
			}
		res[0] = q.coeff[0];

		for(int i=1;i<=n+1;i++) {
			for (int j=n-1;j>i-1;j--) {
				q.coeff[j] = q.coeff[j] + alpha * q.coeff[j+1];
				}	
			res[i] = fact * q.coeff[i];
			fact=fact*(i+1);
			}

/*résultat*/	
		for(int i=0;i<=n;i++){
			printf("derivé %d en %f : %.16f \n", i,alpha,res[i]);
			}	
		}	
	}	
