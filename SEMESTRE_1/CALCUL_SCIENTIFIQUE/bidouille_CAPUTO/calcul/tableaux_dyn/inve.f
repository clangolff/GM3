c inversion matrice triang <
c entrees n ,l, 
c sortie il

      subroutine  inve(n,l,il,c,y)
      implicit none
      integer n,i,j
      double precision, dimension(n,n) :: l,il
      double precision, dimension(n) :: y,c

      do j=1,n
        c=0.
        c(j)=1.
        do i=1,n
         y(i)=(c(i)-sum(l(i,1:i-1)*y(1:i-1)))/l(i,i)
        enddo
        il(:,j)=y
      enddo
      end

