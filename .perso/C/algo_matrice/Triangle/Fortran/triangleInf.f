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

        X(1) = b(1)/T(1,1)
        
        do i=2,n
                X(i) = (b(i)-sum(X(1:i-1)*T(i,1:i-1)))/T(i,i)
        enddo

        write(*,*) X

        end
                
        
