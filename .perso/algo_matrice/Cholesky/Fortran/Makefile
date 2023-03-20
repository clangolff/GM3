FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

cholesky : cholesky.o 
	$(FC) $(OPT) cholesky.o -o cholesky 

clean:
	rm *.o
	

cholesky.o : cholesky.f
	$(FC) $(OPT) -c cholesky.f

