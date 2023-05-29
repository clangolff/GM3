c  attention bug corrige
c  piv=maxval(abs(A(j:n,j)))  pb qd pivot <0
c
c
c
c


      program gauss
      implicit none
      integer i,j,k,n,lpiv
      double precision piv,res

      double precision, dimension(:,:), allocatable :: A,As
      double precision, dimension(:), allocatable ::x,b,v

      read(*,*) n

      allocate(As(n,n))
      allocate(A(n,n+1))
      allocate(b(n))
      allocate(x(n))
      allocate(v(n+1))


! lecture 
      do i=1,n
        do j=1,n
          As(i,j)= 1.d0/(i+j-1.d0)
        enddo
      enddo
c      call random_number(As)
      b= sum(As,dim=2)
 

! forme A
      A(:,n+1)=b
      A(:,1:n)=As

      do  j=1,n 
             lpiv=maxloc(abs(A(j:n,j)),1)
             lpiv=lpiv+j-1
             piv = A(lpiv,j)
             A(lpiv,j:n+1)=A(lpiv,j:n+1)/piv
             v(j:n+1)=A(j,j:n+1)
             A(j,j:n+1)=A(lpiv,j:n+1)
             A(lpiv,j:n+1)=v(j:n+1)
             do k=j+1,n
                    A(k,j:n+1)=A(k,j:n+1)-A(k,j)*A(j,j:n+1)
             enddo               
      enddo
      x(n)=A(n,n+1)
      do i=n-1,1,-1
                x(i)=A(i,n+1)-sum(A(i,i+1:n)*x(i+1:n))
      enddo
      res = norm2(matmul(As,x)-b)
      write(*,*) res
      write(*,*) 
      write(*,*) x
      end 

