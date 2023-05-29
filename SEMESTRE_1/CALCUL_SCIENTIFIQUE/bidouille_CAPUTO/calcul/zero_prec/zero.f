      program zero
      implicit none
      real x
      integer i,n


      n=50
      do i=1,n
       x = 10**(-i)
       write(*,*) i,x
      enddo

      end

