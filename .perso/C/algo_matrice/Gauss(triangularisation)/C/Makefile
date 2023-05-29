FC = gcc

#OPT = -O
#OPT = -p
OPT = -g

gauss : gauss.o matrice.o
	$(FC) $(OPT) gauss.o matrice.o -o gauss -lm



clean:
	rm *.o
	

gauss.o : gauss.c matrice.h
	$(FC) $(OPT) -c gauss.c


matrice.o : matrice.c matrice.h
	$(FC) $(OPT) -c  matrice.c -lm



test : 
	cd src && $(FC) $(OPT) -c matrice.c
