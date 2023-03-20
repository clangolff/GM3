        program grad              
        implicit none
        double precision,dimension(:,:),allocatable :: A
        double precision,dimension(:), allocatable :: b,X,r0,r1,p,Ap
        integer n,i,nMax
        double precision tol,normeR0,normeR1,alpha,beta

        read(*,*) n,nMax,tol

        allocate(A(n,n))
        allocate(b(n))
        allocate(X(n))
        allocate(r0(n))
        allocate(r1(n))
        allocate(p(n))
        allocate(Ap(n))

        do i=1,n
                read(*,*) A(i,1:n)
        enddo
        read(*,*)
        read(*,*) b
        read(*,*) X

        r0 = b - matmul(A,x)
        p = r0
        normeR0 = dot_product(r0,r0)
        do i =1,nMax
                Ap = matmul(A,p)
                write(*,*) i , normeR0
                if(normeR0<tol) then
                        exit
                endif
                alpha = normeR0/dot_product(Ap,p)
                X = X + alpha * p
                r1 = r0 - alpha * Ap
                normeR1 =  dot_product(r1,r1)
                beta = normeR1 / normeR0
                p = r1 + beta * p

                r0 = r1
                normeR0 = normeR1        
        enddo        


        
       
        write(*,*) X
       

        deallocate(A)
        deallocate(b)
        deallocate(X)
        deallocate(r0)
        deallocate(r1)
        deallocate(p)
        deallocate(Ap)
        end
                
        
