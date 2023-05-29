FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

gauss : gauss.o 
	$(FC) $(OPT) gauss.o -o gauss 

gaussMaxpiv : gaussMaxpiv.o 
	$(FC) $(OPT) gaussMaxpiv.o -o gaussMaxpiv 


clean:
	rm *.o
	

gauss.o : gauss.f
	$(FC) $(OPT) -c gauss.f

gaussMaxpiv.o : gaussMaxpiv.f
	$(FC) $(OPT) -c gaussMaxpiv.f

test : 
	cd src && $(FC) $(OPT) -c matrice.c
