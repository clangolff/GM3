c---------------------
c  bisection sur f
c  entree a b f tol nmax 
c  sortie a b ibis 
c
c  ibis = 0 converge
c  ibis = 1 nmax iterations sans converger
c  ibis = -1 racine pas encadree
c---------------------------

      program mbcch
      use modcch
      implicit none
      double precision a, b, cch, tol
      integer nmax,ibis
      external cch

      read(*,*) a, b,tol, nmax, w

      call bis ( a, b, cch, tol, nmax ,ibis)

      end
