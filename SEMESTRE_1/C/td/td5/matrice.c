#include <stdio.h>
#include "matrice.h"

void créerMatrice(Matrice mat,int n, int p){
	for(int i=0;i<n;i++){
		for(int j=0;j<p;j++){
			mat[i][j]=0.0;
		}	
	}
	
}

void remplir(Matrice mat,int n, int p){
	float x;
	printf("remplir matrice ligne par ligne \n");
	for(int i=0;i<n;i++){
		for(int j=0;j<p;j++){
			scanf("%f",&mat[i][j]);
		}	
	}
	affiche(mat,n,p);
}


void affiche(Matrice mat, int n, int p){
	for(int i=0;i<n;i++){
		for(int j=0;j<p;j++){
			printf("%.2f ",mat[i][j]);
		}
		printf("\n");
	}
}

float sumElement(Matrice mat, int n, int p){
	float res=0.0;
	for(int i=0;i<n;i++){
		for(int j=0;j<p;j++) res += mat[i][j];
	}
	return res;
}

int multMatrice(Matrice A, int n1,int p1, Matrice B, int n2, int p2,Matrice C,int *n3, int *p3){
	float sum;
	if(p1 != n2){
		printf("produit impossible \n");
		return 0;  
	}
	else{
		*n3 = n1;
		*p3 = p2;
		créerMatrice(C,*n3,*p3);
		for(int i=0;i<n1;i++){
			for(int j=0;j<p2;j++){
				sum = 0;
				for(int k=0;k<p1;k++){
					sum += A[i][k]*B[k][j];
				}
				C[i][j] = sum;
			}		
		}
	return 1;
	}
}
