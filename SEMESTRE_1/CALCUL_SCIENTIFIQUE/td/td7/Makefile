FC = gfortran

OPT = -g -O0
#OPT = -g -fbounds-check

#a debugger
exe : exe.f
	$(FC) exe.f $(OPT) -o exe

#gauss pivot sur hilbert
gauss : gauss.f
	$(FC) gauss.f $(OPT) -o gauss

#gauss2 pivot sur hilbert double precision
gauss2 : gauss2.f
	$(FC) gauss2.f $(OPT) -o gauss2



td7 : td7.tex
	pdflatex td7
	pdflatex td7
	evince td7.pdf &

clean:
	rm *.o exe gauss gauss2




