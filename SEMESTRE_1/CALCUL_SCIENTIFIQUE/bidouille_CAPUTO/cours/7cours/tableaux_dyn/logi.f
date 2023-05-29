c logistic map

       program logi
       implicit none
       real :: x ,a
       integer n,i

       read(*,*) n,x,a 

       write(*,*) n 
       do i =1,n
         x = a*x*(1-x)
         write(*,*) x
cc         write(*,*) i,x
       enddo

       end
