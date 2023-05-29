CC = gcc

OPT = -g

ln10+6x : ln10+6x.o
	$(CC) $(OPT) ln10+6x.o -o ln10+6x
	@echo "executable crée !" 



ln10+6x.o : ln10+6x.c
	$(CC) $(OPT) -c ln10+6x.c
	@echo "objets crées !"

clean : 
	rm *.o ln10+6x
	@echo "ménage fait !"
