CC = gcc

OPT = -g

tchebychev : tchebychev.o
	$(CC) $(OPT) tchebychev.o -o tchebychev
	@echo "executable crée !" 

tchebychev.o : tchebychev.c
	$(CC) $(OPT) -c tchebychev.c
	@echo "objets crées !"

tchebychevd : tchebychevd.o
	$(CC) $(OPT) tchebychevd.o -o tchebychevd
	@echo "executable crée !" 

tchebychevd.o : tchebychevd.c
	$(CC) $(OPT) -c tchebychevd.c
	@echo "objets crées !"


clean : 
	rm *.o tchebychev tchebychevd
	@echo "ménage fait !"
