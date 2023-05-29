#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int nbelmt;
	double *coeff;
	} Tab;
	
int main() {
	Tab lambda;
	double alpha;

/*initialisation*/
	scanf("%d",&lambda.nbelmt);
	lambda.coeff = (double*) malloc ((lambda.nbelmt+1) * sizeof(double));
	if(lambda.coeff != NULL){
		for(int i=0;i<=lambda.nbelmt;i++){
			scanf("%lf",&(lambda.coeff[i]));
			}
		}	 
	scanf("%lf",&alpha);


/*calcul*/
	Tab c;
	double res, twoalpha = 2 * alpha;
	int i;
	int n = lambda.nbelmt;
	 
		c.nbelmt=n-1;
		c.coeff = (double*) malloc ((c.nbelmt) * sizeof(double));
		c.coeff[n-2]=lambda.coeff[n];
		c.coeff[n-3]=lambda.coeff[n-1]+ twoalpha*c.coeff[n-2];
			for(i=n-2; i>=2 ;i=i-1) {
				c.coeff[i-2]=lambda.coeff[i]+twoalpha*c.coeff[i-1]-c.coeff[i];
			}
		res=(lambda.coeff[1]-c.coeff[1]+2*alpha*c.coeff[0])*alpha+(lambda.coeff[0]-c.coeff[0]);

	printf("%.16lf \n", res);
}
