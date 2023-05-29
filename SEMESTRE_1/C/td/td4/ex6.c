#include <stdio.h>
#include "fonction4et5.h"

int main(){
	char n;
	printf("entrez a pour divisiblePar 7 ou b pour nombre consecutif\n");
	do {
		scanf("%c",&n);
		switch(n){
			case 'a' : divisiblepar7();break;
			case 'b' : nombreConsecutif();break;
			case 'q' : break;
		}
	} while(n != 'q'); 
}
