FC = gcc

#OPT = -O
#OPT = -p
OPT = -g

grad : grad.o matrice.o
	$(FC) $(OPT) grad.o matrice.o -o grad -lm



clean:
	rm *.o
	

grad.o : grad.c matrice.h
	$(FC) $(OPT) -c grad.c


matrice.o : matrice.c matrice.h
	$(FC) $(OPT) -c  matrice.c -lm



test : 
	cd src && $(FC) $(OPT) -c matrice.c
