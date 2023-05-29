        program triangle                
        implicit none
        double precision,dimension(:,:),allocatable :: T
        double precision,dimension(:), allocatable :: b,X
        integer i,n

        read(*,*) n

        allocate(T(n,n))
        allocate(b(n))
        allocate(X(n))

        do i=1,n
                read(*,*) T(i,1:n)
        enddo
        read(*,*)
        read(*,*) b

        X(n) = b(n)/T(n,n)
        
        do i=n-1,1,-1
                X(i) = (b(i)-sum(X(i+1:n)*T(i,i+1:n)))/T(i,i)
        enddo

        write(*,*) X

        end
                
  
