#tanh_lin
#stability criterion as a function of h for F=tanh
#C=1.;l=1; h=0.8; eps = 0.00; tau = 1 ;nf=1
clear;reset
#unset key
set xlabel 'h'
set ylabel 'k_+'
set xrange[0:0.8]
set yrange[0:1.6]
#set label 'unstable' at 0.2,0.35
#set label 'stable' at 0.5,0.1
#colonnes 1 (x) 4 (y)
plot 'd1' u 1:4 w l lw 2,'d1' u 1:3 w l
#set term postscript eps color enhanced 30 ; set out 'd1.eps';rep
