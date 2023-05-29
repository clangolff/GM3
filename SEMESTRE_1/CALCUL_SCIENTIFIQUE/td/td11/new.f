c---------------------
c  newton sur f
c  entree x0 f df tol nmax 
c  sortie x0 inew 
c
c  inew = 0 converge
c  inew = 1 nmax iterations sans converger
c---------------------------


      subroutine new ( x0, f, df, tol, nmax ,inew)
      implicit none
      double precision x0, f, df, tol,res
      integer i,nmax,inew


      do i=1, nmax

       res = -f(x0)/df(x0)
       if (abs(res) < tol) then
         inew = 0
         return
       endif
       x0 = x0 + res
       write(*,*) i , x0, abs(res)

      enddo 
      inew = 1
      return

      end 
