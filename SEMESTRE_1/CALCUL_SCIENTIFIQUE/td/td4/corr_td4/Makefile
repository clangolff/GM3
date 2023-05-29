FC=gfortran
OPT=-g

#edition de liens (on rassemble les objets)
#
# aire du parallelograme entre 2 vecteurs
air : air.o vprod.o
	$(FC) $(OPT) air.o vprod.o -o air

# volume du parallelipipede fait par 3 vecteurs
vol : vol.o vprod.o
	$(FC) $(OPT) vol.o vprod.o -o vol

#-------------------

# angle entre 2 vecteurs
ang : ang.f
	$(FC) $(OPT) ang.f -o ang

#compilation des objets pour les prog air, vol 
vprod.o:vprod.f
	$(FC) $(OPT) vprod.f -c 

air.o:air.f
	$(FC) $(OPT) air.f -c

vol.o:vol.f
	$(FC) $(OPT) vol.f -c

#on crée une option pour enlever les executables et les objets
#pour la mobilité inter-machine
clean:
	rm *.o  ang air  vol 
