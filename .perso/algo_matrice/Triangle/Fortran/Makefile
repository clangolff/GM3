FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

triangleInf : triangleInf.o 
	$(FC) $(OPT) triangleInf.o  -o triangleInf


triangleSup : triangleSup.o 
	$(FC) $(OPT) triangleSup.o -o triangleSup
clean:
	rm *.o
	

triangleInf.o : triangleInf.f 
	$(FC) $(OPT) -c triangleInf.f

triangleSup.o : triangleSup.f 
	$(FC) $(OPT) -c triangleSup.f



test : 
	cd src && $(FC) $(OPT) -c matrice.c
