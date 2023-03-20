FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

triangleInf : triangleinf.o matrice.o
	$(FC) $(OPT) triangleinf.o matrice.o -o triangleInf


triangleSup : trianglesup.o matrice.o
	$(FC) $(OPT) trianglesup.o matrice.o -o triangleSup
clean:
	rm *.o
	

triangleinf.o : triangleinf.c matrice.h
	$(FC) $(OPT) -c triangleinf.c

trianglesup.o : trianglesup.c matrice.h
	$(FC) $(OPT) -c trianglesup.c

matrice.o : matrice.c matrice.h
	$(FC) $(OPT) -c -lm matrice.c



test : 
	cd src && $(FC) $(OPT) -c matrice.c
