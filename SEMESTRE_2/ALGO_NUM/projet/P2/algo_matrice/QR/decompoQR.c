#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define LGMAX 20

typedef struct {
	int nl;
	int nc; 
	double** m; 
} Matrix;  

Matrix AllouerMatrix (int nl, int nc) {
	int i, j;
	Matrix A;
	
	A.nl = nl;
	A.nc = nc;
	A.m = (double**) malloc (nl * sizeof(double*));
	for (i=0; i<nl; i++) {
		A.m[i] = (double*) malloc (nc * sizeof(double));
	}
	
	return A; 
}

Matrix ReadMat (char fic[LGMAX]) {
	FILE* file = NULL;
	char chain[LGMAX];
	char nb[LGMAX][LGMAX];
	char* res = NULL;  
	Matrix Mat;
	int nl, nc, i, j;
    
	file = fopen(fic, "r");
    
	if (file != NULL) {
	        nl = atoi(fgets(chain, LGMAX, file)); 
	        nc = atoi(fgets(chain, LGMAX, file)); 
	        Mat = AllouerMatrix(nl, nc);
        
		for (i=0; i<Mat.nl; i++) {
	        	fgets(chain, LGMAX, file); 
            		res = strtok(chain, " ");
            	
            		for (j=0;j<Mat.nc;j++) {
                		strcpy(nb[j], res); 
                		Mat.m[i][j] = atof(nb[j]);            		
            			res = strtok(NULL, " "); 
            		}
        	}   
        fclose(file); 
	} 
    
	else {
	        printf("Failed to open %s \n", fic);
	}
    
	return Mat; 
}


double DotProduct (double* a, double* b, int nl) {
	int i;
	double res;  
	
	for (i=0; i<nl; i++) {
		res += a[i] * b[i]; 
	}
	
	return res; 
}

double* SubstractVector (double* a, double* b, int nl) { 
	int i;
	double* res = (double*)malloc(nl * sizeof(double));
	
	for (i=0; i<nl; i++)
		res[i] = a[i] - b[i]; 
		
	return res;  
}	

double* SumVector (double* a, double* b, int nl) { 
	int i; 
	double* res = (double*)malloc(nl * sizeof(double));
	
	for (i=0; i<nl; i++)
		res[i] = a[i] + b[i]; 
		
	return res;  
}

double* ProductNmbVector (double alpha, double* b, int nl) { 
	int i; 
	double* res = (double*)malloc(nl * sizeof(double));
	
	for (i=0; i<nl; i++)
		res[i] = alpha * b[i]; 
		
	return res;  
}

Matrix DeterminationQ (Matrix A, double* qchap) {
	Matrix Q;
	int i, j;   
	double* qchapi = (double*)malloc(A.nl * sizeof(double)); 
	double* inter = (double*)malloc(A.nl * sizeof(double));
	
	Q = AllouerMatrix(A.nl, A.nc); 
	
	for (i=0; i<Q.nc; i++) {
		qchapi = memset(qchapi, 0, A.nl * sizeof(double)); //réinitialise le vecteur qchapi
		for (j=0; j<i; j++) {
			inter = ProductNmbVector(DotProduct(A.m[i], Q.m[j], A.nl), Q.m[j], A.nl); 
			qchapi = SumVector(qchapi, inter, A.nl);
		}
		qchapi = SubstractVector(A.m[i], qchapi, A.nl);
		
		qchap[i] = sqrt(DotProduct(qchapi, qchapi, A.nl));
		Q.m[i] = ProductNmbVector(1./qchap[i], qchapi, A.nl);
	}
	
	return Q; 
}

Matrix DeterminationR (Matrix A, Matrix Q, double* qchap) {
	Matrix R; 
	int i, j; 
	 
	R = AllouerMatrix(A.nl, A.nc); 
	
	for(i=0; i<A.nl; i++) {
		for (j=0; j<i; j++) 
			R.m[j][i] = DotProduct(A.m[i], Q.m[j], A.nl); 
		R.m[i][i] = qchap[i];
		for (j=i+1; j<A.nl; j++) 
			R.m[j][i] = 0.; 
	}
	
	return R; 
}

void Display (Matrix A) {
	int i, j; 
	
	for (i=0; i<A.nl; i++) {
		for (j=0; j<A.nc; j++) {
			printf("%lf ", A.m[i][j]); 
			if (j == A.nc-1)
				printf("\n"); 
		}
	}
}

Matrix ProductMatrix(Matrix A, Matrix B) {
	Matrix C = AllouerMatrix(A.nl, B.nc);
    	int i, j, k;
	
	if (A.nc != B.nl) {
	        printf("Erreur: Le nombre de colonnes de la matrice A doit être égal au nombre de lignes de la matrice B.\n");
    	}
    	
    	else {
    		for (i = 0; i < A.nl; i++) {
    			for (j = 0; j < B.nc; j++) {
    			        double sum = 0.0;
    	        
    			        for (k = 0; k < A.nc; k++) {
    			        	sum += A.m[i][k] * B.m[k][j];
    			        }
    			        C.m[i][j] = sum;
    			}
    		}
    	}
	
	return C;
}

int main(int argc, char *argv[]) {
	
	Matrix A, Q, R;
	double* qchap = (double*)malloc(A.nl * sizeof(double)); //Pour conserver les normes des qi
	
	char *fic = argv[1];

	A = ReadMat(fic); 
	printf("Matrice A : \n"); 
	Display(A); 
	
	Q = AllouerMatrix(A.nl, A.nc); 
	R = AllouerMatrix(A.nl, A.nc); 
	
	Q = DeterminationQ(A, qchap); 
	R = DeterminationR(A, Q, qchap); 
	
	printf("\n Matrice Q : \n");
	Display(Q); 
	
	printf("\n Matrice R : \n");
	Display(R); 
	
	printf("\n Produit QR : \n"); 
	Matrix P = AllouerMatrix(Q.nc, R.nl);
	P = ProductMatrix(Q, R); 
	Display(P); 
}

