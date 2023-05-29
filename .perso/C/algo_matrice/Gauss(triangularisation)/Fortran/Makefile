FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

gauss : gauss.o 
	$(FC) $(OPT) gauss.o -o gauss 



clean:
	rm *.o
	

gauss.o : gauss.f
	$(FC) $(OPT) -c gauss.f



test : 
	cd src && $(FC) $(OPT) -c matrice.c
