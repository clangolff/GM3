#ifndef matrice_h
#define matrice_h
#include <stdio.h>
typedef struct matrice{
  double **t;
  int nbL,nbC;
  }Tmatrice;

int Allouer(Tmatrice *,int,int);  
int Remplir(Tmatrice *);
int Affiche(Tmatrice);
int Matmul(Tmatrice,Tmatrice,Tmatrice *);
double Dot_product(Tmatrice,Tmatrice);
double Norm2(Tmatrice,Tmatrice);
int Add(Tmatrice *,Tmatrice);
int Mult(double,Tmatrice *);
int Desallouer(Tmatrice *);
#endif
