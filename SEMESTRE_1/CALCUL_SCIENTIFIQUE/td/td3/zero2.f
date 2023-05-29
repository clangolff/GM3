c*****************
c zero machine
c************

      program zero
      implicit none
      double precision x
      integer n,i

      n=400
      x=1.d0
      do i=1,n
        x = x/10.d0
        write(*,*) i,x
      enddo

      end
