      program mlu
      implicit none;
      double precision eps
      double precision, dimension(:,:), allocatable :: A,L,uni
      double precision, dimension(:), allocatable ::x,b,y
      integer ic,i,j,n

      read(*,*) n  
      allocate(A(n,n))
      allocate(L(n,n))
      allocate(uni(n,n))
      allocate(b(n))
      allocate(x(n))
      allocate(y(n))

      do i=1,n
         do j=1,n
            A(i,j) = 1.d0/(i+j-1.d0)
         enddo
      enddo     

c affichage matrice / ligne
cc      do i=1,n
cc            write(*,*) A(i,:)
cc      enddo
      write(*,*)
c pour avoir x=1
      b = sum(A,dim=2)
cc      write(*,*) b
      write(*,*) 
     
      call lu(n,A,L)
      do i=1,n
c            write(*,*) L(i,:)
      enddo
      write(*,*) 

      call downup(n,L,b,x,y)
      write(*,*) 
      write(*,*) x 
      write(*,*) 
      write(*,*) norm2(matmul(A,x)-b)
      write(*,*) maxval(matmul(A,x)-b)

      deallocate(A)
      deallocate(L)
      deallocate(x)
      deallocate(b)      
      end program

