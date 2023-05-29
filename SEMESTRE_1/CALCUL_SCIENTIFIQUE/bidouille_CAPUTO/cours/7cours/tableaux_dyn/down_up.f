      program down_up
      implicit none
      integer i
      integer,parameter :: n
      real,allocatable l(n,n),u(n,n),x(n),y(n),b(n)

      read(*,*) l,u,b
      do i=1,n
         y(i)=(b(i)-sum(l(i,1:i-1)*b(i,1:i-1)))/l(i,i)
      enddo
      do i=n,1
         x(i)=(y(i)-sum(u(i,i+1:n)*b(i,i+1:n)))/u(i,i)
      enddo
      write(*,*) x  

      end
                                                                       
