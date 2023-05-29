c---------------------
c  newton sur f
c  entree x0 f df tol nmax 
c  sortie x0 inew 
c
c  inew = 0 converge
c  inew = 1 nmax iterations sans converger
c---------------------------


      program mnf5
      use modf5
      implicit none
      double precision x0, tol
      double precision , external :: f5,df5
      integer nmax,inew
      

      read(*,*) x0, tol, nmax, c

      call new ( x0, f5, df5, tol, nmax ,inew)

      end
