c tests where on large matrices
      program tw
      implicit none
      integer n,i,j,k
      double precision se
      double precision, dimension(:,:), allocatable :: a,b

      read(*,*) n,se
      allocate(a(n,n))
      allocate(b(n,n))

      call random_number(a)
      call random_number(b)
      call system('date')
      where (a > se)
         a = log(a)
      endwhere
      call system('date')
      do i=1,n
        do j=1,n
          if (b(i,j) > se ) then
             b(i,j) = log(b(i,j))
          endif
        enddo
      enddo
      call system('date')

      deallocate(a)
      deallocate(b)

      end 
      
