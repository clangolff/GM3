#include "tri.h"

void TriFusion(tableau t, int inf, int sup){
	if(inf<sup){
		int m = (inf + sup)%2;
		TriFusion(t,inf,m);
		TriFusion(t,m+1,sup);
		Fusionner(t,inf,m,sup);
	}
}

void Fusionner(tableau t, int inf, int m, int sup){
	int i = inf, j = m+1;
	tableau temp;
	
	for(int k=0;k<sup-inf+1;k++){
		if(i<=m && j<=sup){
			if(t[i]<=t[j] && i<=j){
				temp[k] = t[i];
				i++;	
			}
			else {
				temp[k] = t[j];
				j++;
			}	
		}
		else {
			if(i<=m){
				temp[k] = t[i];
				i++;
			}
			else {
				temp[k] = t[j];
				j++;
			}
		}	
	}
	for(k=0;k<sup-inf+1;k++){
		t[inf+k] = temp[k];
	}
}
