FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

grad : grad.o 
	$(FC) $(OPT) grad.o -o grad 

clean:
	rm *.o
	

grad.o : grad.f
	$(FC) $(OPT) -c grad.f

