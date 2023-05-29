      subroutine lu(n,A,L)
      implicit none
      double precision, dimension(n,n) :: A,L
      integer i,j,n

!décomposition de cholesky de A=LL_t    
      L(:,:)= 0.0d0 

      do j=1,n       
        L(j,j)=sqrt(A(j,j)-sum(L(j,1:j-1)**2))
        do i=j+1,n
          L(i,j)=(A(i,j)-sum(L(j,1:j-1)*L(i,1:j-1)))/L(j,j)
        enddo
      enddo

      return
      end

