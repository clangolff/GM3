
FC = gfortran
OPT = -g

all : comp td8


comp : comp.tex
	pdflatex comp
	pdflatex comp
	evince comp.pdf &


td8 : td8.tex
	pdflatex td8
	pdflatex td8
	evince td8.pdf &

clean : 
	rm test *dvi *aux *log
	


