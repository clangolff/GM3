#!/bin/bash

#Exercice 1

#1.1
Va=16

#1.2
echo la variable Va vaut $Va

#1.3
echo Va + 5 = $((Va+5))

#1.4
echo Va mod 5 = $((Va%5))

#1.5
echo "scale=3; $Va / 3" |bc

#Exercice2

#2.1
((Va++))
echo incrementer Va = $Va

#2.2
Vb=$((Va-14))
echo Vb = $Vb

#2.3
echo calcul de puissance 3 = $((Vb**3))

#Exercice 3

#3.1
Txt=Bonjour

echo \$Txt = \"$Txt\"

#3.2
echo ${Txt:0:3}

#3.3
echo ${Txt: -3}

#3.4
echo ${Txt%%o*}

#3.5
echo ${Txt%o*}

#3.6
echo ${Txt//o/#}

#3.7
echo ${Txt/Bon/Un }

#Exercice 4

#4.1
read -p "entrez votre prénom : " Prenom

#4.2
Prenom=${Prenom:-Inconnu}

#4.3
echo "Bonjour cher" ${Prenom^^}

#4.4
echo nombre de lettre ${#Prenom}
