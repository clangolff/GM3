      subroutine  downup(n,L,b,x,y)
      implicit none
      integer n,j
      double precision, dimension(n,n) :: L
      double precision, dimension(n) ::x,b,y

      ! résolution de Ly=b
      y(1)=b(1)/L(1,1)
      do j=2,n
       y(j)= (b(j)-sum(L(j,1:j-1)*y(1:j-1)))/L(j,j)
      enddo
      

      ! résolution de L_tx=y
      x(n)=y(n)/L(n,n)
      do j=n-1,1,-1
       x(j)= (y(j)-sum(L(j+1:n,j)*x(j+1:n)))/L(j,j)
      enddo
      return
      end

