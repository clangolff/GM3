reset
unset label
set trange[0:0.0001]
plot [3:9] [0:0.00015] 1/((x+1)*3**x)
set output "k7.svg"

