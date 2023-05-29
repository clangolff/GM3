#hamiltonian
# diese commentaire ds script et fichier de donnees
lj = 0.32;
v(x,y) = 0.5*y**2 + (1-cos(x))/(lj**2) + 0.5*x**2
set samples 5000
set cntrparam levels discrete 0.1, 1, 5, 17., 25.0360499136927, 30.,40.,50 
unset key
unset surface;set contour
xmax = 10
set xrange[-xmax:xmax]
set yrange[-xmax:xmax]
set xtics -xmax,xmax,xmax  
set ytics -xmax,xmax,xmax  
unset ztics
set view 0,0
set xlabel "{/Symbol f}"
set ylabel "{/Symbol f}_t"
splot v(x,y) w l lw 3
#set term postscript eps enhanced color 30; set output "ham.eps";replot
set term postscript eps enhanced 30; set output "ham.eps";replot
