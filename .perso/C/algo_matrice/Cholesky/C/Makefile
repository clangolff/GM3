FC = gcc

#OPT = -O
#OPT = -p
OPT = -g

cholesky : cholesky.o matrice.o
	$(FC) $(OPT) cholesky.o matrice.o -o cholesky -lm



clean:
	rm *.o
	

cholesky.o : cholesky.c matrice.h
	$(FC) $(OPT) -c cholesky.c


matrice.o : matrice.c matrice.h
	$(FC) $(OPT) -c  matrice.c -lm



test : 
	cd src && $(FC) $(OPT) -c matrice.c
