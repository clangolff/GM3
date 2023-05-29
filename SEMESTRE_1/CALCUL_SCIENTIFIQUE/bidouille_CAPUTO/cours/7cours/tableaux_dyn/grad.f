       program grad
       implicit none
       integer, dimension (:,:), allocatable :: nab
       integer n,m,il,jd,ja

       read(*,*) n,m

       allocate(nab(m,n))
       nab=0

       do il =1,m
         read(*,*) jd,ja
         nab(il,jd)=-1
         nab(il,ja)=1
       enddo

       write(*,*)nab

       deallocate(nab)
       end
