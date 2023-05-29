      program main
      implicit none
      integer n,nmax,i,j
      parameter (nmax = 4)

      real a(nmax,nmax)

      read(*,*) n
      call sub(a,n)
      write(*,*) ((a(i,j),i=1,n),j=1,n)

      stop
      end

      subroutine sub(a,n)
      implicit none
      integer n,i,j

      real a(n,n)

      do i=1 , n
         do j=1,n
           a(i,j) = i+j +i*i
         end do
      end do

      return
      end

