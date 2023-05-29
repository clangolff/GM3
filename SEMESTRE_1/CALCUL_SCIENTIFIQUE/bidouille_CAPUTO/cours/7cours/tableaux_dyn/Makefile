#FC = fc
#FC = fort77
#FC = g77
FC = gfortran

#OPT = -O
#OPT = -p
OPT = -g

#logistic map to generate data
logi : logi.f
	$(FC) $(OPT) logi.f -o logi

#histogramme avec where  
hist : hist.f
	$(FC) $(OPT) hist.f -o hist

#histogramme avec count  
hist2 : hist2.f
	$(FC) $(OPT) hist2.f -o hist2

#teste matmul
mm : mm.f
	$(FC) $(OPT) mm.f -o mm

#gradient graphe
grad : grad.f
	$(FC) $(OPT) grad.f -o grad

#teste where
tw : tw.f
	$(FC) $(OPT) tw.f -o tw

#plus grandes p valeurs sur un tableau a(n)
tmax : tmax.f
	$(FC) $(OPT) tmax.f -o tmax

#plus grandes p valeurs sur une matrice a(n,n)
tmax2 : tmax2.f
	$(FC) $(OPT) tmax2.f -o tmax2

clean:
	rm mm grad tw tmax hist hist2 logi tmax2

