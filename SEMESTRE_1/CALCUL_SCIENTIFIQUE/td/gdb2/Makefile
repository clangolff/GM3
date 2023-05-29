FC = gfortran

OPT = -g -O0
#OPT = -g -fbounds-check


#gauss2 pivot sur hilbert double precision
gauss2 : gauss2.f
	$(FC) gauss2.f $(OPT) -o gauss2


td9 : td9.tex
	pdflatex td9
	pdflatex td9
	evince td9.pdf &

# LU
lu : mlu.o downup.o lu.o 
	$(FC) $(OPT) mlu.o downup.o lu.o -o lu

#compilation des objets  
mlu.o : mlu.f 
	$(FC) $(OPT) mlu.f -c


lu.o : lu.f
	$(FC) $(OPT)  lu.f -c 

downup.o : downup.f
	$(FC) $(OPT)  downup.f -c


clean:
	rm *.o lu gauss2

