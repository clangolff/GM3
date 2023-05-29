reset
unset label
set trange[0:0.0001]
plot [1:6] [0:0.0002] 1/((x+1)*9**(x+1))
set output "n3.svg"

