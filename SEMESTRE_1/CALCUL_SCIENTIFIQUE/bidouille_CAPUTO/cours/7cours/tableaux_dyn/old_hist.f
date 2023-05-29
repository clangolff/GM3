c234567
      program hist
      implicit none
      integer i,ib,n,nb
      real hb,xm
      real , dimension(:), allocatable:: x,xb
      integer , dimension(:), allocatable:: b

      read(*,*) n,nb
      allocate (x(n))
      allocate (xb(nb))
      allocate (b(nb))
     
      read(*,*) x

      hb = 20./(nb-1)
      do ib=1,nb
       xb(ib)= (ib-1)*hb 
      enddo
      b = 0

      do i=1,n
        do ib=2,nb
         if(x(i) .ge. xb(ib-1) .and. x(i) .lt. xb(ib)) then
           b(ib-1) = b(ib-1)+1
         endif
        enddo
      enddo

c write histogram at the end
      do ib=1,nb-1
       xm = (xb(ib)+xb(ib+1))*0.5
       write(*,*) xm,b(ib)
      enddo
      end

       
