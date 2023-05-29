clear;reset
set logscale y
set xrange[0:55]
set yrange[1e-16:1]
f(x) = 1/(2**x)
p 'rbcch' u 1:4 w linespoints,f(x) , 'rncch' u 1:3 w linespoints
#p 'rbcch' u 1:4 w linespoints,f(x) 


