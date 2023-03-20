        program gauss               
        implicit none
        double precision,dimension(:,:),allocatable :: A
        double precision,dimension(:), allocatable :: b,X
        integer i,n,k,j
        double precision pivot 

        read(*,*) n

        allocate(A(n,n))
        allocate(b(n))
        allocate(X(n))

        do i=1,n
                read(*,*) A(i,1:n)
        enddo
        read(*,*)
        read(*,*) b

        do k=1,n-1
                if (A(k,k) == 0) then
                        write(*,*) "erreur pivot nul"
                        exit
                endif
                A(k+1:n,k) = A(k+1:n,k)/A(k,k)
                do i=k+1,n
                        A(i,k+1:n) = A(i,k+1:n) - A(i,k) * A(k,k+1:n)
                enddo
        enddo
        
        do i=1,n
                write(*,*) A(i,1:n)
        enddo

        end
                
        
