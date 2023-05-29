CC = gcc

OPT = -g

ln10 : ln10.o
	$(CC) $(OPT) ln10.o -o ln10
	@echo "executable crée !" 



ln10.o : ln10.c
	$(CC) $(OPT) -c ln10.c
	@echo "objets crées !"

clean : 
	rm *.o ln10
	@echo "ménage fait !"
