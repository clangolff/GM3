c logistic map

       program logi
       implicit none
       real :: x ,a
       integer n,i

       read(*,*) n,x,a 

c       write(*,*) n 
       do i =1,n
         x = a*x*(1-x)
c         write(*,*) x
         write(*,*) i,x
       enddo

       end
