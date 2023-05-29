        program grad              
        implicit none
        double precision,dimension(:,:),allocatable :: A
        double precision,dimension(:), allocatable :: b,X,r
        integer n,i,nMax
        double precision tol,normeR,alpha

        read(*,*) n,nMax,tol

        allocate(A(n,n))
        allocate(b(n))
        allocate(X(n))
        allocate(r(n))

        do i=1,n
                read(*,*) A(i,1:n)
        enddo
        read(*,*)
        read(*,*) b
        read(*,*) X

        r = b - matmul(A,x)

        do i =1,nMax
                normeR = dot_product(r,r)
                write(*,*) i , normeR
                if(normeR<tol) then
                        exit
                endif
                alpha = normeR/dot_product(matmul(A,r),r)
                X = X + alpha * r
                r = b - matmul(A,x)        
        enddo        


        
       
        write(*,*) X
       

        deallocate(A)
        deallocate(b)
        deallocate(X)
        deallocate(r)
        end
                
        
