#include "RK4.h"
#include "matrice.h"



/*t  vecteur  dt  f(t,Y) */
int RK4(float t, Tmatrice * Y, float dt,int (*f)(float, Tmatrice, Tmatrice *)){
	Tmatrice K1,K2,K3,K4,K;
	Tmatrice Yb,Yc,Yd;
	int n = (*Y).nbL;

	/* Allocation */
	Allouer(&K1,n,1);
	Allouer(&K2,n,1);
	Allouer(&K3,n,1);
	Allouer(&K4,n,1);
	Allouer(&Yb,n,1);
	Allouer(&Yc,n,1);
	Allouer(&Yd,n,1);
	Allouer(&K,n,1);

	/* copie de Y */
	Add(&Yb,*Y);
	Add(&Yc,*Y);
	Add(&Yd,*Y);
	
	/*  K1  */
	f(t,*Y,&K1);
	
	/*conservation de K1*/
	Add(&K,K1);

	/*  K2  */ 
	Mult(dt*0.5,&K1);
	Add(&Yb,K1);	
	f(t+dt*0.5,Yb,&K2);

	/*conservation de K2*/
	Mult(2.,&K2);
	Add(&K,K2);

	/*  K3  */
	Mult(dt*0.25,&K2);
	Add(&Yc,K2);
	f(t+dt*0.5,Yc,&K3);

	/*conservation de K3*/
	Mult(2.,&K3);
	Add(&K,K3);


	/*  K4  */
	Mult(dt*0.5,&K3);
	f(t+dt,Yd,&K4);
		
	/*conservation de K4*/
	Add(&K,K4);

	/*  moyenne */
	Mult(dt/6,&K);
	Add(Y,K);


	/* Desallocation */
	Desallouer(&K1);
	Desallouer(&K2);
	Desallouer(&K3);
	Desallouer(&K4);
	Desallouer(&Yb);
	Desallouer(&Yc);
	Desallouer(&Yd);
	Desallouer(&K);
}
