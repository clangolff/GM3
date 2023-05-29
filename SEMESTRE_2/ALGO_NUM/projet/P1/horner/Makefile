CC = gcc

OPT = -g

horner : horner.o
	$(CC) $(OPT) horner.o -o horner 
	@echo "executable crée "

horner.o : horner.c
	$(CC) $(OPT) -c horner.c  
	@echo "objets crées !"

hornerd : hornerd.o
	$(CC) $(OPT) hornerd.o -o hornerd 
	@echo "executable crée "

hornerd.o : hornerd.c
	$(CC) $(OPT) -c hornerd.c  
	@echo "objets crées !"

clean : 
	rm *.o horner hornerd
	@echo "ménage fait !"
