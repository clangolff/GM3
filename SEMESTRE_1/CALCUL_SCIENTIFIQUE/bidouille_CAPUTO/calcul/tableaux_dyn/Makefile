FC = gfortran

OPT = -g

#---------executables------------------
# syst triang < 
down : mdown.o down.o
	$(FC) $(OPT) mdown.o down.o -o down

down2 : mdown2.o down2.o
	$(FC) $(OPT) mdown2.o down2.o -o down2

# inversion matrice triang < 
inve : minve.o inve.o
	$(FC) $(OPT) minve.o inve.o -o inve

#test matmul
mm : mm.f
	$(FC) $(OPT)  mm.f -o mm

#---------objets------------------

minve.o : minve.f
	$(FC) $(OPT)  minve.f -c

inve.o : inve.f
	$(FC) $(OPT)  inve.f -c

print_inve :
	cat minve.f inve.f minve.m inve.m > print_inve


mdown.o : mdown.f
	$(FC) $(OPT)  mdown.f -c

down.o : down.f
	$(FC) $(OPT)  down.f -c

mdown2.o : mdown2.f
	$(FC) $(OPT)  mdown2.f -c

down2.o : down2.f
	$(FC) $(OPT)  down2.f -c

clean :
	rm mm down down2 inve *o


