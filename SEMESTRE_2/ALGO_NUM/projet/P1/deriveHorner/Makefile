CC = gcc

OPT = -g

deriveHorner : deriveHorner.o 
	$(CC) $(OPT) deriveHorner.o -o deriveHorner
	@echo "executable crée !" 

deriveHorner.o : deriveHorner.c
	$(CC) $(OPT) -c deriveHorner.c 
	@echo "objets crées !"

deriveHornerd : deriveHornerd.o 
	$(CC) $(OPT) deriveHorner.o -o deriveHornerd
	@echo "executable crée !" 

deriveHornerd.o : deriveHornerd.c
	$(CC) $(OPT) -c deriveHornerd.c 
	@echo "objets crées !"

clean : 
	rm *.o deriveHorner deriveHornerd
	@echo "ménage fait !"
