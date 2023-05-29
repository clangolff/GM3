CC = gcc

OPT = -g

IS : IS.o
	$(CC) $(OPT) IS.o -o IS
	@echo "executable crée !" 



IS.o : IS.c
	$(CC) $(OPT) -c IS.c
	@echo "objets crées !"

clean : 
	rm *.o IS
	@echo "ménage fait !"
