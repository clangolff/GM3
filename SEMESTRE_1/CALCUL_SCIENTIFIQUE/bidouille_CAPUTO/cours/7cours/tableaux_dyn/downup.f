c---------------------------------------
c descente et remontee 
c LUX = B
c LY =B  UX = Y
c---------------------------------------
      subroutine  downup(n,l,u,b,x,y)
      implicit none
      double precision l(n,n),u(n,n),b(n),x(n),y(n),s
      integer i,j,n

c descente LY = B
      do i=1,n
cc         s = 0.d0
cc         do j=1,i-1
cc           s = s + l(i,j)*y(j)
cc         enddo
cc         y(i) = b(i) -s
        y(i) = b(i) - sum(l(i,1:i-1)*y(1:i-1))
      enddo


c remontee UX = Y
      do i=n,1,-1
cc         s = 0.d0
cc         do j=i+1,n
cc           s = s + u(i,j)*x(j)
cc         enddo
cc         x(i) = (y(i) -s)/u(i,i)
        x(i) = (y(i) - sum(u(i,i+1:n)*x(i+1:n)))/u(i,i)
      enddo

      return
      end

           
