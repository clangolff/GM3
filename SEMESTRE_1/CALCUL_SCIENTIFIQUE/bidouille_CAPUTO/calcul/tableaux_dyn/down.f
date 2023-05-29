c tests matmul on large matrices
      subroutine  down(n,l,b,x)
      implicit none
      integer n,i
      real, dimension(n,n) :: l
      real, dimension(n) ::x,b 

      do i=1,n
        x(i)= (b(i)-sum(l(i,1:i-1) *x(1:i-1)) ) /l(i,i)  
      enddo
      end

