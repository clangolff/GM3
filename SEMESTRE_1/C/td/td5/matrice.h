#define MAX 100

typedef float  Matrice[MAX][MAX];

void créerMatrice(Matrice,int,int);
void remplir(Matrice,int,int);
void affiche(Matrice,int,int);

float sumElement(Matrice,int,int);

int  multMatrice(Matrice,int,int,Matrice,int,int,Matrice,int *,int *); 
