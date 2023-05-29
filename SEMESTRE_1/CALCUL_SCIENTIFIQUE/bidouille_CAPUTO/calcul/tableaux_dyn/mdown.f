c tests matmul on large matrices
      program mdown
      implicit none
      integer n,i
      real, dimension(:,:), allocatable :: a,l
      real, dimension(:), allocatable ::x,b 

      read(*,*) n
      allocate(a(n,n))
      allocate(l(n,n))
      allocate(b(n))
      allocate(x(n))

      call random_number(a)
      l=0.
      do i=1,n
        l(i,1:i) = a(i,1:i)
      enddo
      b = sum(l,dim=2)
cc      do i=1,n
cc        write(*,*) l(i,:) , b(i)
cc      enddo

      call down(n,l,b,x)
      write(*,*) x

      deallocate(a)
      deallocate(l)
      deallocate(x)
      deallocate(b)
      end

