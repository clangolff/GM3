#trace sin cos sur 0 pi
# diese commentaire ds script et fichier de donnees
set samples 5000
unset key
set xrange[0:pi]; 
set xtics ( '0' 0 , "{/Symbol p}/2" pi/2 ,"{/Symbol p}" pi)
set grid
set yrange[-1:1]
set xlabel "x"
set ylabel "sin  cos"
plot sin(x) w l lw 3, cos(x) w l lw 3
#pour generer du postcript decommenter la ligne suivante
#set term postscript eps enhanced color 30; set output "simple.eps";replot
#pour generer du png decommenter la ligne suivante
#set term png ; set output "simple.png";replot
