c p plus grandes valeurs dans un tableau a(n)
      program tmax
      implicit none
      integer n,p,j,m,k(1)
      real, dimension(:), allocatable :: a
      real :: mina

      read(*,*) n ,p , m
      allocate(a(n))

c m aiguillage
      if (m==0) then
        call random_number(a)
      else
        do j=1,n
          read(*,*) a(j)
        enddo
      endif

      mina = minval(a)


c      write(*,*) maxloc(a(1,:))
      do j=1,p
         k=maxloc(a)
         write(*,*) k(1),maxval(a)
         write(*,*) k,a(k(1))
         a(k)=mina
      enddo

      deallocate(a)

      end 
      
