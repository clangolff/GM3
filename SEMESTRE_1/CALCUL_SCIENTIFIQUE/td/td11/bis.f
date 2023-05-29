c---------------------
c  bisection sur f
c  entree a b f tol nmax 
c  sortie a b ibis 
c
c  ibis = 0 converge
c  ibis = 1 nmax iterations sans converger
c  ibis = -1 racine pas encadree
c---------------------------


      subroutine bis ( a, b, f, tol, nmax ,ibis)
      implicit none
      double precision a, b, f, tol, fa,fb,fm,m,afa
      integer i,nmax,ibis


      fa = f(a)
      fb = f(b)

c racine pas encadree
      if (fa*fb > 0 ) then
         ibis = -1
         return
      endif

      do i=1, nmax

       m = (a+b)/2
       fm = f(m)
       if (fa*fm < 0.d0 ) then
         b  = m
         fb = fm
       else
         a  = m
         fa = fm
       endif

c       afa = abs(fa)
       afa = abs(a-b)
       write(*,*) i , a, b, afa
       if (afa < tol) then
         ibis = 0
         return
       endif

      enddo 
      ibis = 1
      return

      end 
