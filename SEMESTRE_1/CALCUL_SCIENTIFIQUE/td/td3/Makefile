#FC = f77
FC = gfortran
PC = fpc

#OPT = -O
OPT = -g

# aniversaire
ani: ani.f
	$(FC) $(OPT) ani.f -o ani
# cnp
cnp: cnp.f
	$(FC) $(OPT) cnp.f -o cnp

# eqt 2nd degre 4 octets
eq: eq.f
	$(FC) $(OPT) eq.f -o eq

# eqt 2nd degre 8 octets
eq2: eq2.f
	$(FC) $(OPT) eq2.f -o eq2

# zero Pascal
pascalzero : pascalzero.pas
	$(PC) $(OPT) pascalzero.pas 

# zero machine 4 octets
zero: zero.f
	$(FC) $(OPT) zero.f -o zero

# zero machine 8 octets
zero2: zero2.f
	$(FC) $(OPT) zero2.f -o zero2

# precision machine 4 octets
prec: prec.f
	$(FC) $(OPT) prec.f -o prec

clean:
	rm cnp prec zero eq zero2 eq2
