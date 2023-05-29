clear;reset;
set xrange[5:22];
set xtics (6,8,10,12,14,16,18,20,22)
set yrange[2:9];
set ytics ("-80" -80,"" -60, "-40" -40, "" -20,\
"0" 0, "" 20,"40" 40,"" 60,"80" 80)
set ytics 2,1,9 
set xlabel "1/{/Symbol n}"
set ylabel '<R>'
set nokey
f(x) = 0.32/x;
g(x) = x/1.77;
set label 'b=0.0062' at 14,7
set label '0.0094' at 14,5
set label '0.0125' at 14,3.5
set label '0.0187' at 14,2.5
#
# (f($1)):(g($3)) colonnes 1 (x) 3 (y) en utilisant
#les fonctions f et g
#
p 'h=0.002'u (f($1)):(g($3)) w linespoints \
,'h=0.003'u (f($1)):(g($3))  w linespoints\
,'h=0.004'u (f($1)):(g($3))  w linespoints\
,'h=0.005'u (f($1)):(g($3))  w linespoints
set term postscript eps enhanced 20; set output "r1oo.eps";replot

