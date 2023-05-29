c---------------------
c  newton sur f
c  entree x0 f df tol nmax 
c  sortie x0 inew 
c
c  inew = 0 converge
c  inew = 1 nmax iterations sans converger
c---------------------------


      program mncch
      use modcch
      implicit none
      double precision x0, b, tol
      double precision , external :: cch,dcch
      integer nmax,inew
      

      read(*,*) x0, tol, nmax, w

      call new ( x0, cch, dcch, tol, nmax ,inew)

      end
