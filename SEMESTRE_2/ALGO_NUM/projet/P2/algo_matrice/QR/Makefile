CC = gcc

OPT = -g

decompoQR : decompoQR.o
	$(CC) $(OPT) decompoQR.o -o decompoQR -lm # Biblio math à l'intérieur
	@echo "Executable crée !" 

decompoQR.o : decompoQR.c
	$(CC) $(OPT) -c decompoQR.c 
	@echo "Objet créé !"

clean : 
	rm *.o decompoQR
	@echo "Ménage fait !"
