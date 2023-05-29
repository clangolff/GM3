c*****************
c zero machine
c************

      program zero
      implicit none
      real x
      integer n,i

      n=60
      x=1.
      do i=1,n
        x = x/10
        write(*,*) i,x
      enddo

      end
