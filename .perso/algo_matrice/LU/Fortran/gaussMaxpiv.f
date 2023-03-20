        program gauss               
        implicit none
        double precision,dimension(:,:),allocatable :: A
        double precision,dimension(:), allocatable :: b,X,temp
        integer i,n,k,j,lpiv
        double precision pivot 

        read(*,*) n

        allocate(A(n,n))
        allocate(b(n))
        allocate(X(n))
        allocate(temp(n))

        do i=1,n
                read(*,*) A(i,1:n)
        enddo
        read(*,*)
        read(*,*) b

        do k=1,n-1
                lpiv = maxloc(abs(A(k:n,k)),1)
                lpiv = lpiv+k-1
                temp(k:n) = A(k,k:n)
                A(k,k:n) = A(lpiv,k:n)
                A(lpiv,k:n) = temp(k:n)

                A(k+1:n,k) = A(k+1:n,k)/A(k,k)
                do i=k+1,n
                        A(i,k+1:n) = A(i,k+1:n) - A(i,k) * A(k,k+1:n)
                enddo
        enddo
        
        do i=1,n
                write(*,*) A(i,1:n)
        enddo
        deallocate(A)
        deallocate(b)
        deallocate(temp)
        deallocate(X)
        end
                
 
