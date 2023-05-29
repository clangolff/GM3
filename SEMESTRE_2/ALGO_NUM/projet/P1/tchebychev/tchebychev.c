#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int nbelmt;
	float *coeff;
	} Tab;
	
int main() {
	Tab lambda;
	float alpha;

/*initialisation*/
	scanf("%d",&lambda.nbelmt);
	lambda.coeff = (float*) malloc ((lambda.nbelmt+1) * sizeof(float));
	if(lambda.coeff != NULL){
		for(int i=0;i<=lambda.nbelmt;i++){
			scanf("%f",&(lambda.coeff[i]));
			}
		}	 
	scanf("%f",&alpha);


/*calcul*/
	Tab c;
	float res, twoalpha = 2 * alpha;
	int i;
	int n = lambda.nbelmt;
	 
	c.nbelmt=n-1;
	c.coeff = (float*) malloc ((c.nbelmt) * sizeof(float));
	c.coeff[n-2]=lambda.coeff[n];
	c.coeff[n-3]=lambda.coeff[n-1]+ twoalpha*c.coeff[n-2];
	for(i=n-2; i>=2 ;i=i-1) {
		c.coeff[i-2]=lambda.coeff[i]+twoalpha*c.coeff[i-1]-c.coeff[i];
			}
	res=(lambda.coeff[1]-c.coeff[1]+2*alpha*c.coeff[0])*alpha+(lambda.coeff[0]-c.coeff[0]);

	printf("%.16f \n", res);
}
