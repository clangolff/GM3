c p plus grandes valeurs dans un tableau a(n,n)
      program tmax2
      implicit none
      integer n,i,j,p
      real, dimension(:,:), allocatable :: a
      real :: mina
      integer :: k(2)

      read(*,*) n , p
      allocate(a(n,n))

      call random_number(a)
      mina = minval(a)

c      write(*,*) maxloc(a(1,:))
      do j=1, p
         k=maxloc(a)
cc         write(*,*) maxloc(a),maxval(a)
         write(*,*) k(1),k(2),a(k(1),k(2))
         a(k(1),k(2))=mina
      enddo

      deallocate(a)
      end 
      
