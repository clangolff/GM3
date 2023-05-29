#include <stdio.h>
#include <math.h>


float dérivé(float);



int main(){
	float epsilon, res, x;
	
	
	scanf("%f%f",&x,&epsilon);
	
	res = dérivé(x,epsilon,&cos);
	
	printf("la dérivé de cos en x : %.2f \n", res);
}

float dérivé( float x, float epsilon, float (*f)(float) ){
	float res = *(f)(x+epsilon) - *(f)(x-epsilon)/(2*epsilon);
	return res;
}
