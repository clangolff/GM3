c tests matmul on large matrices
      program mdown
      implicit none
      integer n,i
      double precision, dimension(:,:), allocatable :: l,il,r
      double precision, dimension(:), allocatable :: c,y

      n=5
      allocate(l(n,n))
      allocate(il(n,n))
      allocate(r(n,n))
      allocate(y(n))
      allocate(c(n))

      l(:,1) =( /1.,0.,0.,0.,0./)
      l(:,2) =( /0.5,0.3333,0.,0.,0./)
      l(:,3) =( /0.3333,0.25,0.2,0.,0./)
      l(:,4) =( / 0.25,0.2,0.1667,0.1429,0./) 
      l(:,5) =( / 0.25,0.2,0.1667,0.1429,0.125/)
      l = transpose(l)

      do i=1,n
        write(*,*) real(l(i,:))
      enddo
      write(*,*) 

      call inve(n,l,il,c,y)
      do i=1,n
        write(*,*) real(il(i,:))
      enddo
      write(*,*) 
       
      r = matmul(l,il)
      do i=1,n
        write(*,*) real(r(i,:))
      enddo
      
      deallocate(l)
      deallocate(c)
      deallocate(y)
      deallocate(r)
      end

