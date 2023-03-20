        program cholesky               
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

        do j=1,n
                do i=j,n
                        do k=1,j-1
                                A(i,j) = A(i,j) - A(i,k) * A(j,k)
                        enddo
                        if(i==j)then
                                A(i,j) = sqrt(A(i,j))
                        else 
                                A(i,j) = A(i,j)/A(j,j)
                        endif
                enddo
        enddo
        
        do i=1,n
                write(*,*) A(i,1:n)
        enddo

        end
                
        
