c tests matmul on large matrices
      program mm
      implicit none
      integer n,i,j,k
      double precision s
      double precision, dimension(:,:), allocatable :: a,b,c

      read(*,*) n
      allocate(a(n,n))
      allocate(b(n,n))
      allocate(c(n,n))

      call random_number(a)
      call random_number(b)
      call system('date')
      c = matmul(a,b)
      call system('date')
      do i=1,n
        do j=1,n
          s = 0.d0
          do k=1,n
            s = s+ a(i,k)*b(k,j)
          enddo
          c(i,j)=s
        enddo
      enddo
      call system('date')

      deallocate(a)
      deallocate(b)
      deallocate(c)

      end 
      
