#include <stdio.h>
#include "matrice.h"
#include "RK4.h"
#include "math.h"


int f(float,Tmatrice,Tmatrice *);

int f(float t, Tmatrice Y, Tmatrice * res){
	(*res).t[0][0] = cos(Y.t[0][0]); 
	return 1;
}


void main(){
	float t, dt;
	Tmatrice Y;

	Allouer(&Y,1,1);
	

	/* condition initiale */
	t = 0.;
	Y.t[0][0] = 1.;
	

	/* pas */
	dt = 0.01;
	
	printf("%f  %f \n",t,Y.t[0][0]);

	for(int i=0;i<1000;i++){
		RK4(t,&Y,dt,f);
		t+=dt;
		printf("%f  %f \n",t,Y.t[0][0]);
	}

	Desallouer(&Y);
}
